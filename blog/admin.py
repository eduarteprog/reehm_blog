from django.contrib import admin
from .models import Post, Revista

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'section', 'date_published', 'carrusel', 'importante', 'otras')
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Revista)
class RevistaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'imagen', 'archivo_pdf')
