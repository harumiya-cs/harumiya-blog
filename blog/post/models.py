from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    CATEGORIES = [
        ('Life', 'Life'),
        ('Tech', 'Technical'),
        ('Challenge', 'Challenge'),
    ]
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORIES, default='Life')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    word_count = models.IntegerField(blank=True)
