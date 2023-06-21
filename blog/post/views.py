from django.shortcuts import render
from .models import Post

# Create your views here.
def posts(request):
  posts = Post.objects.filter(status=1).order_by('-created_at')
  context = {'posts': posts}
  return render(request, 'post/all_posts.html', context)

def post(request, slug):
  context = {
     'post': Post.objects.get(slug=slug)
  }
  return render(request, 'post/post_content.html', context)