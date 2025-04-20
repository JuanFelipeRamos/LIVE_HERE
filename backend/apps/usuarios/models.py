from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    telefono = models.CharField(max_length=15)
    img_profile = models.ImageField(upload_to="ImagenesPerfil", null=True, blank=True)
    """
    Campos que trae este modelo por defecto:
    username
    first_name
    last_name
    email
    password
    is_staff
    is_superuser
    date_joined
    last_login
    etc.
    """

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
