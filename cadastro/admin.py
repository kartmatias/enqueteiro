from django.contrib import admin
from django import forms
from .models import Enquete, Resposta

class EnqueteAdminForm(forms.ModelForm):

    class Meta:
        model = Enquete
        fields = '__all__'


class EnqueteAdmin(admin.ModelAdmin):
    form = EnqueteAdminForm
    list_display = ['titulo', 'pergunta', 'data_criacao', 'data_publicacao']
    readonly_fields = ['titulo', 'pergunta', 'data_criacao', 'data_publicacao']

admin.site.register(Enquete, EnqueteAdmin)


class RespostaAdminForm(forms.ModelForm):

    class Meta:
        model = Resposta
        fields = '__all__'


class RespostaAdmin(admin.ModelAdmin):
    form = RespostaAdminForm
    list_display = ['resposta', 'data_reposta']
    readonly_fields = ['resposta', 'data_reposta']

admin.site.register(Resposta, RespostaAdmin)


