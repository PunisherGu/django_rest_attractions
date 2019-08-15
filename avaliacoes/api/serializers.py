from rest_framework.serializers import ModelSerializer
from avaliacoes import models


class AvaliacoesSerializer(ModelSerializer):

    class Meta:
        model = models.Avaliacao
        fields = ('id','usuario','comentario','nota','data')
