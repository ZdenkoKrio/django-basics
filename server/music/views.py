from django.shortcuts import render
from .models import Band


def band_list_view(request):
    result = Band.objects.all().values()

    return render(request, "band_list.html", {"bands": result})


def band_detail_view(request, id):
    result = Band.objects.get(id=id)

    return render(request, "band_detail.html", {"band": result})
