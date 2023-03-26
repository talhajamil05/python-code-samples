from django.shortcuts import render
from braces.views import CsrfExemptMixin
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import *
from .models import *


class LogStringListView(CsrfExemptMixin, ListAPIView):
    """
    Log List String VIEW
    """
    serializer_class = LogStringSerializer
    queryset = Log.objects.all().order_by('-created_on')


class LogListView(CsrfExemptMixin, ListAPIView):
    """
    Log List View
    """
    serializer_class = LogSerializer
    queryset = Log.objects.all().order_by('-created_on')


class CreateMessageAPIView(CsrfExemptMixin, CreateAPIView):
    """
    Create Message View
    """
    serializer_class = MessageSerializer
