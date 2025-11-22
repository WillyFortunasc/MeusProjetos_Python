from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='inicial'),
    path('saudacao/<str:nome>/', views.pagina_saudacao, name='saudacao'),
]