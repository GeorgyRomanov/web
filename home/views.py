from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
	return HttpResponse('<h3>Welcome<h3>')


def about(request):
	return HttpResponse('<h3>About us<h3>')
