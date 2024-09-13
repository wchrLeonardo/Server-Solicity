from rest_framework import generics
from .models import Empresa, Servico
from .serializers import EmpresaSerializer, ServicoSerializer
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

# Generic Views
# Plural -- EndPoints de coleção
# Singular -- EndPoints de Individuo


# ===================== API V1 ============================
class EmpresasAPIView(generics.ListCreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    
class EmpresaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    
class ServicosAPIView(generics.ListCreateAPIView):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(empresa_id = self.kwargs.get('empresa_pk'))
        return self.queryset.all()
    

class ServicoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

    def get_object(self):
        if self.kwargs.get('empresa_pk'):
            return get_object_or_404(self.get_queryset(), empresa_id=self.kwargs.get('empresa_pk'), pk=self.kwargs.get('servico_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('servico_pk'))
    
# =================== API V2 ================================

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

    @action(detail=True, methods=('get'))
    def servicos(self, request, pk=None):
        curso = self.get_object()
        serializer = ServicoSerializer(empresa.servicos.all(), many=True)
        return Response(serializer.data)

'''VIEWSET PADRÃO:
class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
'''
# VIEWSET CUSTOMIZADA:
class ServicoViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer