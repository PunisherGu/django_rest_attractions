from rest_framework import viewsets
from .serializers import ComentariosSerializer
from comentarios import models

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = models.Comentario.objects.all()
    serializer_class = ComentariosSerializer
