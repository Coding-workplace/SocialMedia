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