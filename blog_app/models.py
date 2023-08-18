from django.db import models
import datetime
from django.contrib.auth.models import User



# Create your models here.
CATEGORY_CHOICES=(
    
    ('Fashion','Fashion&styles'),
    ('Business','Business'),
    ('Social','Social'),
    ('Travel','Travel'),
    ('Food','Food'),
    ('Culture','Culture'),
    ('Nature','Nature'),
)

class Bloglist(models.Model):
    Blog_id=models.AutoField(primary_key=True)
    Author_name=models.CharField(max_length=200)
    Publish_date=models.DateTimeField()
    Blog_category=models.CharField(choices=CATEGORY_CHOICES,max_length=200 ,default='SO')
    Blog_title=models.CharField(max_length=400)
    Blog_caption=models.CharField(max_length=500)
    
    Blog_image=models.ImageField(upload_to="blogs",null=True,blank=True)
    likes=models.ManyToManyField(User,related_name="like_blog",blank=True)
    def total_likes(self):
        return self.likes.count()

#comment    
class Comment(models.Model):
    blog=models.ForeignKey('Bloglist',on_delete=models.CASCADE)
    authorname=models.CharField(max_length=200)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"comment by {self.authorname} on {self.blog.Blog_title}"   

