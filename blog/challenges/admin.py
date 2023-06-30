from django.contrib import admin
from .models import Challenge

# Register your modelsE here.
class ChallengeAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'created_at')
  search_fields = ['title', 'content']
  prepopulated_fields = {'slug': ('title',)}

admin.site.register(Challenge, ChallengeAdmin)
# admin.site.register(Day)