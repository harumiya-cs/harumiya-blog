from django.db import models

# Create your models here.

class Post(models.Model):
  STATUS = [
    (0, 'Draft'),
    (1, 'Publish')
  ]

  CATEGORIES = [
      ('Life', 'Life'),
      ('Tech', 'Technical'),
      ('Challenge', 'Challenge'),
  ]
  title = models.CharField(max_length=200)
  slug = models.SlugField(max_length=200, unique=True)
  category = models.CharField(max_length=50, choices=CATEGORIES, default='Life')
  status = models.IntegerField(choices=STATUS, default=0)
  description = models.CharField(max_length=2000, blank=True, null=True)
  content = models.TextField()
  # blog_img = models.ImageField(upload_to= '', default='')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['-created_at']

  def __str__(self):
    return self.title
  
  def word_count(self):
    return len(self.content.split())