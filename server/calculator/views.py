from django.shortcuts import render


def calc_view(request):
    return render(request, "calc.html")
