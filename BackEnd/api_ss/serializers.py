from rest_framework import serializers
from .models import Empresa, Servico

class EmpresaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empresa
        fields = [
            'id',
            'nome_empresa',
            'cnpj_empresa',
            'criacao',
            'ativo',
        ]

class ServicoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'nome_servico': {'write_only': True}
        }
        model = Servico
        fields = [
            'id',
            'empresa',
            'nome_servico',
            'tipo_servico',
            'codigo_servico',
            'data_emissao_servico',
        ]


        
