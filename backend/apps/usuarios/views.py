from rest_framework.viewsets import ModelViewSet
from .models import Usuario
from .serializers import RegistroUsuarioSerializer, PerfilUsuarioSerializer, UsuarioSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class RegistroUsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = RegistroUsuarioSerializer

class PerfilUsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = PerfilUsuarioSerializer
