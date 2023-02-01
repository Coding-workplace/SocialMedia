from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from user.models import Profile
# Create your views here.
def signup_view(request):
	'''Signup Page'''
	if request.method == 'POST':
		username=request.POST.get('username')
		email=request.POST.get('email')
		password=request.POST.get('password')
		cPassword=request.POST.get('confirmPassword')
		checkUser=Profile.objects.filter(username=username)
		if checkUser:
			messages.error(request,"User with this username already exists!")
			return redirect("/")
		else:
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
			return redirect("home_page")
		else:
			messages.error(request,"Invalid Credentials!")
	return HttpResponse("Get request")
def logout_view(request):
	logout(request)
	messages.success(request,"Logout Successfully!")
	return redirect("/")