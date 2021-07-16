from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return self.name

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='static/')
    titulo=models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    # Informações
    info_typegame = models.CharField(max_length=150)
    info_datelaunch = models.CharField(max_length=150)
    info_designers = models.CharField(max_length=150)
    info_developers = models.CharField(max_length=150)
    info_publish = models.CharField(max_length=150)
    info_genero = models.CharField(max_length=150) 
    # Botão
    button_mega = models.URLField(max_length=300)
    button_media = models.URLField(max_length=300)