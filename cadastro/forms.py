from django import forms
from .models import Enquete, Resposta


class EnqueteForm(forms.ModelForm):
    class Meta:
        model = Enquete
        fields = ['titulo', 'pergunta', 'data_criacao', 'data_publicacao', 'autor']


class RespostaForm(forms.ModelForm):
    class Meta:
        model = Resposta
        fields = ['resposta', 'data_reposta', 'enquete']


