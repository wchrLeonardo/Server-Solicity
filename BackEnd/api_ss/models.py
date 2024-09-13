from django.db import models

class Base(models.Model):
    criacao= models.DateTimeField(auto_now_add=True)
    atualizacao= models.DateTimeField(auto_now=True)
    ativo= models.BooleanField(default=True)

    class Meta: 
        abstract = True

class Empresa(Base):
    nome_empresa= models.CharField(max_length=50)
    cnpj_empresa= models.CharField(max_length=25)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
    
    def __str__(self):
        return self.nome_empresa
    
class Servico(Base):
    empresa = models.ForeignKey(Empresa, related_name='servicos', on_delete=models.CASCADE)
    nome_servico= models.CharField(max_length=100)
    tipo_servico= models.CharField(max_length=50)
    codigo_servico= models.CharField(max_length=50, unique=True)
    data_emissao_servico= models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        unique_together = ['tipo_servico', 'empresa']

    def __str__(self):
        return f'{self.nome_servico} foi solicitado pela empresa: {self.empresa} em {self.data_emissao_servico}'
    