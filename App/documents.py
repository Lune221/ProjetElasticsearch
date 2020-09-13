from django_elasticsearch_dsl import (
    DocType,
    fields,
    Index,
)

from .models import (
    Film,
    Publication
)
##Movie

films = Index('films')

@films.doc_type
class FilmDocument(DocType):
    class Meta:
        model = Film
        fields = [
            'title',
            'plot',
            'year',
            'type',
        ]

##EndMovie

##Publis

publis = Index('publis')

@publis.doc_type
class PublicationDocument(DocType):
    class Meta:
        model = Publication
        fields = [
            'type',
            'title',
            'booktitle',
            'year',
            'url',
            'authors',
        ]

##EndPublis