from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegistroUsuarioView, user_profile, EditUsuarioView, ListaUsuariosView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('registro/', RegistroUsuarioView.as_view(), name='registro-usuario'),
    path('lista/', ListaUsuariosView.as_view(), name='listar-usuarios'),
    path('perfil/', user_profile, name='perfil-usuario'),
    path('edit/', EditUsuarioView.as_view(), name='edit-usuario'),
]
