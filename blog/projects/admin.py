from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'created_at')
  search_fields = ['title']
  prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Project, ProjectAdmin)