from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegistroUsuarioView, user_profile, EditUsuarioView, ListaUsuariosView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('registro/', RegistroUsuarioView.as_view(), name='registro-usuario'),
    path('usuarios/', ListaUsuariosView.as_view(), name='listar-usuarios'),
    path('usuario/perfil/', user_profile, name='perfil-usuario'),
    path('usuario/edit/', EditUsuarioView.as_view(), name='edit-usuario'),
]
