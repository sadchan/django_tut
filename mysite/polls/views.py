from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, you're in the polls app now")
# Create your views here.
