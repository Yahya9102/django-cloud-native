from django.urls import path
from .views import create_category

urlpatterns = [
    path("categories/", create_category),
]