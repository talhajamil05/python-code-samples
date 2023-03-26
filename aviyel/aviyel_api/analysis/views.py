import csv
import os
from statistics import mean

import isodate
import pandas as pd
from apiclient.discovery import build
from django.http.response import JsonResponse
from dotenv import load_dotenv
from rest_framework.views import APIView

load_dotenv()

YOUTUBE = build("youtube", "v3", developerKey=os.environ.get("GOOGLE_API_KEY", None))


class AnalysisView(APIView):
    """
    Class for Analysis
    """

    def extract_video_ids(self, results):
        """
        Method to extract video Ids from search results
        """
        ids = [item["id"]["videoId"] for item in results]
        return ids

    def post(self, request):
        """
        Post method, accepts  a request, Creates excel file for stats
        """
        keyword = request.data.get("keyword", None)

        if not keyword or type(keyword) is not str:
            return JsonResponse("Please provide a keyword argument of type string")

        data = pd.DataFrame(columns=["video_id", "category", "duration", "tags"])
        search_results = []
        video_details = []
        video_ids = []
        max_results = 50
        max_pages = 6

        search_query = YOUTUBE.search().list(
            q=keyword, part="snippet", type="video", maxResults=max_results
        )

        result = search_query.execute()
        next_page_token = result["nextPageToken"]
        search_results.extend(result["items"])
        video_ids.extend(self.extract_video_ids(result["items"]))

        for i in range(max_pages):
            search_query = YOUTUBE.search().list(
                q="Countless Storeys",
                part="snippet",
                type="video",
                maxResults=max_results,
                pageToken=next_page_token,
            )
            result = search_query.execute()
            search_results.extend(result["items"])
            next_page_token = result["nextPageToken"]
            video_ids.extend(self.extract_video_ids(result["items"]))

        index = 0
        for index in range(len(video_ids)):
            video_query = YOUTUBE.videos().list(
                id=video_ids[index],
                part=["snippet", "contentDetails"],
            )
            video_detail = video_query.execute()
            video_item = video_detail["items"][0]
            duration = isodate.parse_duration(
                video_item["contentDetails"]["duration"]
            ).total_seconds()

            tags = video_item["snippet"].get("tags", None)
            category_id = video_item["snippet"]["categoryId"]
            category_query = category_query = YOUTUBE.videoCategories().list(
                id=category_id, part="snippet"
            )
            category_result = category_query.execute()
            category_name = category_result["items"][0]["snippet"]["title"]
            data.loc[index] = [video_ids[index], category_name, duration, tags]

        data.to_csv(f"./aviyel_api/input_files/{keyword}.csv")

        return JsonResponse("Input File generated for the provided keyword")

    def get(self, request):
        """
        Get method to generate excel files for the input files
        """
        keyword = request.GET.get("keyword", None)
        if not keyword or not os.path.exists(f"./aviyel_api/input_files/{keyword}.csv"):
            return JsonResponse(
                "Input file not found for the provided keyword", safe=False
            )

        search_data = pd.read_csv(f"./aviyel_api/input_files/{keyword}.csv")

        number_of_videos = search_data["category"].value_counts().to_dict()

        categories = number_of_videos.keys()

        max_tag_videos = max(number_of_videos, key=number_of_videos.get)
        min_tag_videos = min(number_of_videos, key=number_of_videos.get)
        min_max_tag_videos = {
            "Category with Max Videos": max_tag_videos,
            "Category with Min Videos": min_tag_videos,
        }

        average_durations = self.get_average_duration(categories, search_data)

        max_index = search_data["duration"].idxmax()
        min_index = search_data["duration"].idxmin()
        max_duration_category = search_data["category"][max_index]
        min_duration_category = search_data["category"][min_index]
        min_max_duration = {
            "Category with Max Duration": max_duration_category,
            "Category with Min Duration": min_duration_category,
        }

        classified_tags = self.classify_tags(categories, search_data)

        self.write_csv(
            "./aviyel_api/output_files/number_of_videos.csv",
            number_of_videos,
            ["Category", "# of Videos"],
        )
        self.write_csv(
            "./aviyel_api/output_files/min_max_tag_videos.csv", min_max_tag_videos
        )
        self.write_csv(
            "./aviyel_api/output_files/average_durations.csv",
            average_durations,
            ["Category", "Time(Seconds)"],
        )
        self.write_csv(
            "./aviyel_api/output_files/min_max_tag_durations.csv", min_max_duration
        )
        self.write_csv(
            "./aviyel_api/output_files/classified_tags.csv",
            classified_tags,
            ["Category", "Tags"],
        )

        return JsonResponse(
            "Files Generated successfully for the given keyword", safe=False
        )

    def get_average_duration(self, categories, search_data):
        """
        Method to calculate average duration for each category
        """
        durations = {}
        for category in categories:
            category_values = search_data.loc[search_data["category"] == category]
            durations[category] = round(mean(category_values["duration"]), 2)

        return durations

    def classify_tags(self, categories, search_data):
        """
        Method to classify tags in each category
        """
        classified_tags = {}
        for category in categories:
            category_tags = search_data.loc[search_data["category"] == category]
            tags = category_tags["tags"].dropna().unique()
            classified_tags[category] = tags

        return classified_tags

    def write_csv(self, path, data, columns=None):
        with open(path, "w") as csv_file:
            writer = csv.writer(csv_file)
            if columns:
                writer.writerow(columns)
            for key, value in data.items():
                writer.writerow([key, value])
