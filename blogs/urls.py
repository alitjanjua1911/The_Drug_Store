from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
    path('', views.BlogView, name='blog'),
    path('categories/<str:blogcategories>', views.BlogView, name='blogcategories'),
    path('recentblogs/<int:recentblog>', views.recentBlogs, name='recentBlogs'),
    path('tag/<str:blogtag>', views.blogTag, name='blogTag'),
    # url(r'^blogs/blogdetails/(?P<blogcategories>\w+)/(?P<recentpost>\w+)/(?P<blogtag>[\w-]+)/$', views.BlogView, name='blogview'),
    path('blogdetails/<int:blogId>', views.BlogDetails, name='blogdetails')
]