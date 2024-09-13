from django.urls import path
from .views import EmpresasAPIView, ServicosAPIView, EmpresaAPIView, ServicoAPIView, EmpresaViewSet, ServicoViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("servicos", ServicoViewSet)

urlpatterns = [
    path('empresas/', EmpresasAPIView.as_view(), name='empresas'),
    path('empresas/<int:pk>', EmpresaAPIView.as_view(), name='empresa'),
    path('empresas/<int:empresa_pk>/servicos/', ServicosAPIView.as_view(), name='empresa_servicos'),
    path('empresas/<int:empresa_pk>/servicos/<int:servico_pk>', ServicoAPIView.as_view(), name='empresa_servico'),
    path('servicos/<int:servico_pk>', ServicoAPIView.as_view(), name='servico'),
    path('servicos/', ServicosAPIView.as_view(), name='servicos'),
]
