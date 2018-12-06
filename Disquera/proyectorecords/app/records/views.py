from django.shortcuts import render

from app.records.models import Cancion

# Create your views here.

def songs(request):
    all_songs= Cancion.objects.all()
    context= {'object_list': all_songs}
    return render(request, 'disquera/allsongs.html', context)


def detail_songs(request, id_song):
    song= Cancion.objects.get(id=id_song)
    context= {'object': song}
    return render(request, 'disquera/detailsongs.html', context)
