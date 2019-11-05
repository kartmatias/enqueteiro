from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Enquete(models.Model):

    # Fields
    titulo = models.CharField(max_length=300, null=False, blank=False)
    pergunta = models. TextField(blank=False, null=False)
    data_criacao = models.DateTimeField(default=timezone.now)
    data_publicacao = models.DateTimeField(blank=True, null=True)

    # Relationship Fields
    autor = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE, related_name="enquetes"    
        )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('cadastro_enquete_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('cadastro_enquete_update', args=(self.pk,))


class Resposta(models.Model):

    # Fields
    resposta = models.CharField(max_length=300)
    data_reposta = models.DateTimeField(default=timezone.now)

    # Relationship Fields
    enquete = models.ForeignKey(
        'cadastro.Enquete',
        on_delete=models.CASCADE, related_name="respostas"
        )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('cadastro_resposta_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('cadastro_resposta_update', args=(self.pk,))


