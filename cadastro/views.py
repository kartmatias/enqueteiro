from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Enquete, Resposta
from .forms import EnqueteForm, RespostaForm


class EnqueteListView(ListView):
    model = Enquete


class EnqueteCreateView(CreateView):
    model = Enquete
    form_class = EnqueteForm


class EnqueteDetailView(DetailView):
    model = Enquete


class EnqueteUpdateView(UpdateView):
    model = Enquete
    form_class = EnqueteForm


class RespostaListView(ListView):
    model = Resposta


class RespostaCreateView(CreateView):
    model = Resposta
    form_class = RespostaForm


class RespostaDetailView(DetailView):
    model = Resposta


class RespostaUpdateView(UpdateView):
    model = Resposta
    form_class = RespostaForm

