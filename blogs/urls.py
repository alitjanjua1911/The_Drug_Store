from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
    path('', views.BlogView, name='blog'),
    # url(r'(?P<blogcategories>\w+)/(?P<recentblog>\d+)/(P<blogtag>\w+)/$', views.BlogView, name='blogV'),
    # path('<str:blogcategories>/<int:recentblog>/<str:blogtag>', views.BlogView, name='blogV'),
    path('categories/<str:blogcategories>', views.BlogView, name='blogcategories'),
    path('recentblogs/<int:recentblog>', views.BlogView, name='recentBlogs'),
    path('tag/<str:blogtag>', views.BlogView, name='blogTag'),
    # url(r'^blogs/blogdetails/(?P<blogcategories>\w+)/(?P<recentpost>\w+)/(?P<blogtag>[\w-]+)/$', views.BlogView, name='blogview'),
    path('blogdetails/<int:blogId>', views.BlogDetails, name='blogdetails')
]