from django.contrib import messages
from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.urls import reverse
from django.utils import timezone
from django.views.generic import TemplateView
from .forms import commentsForm

from .models import Blog, blogComments

# Create your views here.
def BlogView(request, blogcategories="", recentpost=-1, blogtag=""):
    # categories=request.GET['blogcategory']
    categories=blogcategories
    if categories != "":
        blog_model=Blog.objects.all().filter(blogCategory=categories).order_by('blogDate')
    elif recentpost!=-1:
        blog_model=Blog.objects.all().filter(id=recentpost)
    elif blogtag!="":
        blog_model=Blog.objects.all().filter(blogTag=blogtag)
    else:
        blog_model=Blog.objects.all().order_by('blogDate')
    return render(request, 'blogs.html',{'blog_model':blog_model})

def BlogDetails(request, blogId=0):
    # blogId = request.GET['blogId']
    _blogId=blogId
    blog_model = Blog.objects.get(id=blogId)
    comments_model = blogComments.objects.filter(blog_id=blogId)
    categories=Blog.objects.all().values('blogCategory')
    # recent_posts=Blog.objects.filter(blogDate_lte=datetime.today(), blogDate_gt=datetime.today()-datetime.timedelta(days=5))
    some_day_last_week = timezone.now().date() - timedelta(days=7)
    monday_of_last_week = some_day_last_week - timedelta(days=(some_day_last_week.isocalendar()[2] - 1))
    monday_of_this_week = monday_of_last_week + timedelta(days=7)
    recent_posts=Blog.objects.filter(blogDate__gte=monday_of_last_week, blogDate__lt=monday_of_this_week)
    monday_of_last_week = some_day_last_week - timedelta(days=(some_day_last_week.isocalendar()[2] - 1))

    tags_model=Blog.objects.values('blogTag').distinct()
    if request.method=='GET':
        return render(request, 'blogDetails.html', {'blog_model':blog_model, 'comments_model':comments_model, 'categories':categories, 'recent_posts':recent_posts, 'tag_model':tags_model })
    else:
        if request.POST.get('name') and request.POST.get('comment'):
            commets = blogComments()
            commets.senderName = request.POST.get('name')
            commets.comment = request.POST.get('comment')
            commets.blog_id = blogId
            commets.date = datetime.now()
            commets.user_id = request.user.id
            commets.photo = '../../static/assets/blogCommentsImages/comment-icon.png'
            commets.save()
            messages.success(request, 'Your comment is successfully sent')
        else:
            messages.success(request, 'Your comment is not sent')
        # return redirect('BlogDetails', blogId=_blogId)
        return redirect(BlogDetails, blogId=_blogId)