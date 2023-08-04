from django.urls import path
from . import views

urlpatterns = [
  path('', views.projects, name="projects"),
  path('<str:slug>/', views.project, name="project"),
]