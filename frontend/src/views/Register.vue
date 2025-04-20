<script setup>
import { ref } from 'vue';
import api from '../services/axios';

//const errorMsg = ref("");

const usuario = ref({
  username: "",
  first_name: "",
  last_name: "",
  email: "",
  telefono: "",
  password: ""
});

const registrarUsuario = async (e) => {
  e.preventDefault()

  try {
    const response = await api.post('/usuarios/', usuario.value)
    alert('Usuario registrado exitosamente.')
    //console.log('Respuesta del backend:', response.data)

    usuario.value = {
      username: '',
      first_name: '',
      last_name: '',
      email: '',
      telefono: '',
      password: ''
    }
  } catch (error) {
    alert('Ocurrió un error al registrar el usuario.')
    console.error('Error al registrar:', error)
  }
}

</script>


<template>
  <div class="login-container">
    <div class="login-box">
      <div class="icon-container">
        <font-awesome-icon :icon="['fas', 'user']" class="user-icon" />
      </div>
      <h2>REGÍSTRATE</h2>
      <form @submit.prevent="registrarUsuario">
        <label for="username">Nombre de usuario</label>
        <input v-model="usuario.username" type="text" id="username" required />

        <div class="name-row">
          <div class="name-column">
            <label for="first-name">Nombres</label>
            <input v-model="usuario.first_name" type="text" id="first-name" />
          </div>
          <div class="name-column">
            <label for="last-name">Apellidos</label>
            <input v-model="usuario.last_name" type="text" id="last-name" />
          </div>
        </div>

        <div class="name-row">
          <div class="name-column">
            <label for="email">Correo electrónico</label>
            <input v-model="usuario.email" type="email" id="email" required />
          </div>
          <div class="name-column">
            <label for="phone">Teléfono</label>
            <input v-model="usuario.telefono" type="tel" id="phone" required />
          </div>
        </div>

        <label for="password">Contraseña</label>
        <input v-model="usuario.password" type="password" id="password" required />

        <button class="login-btn">Continuar</button>
      </form>

      <p class="register-text">
        ¿Ya tienes una cuenta?
        <router-link to="Login">
          <a class="register-link">Inicia sesión aquí</a>
        </router-link>
      </p>
    </div>
  </div>
</template>


<style scoped>
html,
body {
  height: 100%;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
  display: flex;
  flex-direction: column;
}

.login-container {
  flex-grow: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #0c0c24;
  width: 100%;
}

.login-box {
  background-color: #1a1a50;
  padding: 19px 50px;
  border-radius: 15px;
  text-align: center;
  width: 100%;
  max-width: 400px;
  color: white;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.5);
}

.icon-container {
  background-color: #2c2c6c;
  width: 70px;
  height: 70px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 50%;
  margin: 0 auto 20px;
}

.user-icon {
  font-size: 30px;
  color: white;
}

h2 {
  margin-bottom: 20px;
}

label {
  display: block;
  text-align: left;
  font-size: 14px;
  margin: 10px 0 5px;
}

input {
  width: 100%;
  padding: 8px;
  border-radius: 5px;
  border: none;
  outline: none;
  font-size: 16px;
  background-color: white;
  color: black;
  margin-bottom: 10px;
}

/* 🔹 Inputs lado a lado */
.name-row {
  display: flex;
  gap: 10px;
  justify-content: space-between;
}

.name-column {
  flex: 1;
}

/* 🔹 Botón */
.login-btn {
  background-color: #2c2c6c;
  color: white;
  font-size: 16px;
  padding: 10px;
  width: 100%;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 10px;
  transition: background-color 0.3s ease-in-out;
}

.login-btn:hover {
  background-color: #4a90e2;
}

.login-btn:active {
  background-color: #2c2c6c;
}

/* 🔹 Enlace de registro */
.register-text {
  font-size: 14px;
  margin-top: 15px;
}

.register-link {
  color: white;
  text-decoration: none;
  transition: color 0.3s ease-in-out;
}

.register-link:hover {
  color: #82b1ff;
}

.register-link:active {
  color: white;
}
</style>
