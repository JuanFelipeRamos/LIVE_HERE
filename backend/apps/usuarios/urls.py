from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, RegistroUsuarioViewSet, PerfilUsuarioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'registro', RegistroUsuarioViewSet)
router.register(r'perfil', PerfilUsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
