from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def main(request):
    """homepage"""
    return HttpResponse("hello world")
