from rest_framework import serializers
from .models import Usuario

#Serializer para gestionar usuarios en el admin
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

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
        user.save()
        return user


#Para visualizar el perfil del usuario
class PerfilUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'img_profile', 'username', 'first_name', 'last_name', 'email', 'telefono']
