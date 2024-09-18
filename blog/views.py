from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.templatetags.static import static
import os
from django.conf import settings
from django.shortcuts import render
from .models import Revista


def post_list(request):
    posts = Post.objects.filter(date_published__lte=timezone.now()).order_by('date_published')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    # Divide el texto en párrafos
    paragraphs = post.text.split('\n')
    total_paragraphs = len(paragraphs)
    third = total_paragraphs // 3
    
    # Divide los párrafos en tres partes
    part1 = paragraphs[:third]
    part2 = paragraphs[third:2*third]
    part3 = paragraphs[2*third:]
    
    context = {
        'post': post,
        'part1': part1,
        'part2': part2,
        'part3': part3,
    }
    return render(request, 'blog/post_detail.html', context)

def post_principal(request):
    posts = Post.objects.filter(section='principal').order_by('-date_published')
    return render(request, 'blog/post_principal.html', {'posts': posts})

def post_recitales(request):
    posts = Post.objects.filter(section='recitales').order_by('-date_published')
    return render(request, 'blog/post_recitales.html', {'posts': posts})

def post_reseñas(request):
    posts = Post.objects.filter(section='reseñas').order_by('-date_published')
    return render(request, 'blog/post_reseñas.html', {'posts': posts})

def post_que_es_la_reehm(request):
    posts = Post.objects.filter(section='que_es_la_reehm').order_by('-date_published')
    return render(request, 'blog/post_que_es_la_reehm.html', {'posts': posts})

def post_protocolo(request):
    return render(request, 'blog/post_protocolo.html')

def quienes_somos(request):
    return render(request, 'blog/quienes_somos.html')

def post_encuentros(request):
    posts = Post.objects.filter(section='encuentros').order_by('-date_published')
    return render(request, 'blog/post_encuentros.html', {'posts': posts})

def post_agenda(request):
    posts = Post.objects.filter(section='agenda').order_by('-date_published')
    return render(request, 'blog/post_agenda.html', {'posts': posts})

def lista_revistas(request):
    revistas = Revista.objects.all()
    return render(request, 'blog/lista_revistas.html', {'revistas': revistas})

def index(request):
    # Obtener publicaciones que se mostrarán en el carrusel
    carrusel_posts = Post.objects.filter(carrusel=True)
    # Obtener publicaciones importantes
    importante_posts = Post.objects.filter(importante=True)
    # Obtener otras publicaciones
    otras_posts = Post.objects.filter(otras=True)

    context = {
        'carrusel_posts': carrusel_posts,
        'importante_posts': importante_posts,
        'otras_posts': otras_posts,
    }
    return render(request, 'blog/index.html', context)

def publicaciones(request):
    # Obtenemos todas las revistas desde la base de datos
    revistas = Revista.objects.all()
    
    # Renderizamos el template con las revistas
    return render(request, 'blog/publicaciones.html', {'revistas': revistas})