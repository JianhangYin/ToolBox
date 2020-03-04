from django.urls import path
from backend import views

urlpatterns = [
    path('meal-planning', views.post_meal_planning),
    path('web-scraping', views.web_scraping),
]