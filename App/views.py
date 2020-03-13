from django.shortcuts import render
from .models import Film
from rest_framework import viewsets
from .serializers import FilmSerializer
from .documents import FilmDocument

# Create your views here.

class FilmView(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


def search(request):
    q = request.GET.get('q')
    if q:
        movies = FilmDocument.search().query("match", title=q)
    else:
        movies = ""

    return render(request, "App/result.html", {"movies" : movies})