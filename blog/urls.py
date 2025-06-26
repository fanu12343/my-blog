from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('sports/', views.sports, name='sports'),
    path('travel/', views.travel, name='travel'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact_view, name='contact'),
 ]

