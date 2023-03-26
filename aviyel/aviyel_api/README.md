# AVIYEL

# Requirements
1. Python 3.8.10

# Setup
1. Make sure python 3.8.10 is installed in the system either as default python version or through pyenv.
2. Navigate to aviyel_api folder
3. Add the value for GOOGLE_API_KEY in the .env file
4. Run the following commands to get started
```
1. pipenv shell
2. pip install -r requirements.txt
3. python manage.py runserver
```

### API_ENDPOINTS

1. The task is implemented as a simple Django Rest Framework API.
2. The base url is ```http://127.0.0.1:8000/analysis/```
3. The endpoint has two methods that is ```GET``` and ```POST```


### POST
The post method is used to generate the input file for the given keyword. It utilizes the YOUTUBE data API to get list as well as details of each video. To run, use POSTMAN or some other API testing tool and hit ```http://127.0.0.1:8000/analysis/``` with the following body with content-type ```application/json```
```
{"keyword": "travel"}
```
Hitting the endpoint will search, clean and then generate a file in the ```input_files``` folder which can then be used for running the analysis.

### GET
The get method is used to run the analysis on the generated input file. To run the analysis, hit the following endpoint with keyword as the query param ```http://127.0.0.1:8000/analysis/?keyword=travel```
Hitting the endpoint will generate csv files in the ```ouput_files``` folder with the required analysis written into each file.

### OVERVIEW
1. File operations were used to write and read the data gathered from Youtube API instead of database because running query operations to save and load the data would have been expensive instead of writing and reading from the file
2. The decision to implement an API instead of a python script was taken to provide flexibility. The POST method can be used to generate the data for the given keyword and the GET method can be used to run analysis on the generated input file.
3. Pandas and Numpy were primarily used for analysis whereas Django Rest Framework was used to implemnent the API
4. Input file and output files are generated and attached for testing for the keyword ```travel```
