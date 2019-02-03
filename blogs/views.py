from django.contrib import messages
from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.utils import timezone

from .models import Blog, blogComments

# Create your views here.
def BlogView(request, blogcategories=None):
    # categories=request.GET['blogcategory']
    categories=blogcategories
    eyc = type(categories)
    if categories:
        blog_model=Blog.objects.all().filter(blogCategory=categories).order_by('blogDate')
    else:
        blog_model=Blog.objects.all().order_by('blogDate')

    return render(request, 'blogs.html',{'blog_model':blog_model})

def recentBlogs(request, recentblog=None):
    if recentblog:
        blog_model=Blog.objects.all().filter(id=recentblog).order_by('blogDate')
    else:
        blog_model = Blog.objects.all().order_by('blogDate')
    return render(request, 'blogs.html', {'blog_model': blog_model})

def blogTag(request, blogtag=None):
    if blogtag:
        blog_model=Blog.objects.all().filter(blogTag=blogtag).order_by('blogDate')
    else:
        blog_model = Blog.objects.all().order_by('blogDate')
    return render(request, 'blogs.html', {'blog_model': blog_model})

def BlogDetails(request, blogId=0):
    # blogId = request.GET['blogId']
    _blogId=blogId
    blog_model = Blog.objects.get(id=blogId)
    comments_model = blogComments.objects.filter(blog_id=blogId)
    totalComments=blogComments.objects.filter(blog_id=blogId).count()
    categories=Blog.objects.all().values('blogCategory').distinct()
    some_day_last_week = timezone.now().date() - timedelta(days=7)
    monday_of_last_week = some_day_last_week - timedelta(days=(some_day_last_week.isocalendar()[2] - 1))
    monday_of_this_week = monday_of_last_week + timedelta(days=7)
    recent_posts=Blog.objects.filter(blogDate__gte=monday_of_last_week, blogDate__lt=monday_of_this_week)

    tags_model=Blog.objects.values('blogTag').distinct()
    if request.method=='GET':
        return render(request, 'blogDetails.html',
                      {'blog_model':blog_model,
                       'comments_model':comments_model,
                       'categories':categories,
                       'recent_posts':recent_posts,
                       'tag_model':tags_model,
                       'total_comments':totalComments })
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
        return redirect(BlogDetails, blogId=_blogId)