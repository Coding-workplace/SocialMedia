from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
# Create your views here.
def signup_view(request):
	'''Signup Page'''
	if request.method == 'POST':
		username=request.POST.get('username')
		email=request.POST.get('email')
		password=request.POST.get('password')
		cPassword=request.POST.get('confirmPassword')
		if password == cPassword and password != "":
			user=User.objects.create_user(username=username,email=email,password=password)
			user.save()
			messages.success(request,"User created")
		else:
			messages.error(request,"Password and Confirm Password doesn't match or empty")
	return render(request,"account/signup.html")
def login_view(request):
	'''login'''
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			messages.success(request,"Login Successfully!")
			return HttpResponse("login succesfully")
		else:
			messages.error(request,"Invalid Credentials!")
			return HttpResponse("invalid credentials")
	return HttpResponse("Get request")