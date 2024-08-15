# Reehm

## Instalación

### Windows

Instalar Docker Desktop de https://docs.docker.com/desktop/install/windows-install/

### Linux

Instalar Docker [https://docs.docker.com/engine/install/ubuntu/] y docker-compose [https://github.com/docker/compose]

### Configuración

Crear en el root del proyecto el archivo .env con el siguiente contenido:

```
DEBUG=True
```

### Ejecutar aplicación

Para ejecutar la aplicación con su db deben ejecutar el comando `docker-compose up -d` desde una consola linux o desde la consola de VS. Con este ultimo, tiene herramientas para ejecutar las imagenes docker, pero no tengo ni idea cómo se usan.

## Comandos útiles

1. Levantar docker: `docker-compose up -d`
1. Bajar docker: `docker-compose stop`
1. Compilar docker: `docker-compose build web`
1. Acceder a la imagen: `docker-compose exec web bash`
1. Correr migraciones: `docker-compose up migrate`
1. Correr shell django: `docker-compose exec web ./manage.py shell_plus`
