from rest_framework.viewsets import ModelViewSet
from avaliacoes import models
from .serializers import AvaliacoesSerializer


class AvaliacaoViewSet(ModelViewSet):
    queryset = models.Avaliacao.objects.all()
    serializer_class = AvaliacoesSerializer
