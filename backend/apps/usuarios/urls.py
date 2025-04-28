from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, RegistroUsuarioView, PerfilUsuarioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')
router.register(r'perfil', PerfilUsuarioViewSet, basename='perfil')

urlpatterns = [
    path('', include(router.urls)),
    path('registro/', RegistroUsuarioView.as_view(), name='registro-usuario'),
]