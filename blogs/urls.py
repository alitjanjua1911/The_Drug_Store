from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
    path('', views.BlogView, name='blog'),
    # path('blogs/<str:blogcategories>/<int:recentpost>/<str:blogtag>', views.BlogView),
    # url(r'^blogs/blogdetails/(?P<blogcategories>\w+)/(?P<recentpost>\w+)/(?P<blogtag>[\w-]+)/$', views.BlogView, name='blogview'),
    path('blogdetails/<int:blogId>', views.BlogDetails, name='blogdetails')
]