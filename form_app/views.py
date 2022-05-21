from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.


def index(request):
    return HttpResponse('<h1>THIS IS FORM_APP</h1>')
