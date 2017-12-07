from django.shortcuts import render
from django.utils import timezone
from .models import Post, Authors
from django.views.generic import TemplateView

# Create your views here.

class BlogPost(TemplateView):
    template_name = 'home/home.html'
    
    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super(BlogPost, self).get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=pk)

        return context

class Author(TemplateView):
    
    template_name = 'home/authors_posts.html'
    #queryset= Post.objects.all().filter(year)

    def get_context_data(self, **kwargs):
        author = self.kwargs['pk']

        context = super(Author, self).get_context_data(**kwargs)
        context['author'] = Authors.objects.all().filter(pk=author)
        context['post'] = Post.objects.all().filter(author=author)

        return context

class DisplayPosts(TemplateView):
    template_name = 'home/blog_post.html'

    def get_context_data(self, **kwargs):
        context = super(DisplayPosts, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-date')

        return context
    
class Archives(TemplateView):
    template_name = 'home/archives.html'
   
    def get_context_data(self, **kwargs):
        year = self.kwargs['date']
        context = super(Archives, self).get_context_data(**kwargs)
        context['group_post'] = Post.objects.all().filter(date=year)

        return context

def about(request):

    return render(request, template_name='home/about.html')


