from django.contrib import admin
from django.urls import path, include
from analysis.views import AnalysisView

urlpatterns = [
    path("", AnalysisView.as_view(), name="analysis")
]
