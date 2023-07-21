from django.db import models
import datetime
from django.contrib.auth.models import User



# Create your models here.
class Bloglist(models.Model):
    Blog_id=models.AutoField(primary_key=True)
    Author_name=models.CharField(max_length=200)
    Publish_date=models.DateTimeField()
    Blog_category=models.CharField(max_length=300,null=True,blank=True)
    Blog_title=models.CharField(max_length=400)
    Blog_caption=models.CharField(max_length=500)
    
    Blog_image=models.ImageField(upload_to="blogs",null=True,blank=True)
    likes=models.ManyToManyField(User,related_name="like_blog",blank=True)
    def total_likes(self):
        return self.likes.count()

