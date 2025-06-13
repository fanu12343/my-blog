from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("projects/", views.projects_page, name="projects"),
    path("sports/", views.sports_page, name="sports"),
    path("skills/", views.travel_page, name="travel"),
]
