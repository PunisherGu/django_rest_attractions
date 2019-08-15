from rest_framework.serializers import ModelSerializer
from comentarios import models


class ComentariosSerializer(ModelSerializer):

    class Meta:
        model = models.Comentario
        fields = ('id', 'usuario', 'comentario', 'data', 'aprovado')
