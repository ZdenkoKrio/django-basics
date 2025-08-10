from django.shortcuts import render, redirect
from .models import Band, Album, Song


def band_list_view(request):
    result = Band.objects.all().values()
    print(f"BANDS: {result}")
    return render(request, "band_list.html", {"bands": result})


def band_detail_view(request, id):
    result = Band.objects.get(id=id)
    print(f"BAND: {result}")
    albums = Album.objects.filter(band=result)
    print(f"ALbums: {albums}")
    return render(request, "band_detail.html",
                  {"band": result,
                   "albums": albums})


def band_create_view(request):
    name = request.GET.get("name")
    year = request.GET.get("year")
    genre = request.GET.get("genre")

    if ((name is not None and year is not None) and
            (name is not "" and year is not "")):
        new_band = Band(name=name, year=year, genre=genre)
        new_band.save()
        return redirect("bands")

    return render(request, "band_create.html")


def album_detail_view(request, id):
    result = Album.objects.get(id=id)
    songs = Song.objects.filter(album=result)
    return render(request, "album_detail.html",
                  {"album": result,
                   "songs": songs})


def song_detail_view(request, id):
    result = Song.objects.get(id=id)
    return render(request, "song_detail.html",
                  {"song": result})