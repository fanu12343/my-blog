from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def starting_page(request):
    return render(request,"blog/index.html")

def projects_page(request):
    return render(request,"blog/project.html")


def sports_page(request):
    return render(request,"blog/sports.html")

def travel_page(request):
    return render(request,"blog/travel.html")