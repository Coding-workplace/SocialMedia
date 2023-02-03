from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	image=models.ImageField()
	caption=models.TextField()
	date=models.DateField(auto_now_add=True,null=True)
	def __str__(self):
		
		 return '%s %s' % (self.user, self.caption[:20])
class Profile(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	bio=models.CharField(max_length=50)
	followers=models.IntegerField(default=0)
	following=models.IntegerField(default=0)
	image=models.ImageField()
	def __str__(self):
		 return str(self.user)
class Like(models.Model):
	user=models.ManyToManyField(User)
	post=models.OneToOneField(Post,on_delete=models.CASCADE)
	likes=models.IntegerField(default=0)
	@classmethod
	def like(cls,post,liking_user):
		obj,create=cls.objects.get_or_create(post=post)
		obj.user.add(liking_user)

	@classmethod
	def dislike(cls,post,disliking_user):
		obj,create=cls.objects.get_or_create(post=post)
		obj.user.remove(disliking_user)