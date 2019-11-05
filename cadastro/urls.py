from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'enquete', api.EnqueteViewSet)
router.register(r'resposta', api.RespostaViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Enquete
    path('enquete/', views.EnqueteListView.as_view(), name='cadastro_enquete_list'),
    path('enquete/create/', views.EnqueteCreateView.as_view(), name='cadastro_enquete_create'),
    path('enquete/detail/<int:pk>/', views.EnqueteDetailView.as_view(), name='cadastro_enquete_detail'),
    path('enquete/update/<int:pk>/', views.EnqueteUpdateView.as_view(), name='cadastro_enquete_update'),
)

urlpatterns += (
    # urls for Resposta
    path('resposta/', views.RespostaListView.as_view(), name='cadastro_resposta_list'),
    path('resposta/create/', views.RespostaCreateView.as_view(), name='cadastro_resposta_create'),
    path('resposta/detail/<int:pk>/', views.RespostaDetailView.as_view(), name='cadastro_resposta_detail'),
    path('resposta/update/<int:pk>/', views.RespostaUpdateView.as_view(), name='cadastro_resposta_update'),
)

