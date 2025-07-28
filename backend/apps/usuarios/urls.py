from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegistroUsuarioView, user_profile, EditUsuarioView, ListaUsuariosView, MsgActivarCuentaView, MsgRecuperarPwdView
from .users import activar_cuenta, recuperar_pwd

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('registro/', RegistroUsuarioView.as_view(), name='registro-usuario'),
    path('lista/', ListaUsuariosView.as_view(), name='listar-usuarios'),
    path('perfil/', user_profile, name='perfil-usuario'),
    path('edit/', EditUsuarioView.as_view(), name='edit-usuario'),

    # Para envío de emails sobre activar cuenta
    path("msg_activar_cuenta/", MsgActivarCuentaView.as_view(), name="mensage-activar-cuenta"),

    # Para activar la cuenta del usuario
    path('activar_cuenta/<uidb64>/<token>/', activar_cuenta, name='activar-cuenta'),

    # Para envío de emails sobre recuperar contraseña
    path("msg_recuperar_pwd/", MsgRecuperarPwdView.as_view(), name="mensage-recuperar-pwd"),

    # Para recuperar contraseña del usuario
    path("recuperar_pwd/<uidb64>/<token>/", recuperar_pwd, name="recuperar-password"),
]
