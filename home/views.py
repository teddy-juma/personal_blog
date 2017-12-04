from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def about(request):

    return render(request, template_name='home/about.html')


