from django.urls import path
from rest_api.views import lista_viajes

urlpatterns=[
    path('lista_viajes', lista_viajes, name="Lista Viajes"),
]
