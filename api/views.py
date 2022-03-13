from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloWorld(APIView):

    def get(self, request: Request):
        return Response({"message": "Hello World!!!"}, status.HTTP_200_OK)
