from rest_framework.serializers import ModelSerializer
from atracoes import models


class AtracaoSerializer(ModelSerializer):

    class Meta:
        model = models.Atracao
        fields = ('id', 'nome', 'descricao', 'horario_func', 'idade_min', 'foto')
