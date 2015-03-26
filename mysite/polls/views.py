from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
