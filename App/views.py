from django.shortcuts import render, HttpResponse
from .models import Film, Publication
from rest_framework import viewsets
from .serializers import FilmSerializer
from .documents import FilmDocument, PublicationDocument
import json
from time import time
# Create your views here.

#For REST FRAMEWORK
class FilmView(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

#For web SOckets


def filmSearch(request):
    q = request.GET.get('q')

    if q:
        movies = FilmDocument.search().query("match", title=q)
    else:
        movies = ""

    return render(request, "App/resultf.html", {"movies" : movies})


def publisSearch(request):
    q = request.GET.get('q')
    nb = 0
    t = 0
    print("Trying to connect ...#########")
    if q:
        t0 = time()
        #print("Using MySQL and DJango for the search...###")
        #publis = Publication.objects.filter(title__icontains=q)

        print("Using ES and DJango for the search...###")
        publis = PublicationDocument.search().query("match", title=q)
        nb = publis.count()
        t = time() - t0
    else:
        publis = ""
        q = ""
    print("We are OK ...#########")
    return render(request, "App/resultp.html", {"publis" : publis, "nombre" : nb, "time" : t, "q" : q})

def publisAutcompletion(value):#To make autocompletion while rechearching publications
    tab_pub = []
    if value:
        publis = PublicationDocument.search().query("match", title=value)
        nb = publis.count() #The number of  found publications
        #response = publis.execute()
        i = 0
        for pub in  publis:
            tab_pub.append(pub.title)
            i+=1
            if i == 3:
                break
    print(tab_pub)
    return tab_pub


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