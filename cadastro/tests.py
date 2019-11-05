import unittest
from django.urls import reverse
from django.test import Client
from .models import Enquete, Resposta
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_enquete(**kwargs):
    defaults = {}
    defaults["titulo"] = "titulo"
    defaults["pergunta"] = "pergunta"
    defaults["data_criacao"] = "data_criacao"
    defaults["data_publicacao"] = "data_publicacao"
    defaults.update(**kwargs)
    if "autor" not in defaults:
        defaults["autor"] = create_'auth_user'()
    return Enquete.objects.create(**defaults)


def create_resposta(**kwargs):
    defaults = {}
    defaults["resposta"] = "resposta"
    defaults["data_reposta"] = "data_reposta"
    defaults.update(**kwargs)
    if "enquete" not in defaults:
        defaults["enquete"] = create_enquete()
    return Resposta.objects.create(**defaults)


class EnqueteViewTest(unittest.TestCase):
    '''
    Tests for Enquete
    '''
    def setUp(self):
        self.client = Client()

    def test_list_enquete(self):
        url = reverse('cadastro_enquete_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_enquete(self):
        url = reverse('cadastro_enquete_create')
        data = {
            "titulo": "titulo",
            "pergunta": "pergunta",
            "data_criacao": "data_criacao",
            "data_publicacao": "data_publicacao",
            "autor": create_'auth_user'().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_enquete(self):
        enquete = create_enquete()
        url = reverse('cadastro_enquete_detail', args=[enquete.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_enquete(self):
        enquete = create_enquete()
        data = {
            "titulo": "titulo",
            "pergunta": "pergunta",
            "data_criacao": "data_criacao",
            "data_publicacao": "data_publicacao",
            "autor": create_'auth_user'().pk,
        }
        url = reverse('cadastro_enquete_update', args=[enquete.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class RespostaViewTest(unittest.TestCase):
    '''
    Tests for Resposta
    '''
    def setUp(self):
        self.client = Client()

    def test_list_resposta(self):
        url = reverse('cadastro_resposta_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_resposta(self):
        url = reverse('cadastro_resposta_create')
        data = {
            "resposta": "resposta",
            "data_reposta": "data_reposta",
            "enquete": create_enquete().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_resposta(self):
        resposta = create_resposta()
        url = reverse('cadastro_resposta_detail', args=[resposta.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_resposta(self):
        resposta = create_resposta()
        data = {
            "resposta": "resposta",
            "data_reposta": "data_reposta",
            "enquete": create_enquete().pk,
        }
        url = reverse('cadastro_resposta_update', args=[resposta.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


