from django.shortcuts import render
#Aqui fica as requisições vindas do front isto é, qualquer interação  que o usuário faz no site

def index(request):
    return render(request, 'home.html',{})