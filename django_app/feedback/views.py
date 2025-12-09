from django.shortcuts import render

from rest_framework import generics
from .models import Feedback
from .serializers import FeedbackSerializer
# import requests

class FeedbackListCreate(generics.ListCreateAPIView):
    queryset = Feedback.objects.all().order_by('-created_at')
    serializer_class = FeedbackSerializer

    def perform_create(self, serializer):
        #это для апи
        serializer.save(sentiment=None, summary=None, categories=None)
