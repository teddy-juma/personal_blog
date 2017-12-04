from django.urls import path, include
from django.views.generic import ListView
from home.models import Post
from . import views

urlpatterns = [path('',ListView.as_view(
                                    queryset=Post.objects.all().order_by("-date")[:25],
                                    template_name="home/home.html")),
                                    
                path('about/', views.about)]