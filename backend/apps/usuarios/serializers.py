from rest_framework import serializers
from .models import Usuario

#Para registrar un nuevo usuario
class RegistroUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'telefono', 'password']
        extra_kwargs = {'password': {'write_only': True}} #El campo password no se mostrara en la respuesta del serializer

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Usuario(**validated_data)
        user.set_password(password)  # Aquí se encripta la contraseña
        user.is_active = False
        user.save()
        return user


#Para listar todos los usuarios
class ListUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'telefono', 'img_profile']


#Para editar los datos del usuarios (menos la contraseña y el username)
class EditUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'telefono', 'img_profile']
        read_only_fields = ['username']
