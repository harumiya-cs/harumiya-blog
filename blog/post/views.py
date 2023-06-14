from django.shortcuts import render
from .models import Post

# Create your views here.
def blogs(request):
  blogs = Post.objects.filter(status=1).order_by('-created_at')
  context = {'blogs': blogs}
  return render(request, 'post/blogs.html', context)

def blog(request, slug):
  context = {
     'blog': Post.objects.get(slug=slug)
  }
  return render(request, 'post/blog.html', context)