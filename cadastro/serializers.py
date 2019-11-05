from . import models

from rest_framework import serializers


class EnqueteSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Enquete
        fields = (
            'pk', 
            'titulo', 
            'pergunta', 
            'data_criacao', 
            'data_publicacao', 
        )


class RespostaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Resposta
        fields = (
            'pk', 
            'resposta', 
            'data_reposta', 
        )


