from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Viaje
from .serializers import ViajeSerializer

# Create your views here.

@csrf_exempt
@api_view(['GET'])
def lista_viajes(request):
    viajes = Viaje.objects.all()
    serializer = ViajeSerializer(viajes, many=True)
    return Response (serializer.data)
