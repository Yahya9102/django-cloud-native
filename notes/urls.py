from django.urls import path
from .views import create_note

urlpatterns = [
    path("notes/", create_note),
]