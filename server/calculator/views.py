from django.db.models.expressions import result
from django.shortcuts import render
from django.http import HttpResponse


def calc_view(request):
    num1 = request.GET.get("num1")
    num2 = request.GET.get("num2")

    result = None
    if num1 is not None and num2 is not None:
        result = int(num1) + int(num2)

    return render(request, "calc.html", {"result": result})


def showcase_plus(request, num1, num2):
    return HttpResponse(f"Vysledok: {num2+num1}")