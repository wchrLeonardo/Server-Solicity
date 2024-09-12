from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from .models import UserService
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserService.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return UserService.objects.filter(id=self.request.user.id)
    
    def destroy(self, request, *args, **kwargs):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CreateUserView(generics.CreateAPIView):
    queryset = UserService.objects.all()
    serializer_class = UserSerializer