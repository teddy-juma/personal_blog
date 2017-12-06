from django.shortcuts import render
from django.utils import timezone
from .models import Post, Authors
from django.views.generic import TemplateView, ListView

# Create your views here.

class BlogPost(ListView):
    template_name = 'home/home.html'
    queryset=Post.objects.all().order_by("-date")[:25]

class Author(TemplateView):
    
    template_name = 'home/authors_posts.html'
    #queryset= Post.objects.all().filter(year)

    def get_context_data(self, **kwargs):
        author = self.kwargs['pk']

        context = super(Author, self).get_context_data(**kwargs)
        context['author'] = Authors.objects.all().filter(pk=author)
        context['posts'] = Post.objects.all().filter(author=author)

        return context


    
    
def about(request):

    return render(request, template_name='home/about.html')


