from django.db import models
from django.conf import settings
# Create your models here.

#classes referente a tabela de usuários do site e salas

class Room(models.Model):
    user = models.ForeignKey( #  
        settings.AUTH_USER_MODEL,
        on_delete =models.CASCADE,
    )
    title = models.CharField(max_length=200) #titulo  da sala
    messages = models.ManyToManyField('Message', blank=True) #as mensagens enviadas nessa sala serão armazenadas foi utilado o parâmetro blank para poder criar uma sala vazia sem ser obrigatório ter mensagem
    created_at = models.DateTimeField(auto_now_add=True)  #data em que foi criada a sala

    def __str__(self): #define o nome da sala como o titulo ao invés de ser object(0)
        return self.title

class Message(models.Model): #crio o objeto mensagem
    user = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    on_delete =models.CASCADE,
    )
    text = models.TextField() #texto da mensagem
    created_at = models.DateTimeField(auto_now_add=True) #data do envio da mensagem

    def __str__(self): #funçao para mostrar o nome do usuário e a mensagem q enviou no painel admin da django
        return f"{self.user.username}: {self.text}"
