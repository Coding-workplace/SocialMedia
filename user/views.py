from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Post
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