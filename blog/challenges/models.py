from django.db import models

# Create your models here.

class Challenge(models.Model):
  title = models.CharField(max_length=200)
  slug = models.SlugField(max_length=200, unique=True)
  description = models.TextField()
  length = models.IntegerField()
  story = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
      ordering = ['-created_at']
  

# class Day(models.Model):
#   status = models.BooleanField(default=False)
#   story = models.TextField(default="incomplete")
#   challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
#   # pic(optional)