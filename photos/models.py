from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return self.name

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    titulo=models.CharField(max_length=150, blank=True)
    description = models.TextField(max_length=300, blank=True)
    # Informações
    info_typegame = models.CharField(max_length=150, blank=True)
    info_datelaunch = models.CharField(max_length=150, blank=True)
    info_designers = models.CharField(max_length=150, blank=True)
    info_developers = models.CharField(max_length=150, blank=True)
    info_publish = models.CharField(max_length=150, blank=True)
    info_genero = models.CharField(max_length=150, blank=True)
    # Requerimentos
    req_processador = models.CharField(max_length=150, blank=True)
    req_memoria = models.CharField(max_length=150, blank=True)
    req_memoriavideo = models.CharField(max_length=150, blank=True)
    req_direct = models.CharField(max_length=150, blank=True)
    req_sistema = models.CharField(max_length=150, blank=True)
    req_volumedisco = models.CharField(max_length=150, blank=True)



    # Botão
    button_mega = models.URLField(max_length=300, blank=True)
    button_media = models.URLField(max_length=300, blank=True)