from django.shortcuts import render
from .models import Challenge


# Create your views here.
def main(request):
  challenges = Challenge.objects.all()
  context = {'challenges': challenges}
  return render(request, 'challenges/main.html', context)


def challenge(request, slug):
  context = {
    'challenge': Challenge.objects.get(slug=slug),
  }
  return render(request, 'challenges/challenge.html', context)