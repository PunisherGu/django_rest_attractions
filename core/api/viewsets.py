from rest_framework import viewsets
from core.models import PontoTuristico
from . import serializers

class PontoTuristicoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PontoTuristico.objects.all()
    serializer_class = serializers.PontoTuristicoSerializer
