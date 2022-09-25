from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
# API import
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework import status
from App_Article.models import Blog
from App_Article.serializers import BlogSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def Article(request):
    if request.method == 'GET':
        all_post = Blog.objects.all()
        serializer = BlogSerializer(all_post, many=True)
        return Response(serializer.data)


    def startCall(request):
        if request.method == "POST":
            serializer = BlogSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #Return this if request method is not POST
        return Response({'key': 'value'}, status=status.HTTP_200_OK)


def ArticleDetails(request, id):
    pass
