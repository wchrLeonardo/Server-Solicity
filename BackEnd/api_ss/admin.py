from django.contrib import admin
from .models import Servico, Empresa

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome_empresa', 'cnpj_empresa', 'criacao', 'atualizacao', 'ativo')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('empresa','nome_servico','tipo_servico','codigo_servico','data_emissao_servico','criacao','atualizacao','ativo')