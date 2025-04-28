from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Usuario
from .serializers import RegistroUsuarioSerializer, PerfilUsuarioSerializer, UsuarioSerializer

User = get_user_model() #Se almacena el modelo de usuario en la variable User

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    #Permite crear un usuario incluso si no está logueado, pero para hacer más cosas sí hay que estar logueado
    def get_permissions(self):
        if self.action in ['create']:
            return [AllowAny()]
        return [IsAuthenticated()]
    
    #Solo responde a peticiones GET y solo pueden acceder usuarios autenticados
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


class RegistroUsuarioView(APIView):
    #permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegistroUsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Usuario creado correctamente."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
"""
class RegistroUsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = RegistroUsuarioSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(user.password)
        user.save()"""

class PerfilUsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = PerfilUsuarioSerializer
