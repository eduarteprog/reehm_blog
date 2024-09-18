from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.files.storage import default_storage

class Post(models.Model):
    SECTIONS = [
        ('que_es_la_reehm', '¿Qué es la Reehm?'),
        ('protocolo', 'Protocolo'),
        ('encuentros', 'Encuentros'),
        ('reseñas', 'Reseñas'),
        ('agenda', 'Agenda'),
    ]

    title = models.CharField(max_length=200, verbose_name='Título')
    text = models.TextField(verbose_name='Texto')
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Imagen Principal')
    image_2 = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Imagen Secundaria 1')
    image_3 = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Imagen Secundaria 2')
    image_4 = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Imagen Secundaria 3')
    author = models.CharField(max_length=200, verbose_name='Autor')
    section = models.CharField(max_length=50, choices=SECTIONS, default='principal', verbose_name='Sección')
    slug = models.SlugField(unique=True, blank=True, max_length=200, verbose_name='Slug (puedes dejarlo en blanco y se genera sólo)')
    date_published = models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Publicación')
    carrusel = models.BooleanField(default=False, verbose_name='Principal en Carrusel')
    importante = models.BooleanField(default=False, verbose_name='Principal en Importante')
    otras = models.BooleanField(default=False, verbose_name='Principal en Otras')

    def publish(self):
        self.date_published = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        if not self.pk:
            if not self.author:
                self.author = User.objects.filter(username='Reem').first()  
                if not self.author:
                    # Crea el usuario si no existe
                    self.author = User.objects.create_user(username='Reehm', password='defaultpassword')
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Elimina los archivos de imagen antes de eliminar la instancia
        if self.image and default_storage.exists(self.image.path):
            default_storage.delete(self.image.path)
        if self.image_2 and default_storage.exists(self.image_2.path):
            default_storage.delete(self.image_2.path)
        if self.image_3 and default_storage.exists(self.image_3.path):
            default_storage.delete(self.image_3.path)
        if self.image_4 and default_storage.exists(self.image_4.path):
            default_storage.delete(self.image_4.path)
        
        super().delete(*args, **kwargs)

    def _str_(self):
        return self.title

class Revista(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Título')
    imagen = models.ImageField(upload_to='revistas/imagenes/', verbose_name='Imagen de la Revista')
    archivo_pdf = models.FileField(upload_to='revistas/pdfs/', verbose_name='Archivo PDF')

    def __str__(self):
        return self.titulo
