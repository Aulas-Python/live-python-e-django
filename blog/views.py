from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Post
# Create your views here.

def index(request):

    context = {}
    posts = Post.objects.all()

    context['posts'] = posts

    print(context)

    return render(request, 'index.html', context=context)


@login_required(login_url='/contas/login')
def criar(request):
    context = {}
    return render(request, 'criar.html', context=context)

def editar(request):
    return HttpResponse('Editar')

def deletar(request):

    return HttpResponse('Deletar')

def detalhes(request):
    context = {}
    
    post = {
            'titulo': 'titulo da noticia',
            'conteudo': 'o conteudo da noticia'
        }
    context['post'] = post
    return render(request, 'detalhes.html', context=context)