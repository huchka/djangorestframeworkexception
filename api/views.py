from django.shortcuts import render

# Create your views here.
from django_filters import rest_framework
from rest_framework import status, filters
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from api.filter.note_filter import NoteFilters
from api.models import Note
from api.serializer.note_serializer import NoteSerializer


class HelloWorld(APIView):

    def get(self, request: Request):
        return Response({"message": "Hello World!!!"}, status.HTTP_200_OK)


class NoteList(ListAPIView):

    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_class = NoteFilters
