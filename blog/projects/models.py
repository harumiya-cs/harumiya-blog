from django.db import models

# Create your models here.
class Project(models.Model):
  title = models.CharField(max_length=200)
  slug = models.SlugField(max_length=200, unique=True)
  description = models.CharField(max_length=5000, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  word_count = models.IntegerField(blank=True, null=True)
  project_pic = models.ImageField(upload_to="images/")
  project_live_link = models.CharField(max_length=300, blank=True, null=True)
  project_source_link = models.CharField(max_length=300)

  class Meta:
      ordering = ['-created_at']

  def __str__(self):
      return self.title