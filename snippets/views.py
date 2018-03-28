from django.shortcuts import render
from django.http import HttpResponse

def create(request):
	return HttpResponse("Create function")

def view(request, key):
	return HttpResponse("View function: " +str(key))


