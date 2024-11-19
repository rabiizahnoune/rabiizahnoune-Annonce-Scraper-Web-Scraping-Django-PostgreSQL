from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('start-scraping/', views.start_scraping, name='start_scraping'),
]