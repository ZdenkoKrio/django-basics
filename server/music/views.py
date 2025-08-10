from django.shortcuts import render, redirect
from .models import Band


def band_list_view(request):
    result = Band.objects.all().values()

    return render(request, "band_list.html", {"bands": result})


def band_detail_view(request, id):
    result = Band.objects.get(id=id)

    return render(request, "band_detail.html", {"band": result})


def band_create_view(request):
    name = request.GET.get("name")
    year = request.GET.get("year")

    if ((name is not None and year is not None) and
            (name is not "" and year is not "")):
        new_band = Band(name=name, year=year)
        new_band.save()
        return redirect("bands")

    return render(request, "band_create.html")
