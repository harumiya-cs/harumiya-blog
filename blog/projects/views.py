from django.shortcuts import render
from .models import Project

# Create your views here.
def projects(request):
  projects = Project.objects.all()
  print(projects)

  context = {
     'projects': projects,
  }
  return render(request, 'projects/main.html', context)


def project(request):
    pass