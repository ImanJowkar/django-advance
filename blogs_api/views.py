from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from blogs.models import Post
# Create your views here.


class APIPostListView(APIView):
    def get(self, request):
        return Response('ok')


