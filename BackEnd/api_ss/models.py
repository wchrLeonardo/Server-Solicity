from django.db import models

# Create your models here.
class UserService(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=True)
    email = models.EmailField(max_length=70, unique=True)
    senha = models.CharField(max_length=25)
    
    def __str__(self):
        return self.nome
    
    
    