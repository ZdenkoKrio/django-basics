from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello World!")


def home2(request):
    return render(request, "home2.html")


def home_d(request, number):

    return HttpResponse(f"Hello World! {number}")


def home2_d(request, number):
    return render(request, "home2.html", {"number":number})