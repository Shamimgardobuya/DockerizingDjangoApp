from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def docker_lite_message(request):
    return HttpResponse("Hello world, today we will learn devops basics")
