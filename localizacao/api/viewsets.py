from rest_framework import viewsets
from .serializers import LocalizacaoSerializer
from localizacao import models

class LocalizacaoViewSet(viewsets.ModelViewSet):
    queryset = models.Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer
