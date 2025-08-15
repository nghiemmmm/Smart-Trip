from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def main_view(request):
    return HttpResponse("Hello, this is the main view of the API.")
# from .views import *  # Import tất cả models từ package models/