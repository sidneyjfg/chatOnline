### Chat Online em Python Django e JavaScript
Este é um projeto de chat online desenvolvido utilizando Python Django para o backend e JavaScript para o frontend. Este README fornecerá informações sobre como configurar e executar o projeto localmente, juntamente com algumas notas sobre o que foi aprendido durante o desenvolvimento.

## Tecnologias Utilizadas
```
Python 3.x
Django 3.x
JavaScript
HTML
CSS
Funcionalidades
Envio e recebimento de mensagens em tempo real.
Interface de usuário simples e intuitiva.
```

## Pré-requisitos
Python 3 instalado em seu sistema.
pip (gerenciador de pacotes do Python) instalado.
Instalação e Execução Local
Clone o repositório:

```
git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto
```
Crie um ambiente virtual (opcional, mas altamente recomendado):


```
python3 -m venv venv
```
Ative o ambiente virtual:

No Windows:

```
venv\Scripts\activate
```
No macOS e Linux:

```
source venv/bin/activate
```
Instale as dependências do Python:
```
pip install -r requirements.txt
```
Execute as migrações do Django:


```
python manage.py migrate
```

Inicie o servidor de desenvolvimento:


```
python manage.py runserver
```

Acesse o aplicativo:

Abra o navegador e acesse http://localhost:8000 para visualizar o chat online.

## Aprendizados
Durante o desenvolvimento deste projeto, aprendi:

Como configurar um projeto Django básico.
Integração do Django com JavaScript para comunicação em tempo real.
Conceitos de WebSockets e uso de bibliotecas como Django Channels para comunicação bidirecional.
Práticas de desenvolvimento frontend para criar uma interface de usuário responsiva e intuitiva.
