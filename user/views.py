from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Post,Profile
# Create your views here.
def home(request):
	if request.method=="POST":
		caption=request.POST.get("caption")
		image=request.FILES.get("image")
		user=request.user
		user=Post(caption=caption,image=image,user=user)
		user.save()
		messages.success(request,"Uploaded Successfully")
	allPost=Post.objects.all()
	data={
		'posts':allPost
	}
	return render(request,'user/feed.html',data)
def delete_post(request,pk):
	post= Post.objects.get(id=pk)
	post.delete()
	messages.error(request,"Deleted Successfully!")
	return redirect("home_page")
def profile_view(request,username):
	userdata= User.objects.filter(username=username)
	if userdata:
		profile=Profile.objects.get(user=userdata[0])
		data={
			'profile':profile
		}
		return render(request,"user/profile.html",data)
	else:
		messages.error(request,"User does not exist!")
		return redirect("home_page")