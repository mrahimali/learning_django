from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('science/', views.scienceNews, name='ScienceNews'),
    path('politics/', views.politicsNews, name='home'),
    path('sports/', views.sportsNews, name='home'),
]
