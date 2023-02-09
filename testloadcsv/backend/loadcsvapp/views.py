from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import os
import pandas as pd
import json

from rest_framework import generics
from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer

posts = [{
    'author': 'Anna',
    'title': 'Blog post 1'}]
    
def index(request):
    context = {'posts': posts}
    return render(request, 'index.html', context)

#def index(request):
#    return HttpResponse("Hello World") 

class BlogView(viewsets.ModelViewSet):
   	queryset = Blog.objects.all()
   	serializer_class = BlogSerializer

class EndpointView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class= BlogSerializer

class HelloWorld(APIView):
    def get(self, request, format=None):
        #data = {'message': 'Hello World!'}
        d = os.getcwd() # how we get the current dorectory
        name = 'gdp.csv'
        file_directory = d+'\media\\'+name #saving the file in the media directory
        print(file_directory)
        df = json.loads(pd.read_csv(file_directory).sample(10).to_json(orient='records'))
        print(df)
        return Response(df)

def get_data(request):
    data = {"message": "Hello, World!"}
    return JsonResponse(data)

                                
