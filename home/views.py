from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.


def home(request):
    post = Post.objects.filter(date=timezone.now()).order_by('date')

    return render(request,"home/home.html",{'post':post})