from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="catalog_index"),  # wichtig für die Tests
]
