from django.shortcuts import render
from django.http import HttpResponse

def bookticket(request):
	return HttpResponse("This application is for booking air tickets")
# Create your views here.
