from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, RegistroUsuarioViewSet, PerfilUsuarioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')
router.register(r'registro', RegistroUsuarioViewSet, basename='registro')
router.register(r'perfil', PerfilUsuarioViewSet, basename='perfil')

urlpatterns = [
    path('', include(router.urls)),
]