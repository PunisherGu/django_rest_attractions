from rest_framework.serializers import ModelSerializer
from localizacao import models


class LocalizacaoSerializer(ModelSerializer):

    class Meta:
        model = models.Localizacao
        fields = ('id', 'linha1', 'linha2', 'cidade',
                 'estado', 'pais', 'latitude', 'longitude')
