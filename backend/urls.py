from django.urls import path
from backend import views

urlpatterns = [
    path('get-five-recipe', views.get_five_recipe),
    path('meal-planning', views.post_meal_planning),
    path('web-scraping', views.web_scraping),
]