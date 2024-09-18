from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name='index'),
    path('revistas/', views.lista_revistas, name='lista_revistas'),
    path('posts/lista/', views.post_list, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('posts/principal/', views.post_principal, name='post_principal'),
    path('posts/recitales/', views.post_recitales, name='post_recitales'),
    path('posts/reseñas/', views.post_reseñas, name='post_reseñas'),
    path('posts/que_es_la_reehm/', views.post_que_es_la_reehm, name='post_que_es_la_reehm'),
    path('posts/protocolo/', views.post_protocolo, name='protocolo'),
    path('posts/encuentros/', views.post_encuentros, name='post_encuentros'),
    path('posts/agenda/', views.post_agenda, name='post_agenda'),
    path('posts/publicaciones/', views.publicaciones, name='publicaciones'),
    path('posts/quienes_somos/', views.quienes_somos, name='quienes_somos'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)