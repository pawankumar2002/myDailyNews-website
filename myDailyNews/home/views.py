from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.

def home(request,category=''):
    url=f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey=2668032f963e4e72b05ab422b6026554"
    response = requests.get(url)
    articles=response.json()['articles']
    context={'articles':articles}
    return render(request,'home.html',context)
