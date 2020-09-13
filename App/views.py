from django.shortcuts import render, HttpResponse
from .models import Film, Publication
from rest_framework import viewsets
from .serializers import FilmSerializer
from .documents import FilmDocument, PublicationDocument
import json
from time import time
# Create your views here.

class FilmView(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


def filmSearch(request):
    q = request.GET.get('q')

    if q:
        movies = FilmDocument.search().query("match", title=q)
    else:
        movies = ""

    return render(request, "App/resultm.html", {"movies" : movies})

def publisSearch(request):
    q = request.GET.get('q')
    nb = 0
    t = 0
    print("Trying to connect ...#########")
    if q:
        t0 = time()
        publis = Publication.objects.filter(title__icontains=q)
        
        #publis = PublicationDocument.search().query("match", title=q)
        nb = publis.count()
        t = time() - t0
    else:
        publis = ""
    print("We are OK ...#########")
    return render(request, "App/resultp.html", {"publis" : publis, "nombre" : nb, "time" : t})


def queryPublisFomJson(request):

    with open("C:/Users/ASUS/OneDrive/Bureau/Projet BD NoSQL/ElasticProject/ElasticProject/App/dblp.json", encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
        for pub in data:
            publis = Publication()
            
            publis.type = pub["type"]
            publis.title = pub["title"]

            publis.year = int(pub["year"])

            try:
                publis.booktitle = pub["booktitle"]
            except KeyError:
                publis.booktitle = "None"

            try:
                publis.url = pub["url"]
            except KeyError:
                publis.url = "None"
            
            publis.authors = ""
            for auth in pub["authors"]:
                publis.authors = publis.authors + auth
                publis.authors = publis.authors + ", "

            publis.save()
    return HttpResponse("Tout est OKKKKKKKKKKKKKKKKKKKK!")