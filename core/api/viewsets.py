from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from core.models import PontoTuristico
from . import serializers

class PontoTuristicoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = serializers.PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.all()

    def list(self, request, *args, **kwargs):
        return  Response({'teste': 123})

    def create(self, request, *args, **kwargs):
        return  Response({'Hello': request.data['nome']})

    def destroy(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, *args, **kwargs):#dispara no get mas em um unico recurso
        pass

    def partial_update(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        pass
