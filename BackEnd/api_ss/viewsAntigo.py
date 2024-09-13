from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Empresa, Servico
from .serializers import EmpresaSerializer, ServicoSerializer

class EmpresaAPIView(APIView):

    def get(self, request):
        empresas = Empresa.objects.all()
        serializer = EmpresaSerializer(empresas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmpresaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response({"mensagem": "Criado com sucesso!"}, status=status.HTTP_201_CREATED) 
        # return Response({"id": serializer.data['id'], "empresa": serializer.data['nome_empresa']}, status=status.HTTP_201_CREATED) 

class ServicoAPIView(APIView):

    def get(self, request):
        servicos = Servico.objects.all()
        serializer = ServicoSerializer(servicos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServicoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
