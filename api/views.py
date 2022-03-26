import logging

from django.shortcuts import render

# Create your views here.
from django_filters import rest_framework
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from api.exceptions import CustomValidationError
from api.filter.note_filter import NoteFilters
from api.models import Note
from api.serializer.note_serializer import NoteSerializer

logger = logging.getLogger(__file__)

class HelloWorld(APIView):

    def get(self, request: Request):
        logger.info("Hello world view")
        return Response({"message": "Hello World!!!"}, status.HTTP_200_OK)


class CustomListCreateAPIView(ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request)
        except ValidationError as e:
            raise CustomValidationError(e.detail, e.status_code)


class NoteList(CustomListCreateAPIView):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_class = NoteFilters
