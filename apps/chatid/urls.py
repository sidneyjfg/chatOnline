from django.urls import path
#configuração de caminhos para as views do app
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]