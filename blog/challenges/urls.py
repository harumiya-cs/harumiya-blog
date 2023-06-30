from django.urls import path
from . import views
urlpatterns = [
  path('', views.main, name='challenges'),
  path('<str:slug>', views.challenge, name='challenge'),

]