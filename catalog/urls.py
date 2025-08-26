from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="catalog_index"),  # <- WICHTIG: Name ist catalog_index
]
