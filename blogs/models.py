from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    blogCategory=models.CharField(max_length=50, null=True)
    blogName=models.CharField(max_length=50, null=True)
    postedBy=models.CharField(max_length=50, null=True)
    blogDate=models.DateField(null=True, max_length=300)
    blogAbout=models.CharField(max_length=150, null=True)
    blogDescription=models.CharField(max_length=500, null=True)
    blogQuote=models.CharField(max_length=300, null=True)
    blogTag=models.CharField(max_length=100, null=True)
    photo=models.ImageField(upload_to='static/assets/blogImages', default='static/assets/blogImages/blog1.jpg')

class blogComments(models.Model):
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    senderName=models.CharField(max_length=50)
    date=models.DateTimeField(null=True)
    comment=models.CharField(max_length=200)
    photo = models.ImageField(upload_to='static/assets/blogCommentsImages', default='static/assets/blogCommentsImages/comment-icon.png')