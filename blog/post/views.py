from django.shortcuts import render
from .models import Post

# Create your views here.
def blogs(request):
  blogs = Post.objects.all()
  context = {'blogs': blogs}
  return render(request, 'post/blogs.html', context)

def blog(request, slug):
  context = {
     'blog': Post.objects.get(slug=slug)
  }
  return render(request, 'post/blog.html', context)