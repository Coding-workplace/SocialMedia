from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login_view(request):
	'''Login Page'''
	return render(request,"account/signup.html")