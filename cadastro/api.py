from . import models
from . import serializers
from rest_framework import viewsets, permissions


class EnqueteViewSet(viewsets.ModelViewSet):
    """ViewSet for the Enquete class"""

    queryset = models.Enquete.objects.all()
    serializer_class = serializers.EnqueteSerializer
    permission_classes = [permissions.IsAuthenticated]


class RespostaViewSet(viewsets.ModelViewSet):
    """ViewSet for the Resposta class"""

    queryset = models.Resposta.objects.all()
    serializer_class = serializers.RespostaSerializer
    permission_classes = [permissions.IsAuthenticated]


