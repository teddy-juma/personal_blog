from django.urls import path, include, re_path
from django.views.generic import ListView
from home.models import Post
from .views import *

urlpatterns = [path('',DisplayPosts.as_view()),
                path('about/', about),
                path('authors/<int:pk>', Author.as_view()),
                path('postid/<int:pk>', BlogPost.as_view()),
                path('<slug:date>', Archives.as_view())]



#(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-_]+)
