from django.urls import path

from . import views
# from parent directory import views module

urlpatterns = [
    path("", views.index, name="index"),
]