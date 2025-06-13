from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView
from .serializers import ListUsuarioSerializer, RegistroUsuarioSerializer, EditUsuarioSerializer
from .models import Usuario

# lista todos los usuarios
class ListaUsuariosView(ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = ListUsuarioSerializer


#Registra usuarios
class RegistroUsuarioView(CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = RegistroUsuarioSerializer


#Mustra los datos del usuario autenticado
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user
    return Response({
        'id': user.id,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'telefono': user.telefono,
        'img_profile': user.img_profile.url if user.img_profile else None
    })


#Edita los datos del usuarios (menos la contraseña y el username)
class EditUsuarioView(RetrieveUpdateAPIView):
    serializer_class = EditUsuarioSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
