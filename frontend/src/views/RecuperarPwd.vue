<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '../services/axios';

const router = useRouter()
const usuario = ref({
  email: ''
})

const recuperarPassword = async (e) => {
  e.preventDefault()

  try {
    // Para enviar correo de activación de cuenta
    const response = await api.post('/usuarios/msg_recuperar_pwd/', {
      email: usuario.value.email
    })

    usuario.value.email = ''

    router.push('/MsgRecuperarPwd')
  } catch (error) {
    alert('Ocurrió un error al solicitar la recuperación de contraseña.')
    console.error('Error:', error)
    if (error.response && error.response.data) {
      console.log("Detalles del backend:", error.response.data.detalle);
    }
  }
}
</script>

<template>
  <div class="email-container">
    <div class="email-box">
      <div class="icon-container">
        <font-awesome-icon :icon="['fas', 'paper-plane']" class="email-icon" />
      </div>
      <h2>RECUPERA TU CONTRASEÑA</h2>
      <form @submit.prevent="recuperarPassword">
        <p>Ingresa tu correo electrónico (asociado a tu cuenta de Live Here) para que podamos enviarte un enlace donde podrás recuperar tu contraseña.</p>

        <input v-model="usuario.email" type="text" id="email" required />

        <button class="email-btn">Continuar</button>
      </form>

      <div class="login-text">
        <router-link to="Login">
          <a class="login-link">Volver</a>
        </router-link>
      </div>
    </div>
  </div>
</template>


<style scoped>
html, body {
  height: 100%;
  margin: 0;
  padding: 0;
  overflow-x: hidden;
  display: flex;
  flex-direction: column;
}

.email-container {
  flex-grow: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #0c0c24;
  width: 100%;
}


.email-box {
  background-color: #1a1a50;
  padding: 60px 50px;
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

.email-icon {
  font-size: 30px;
  color: white;
}

h2 {
  margin-bottom: 20px;
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
}

#email {
  margin-top: 20px;
}

.email-btn {
  background-color: #2c2c6c;
  color: white;
  font-size: 16px;
  padding: 10px;
  width: 100%;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 20px;
  transition: background-color 0.3s ease-in-out;
}

.email-btn:hover {
  background-color: #4a90e2;
}

.email-btn:active {
  background-color: #2c2c6c;
}

/* 🔹 Asegurar que el checkbox esté alineado con el texto */
.checkbox-container {
  display: flex;
  align-items: center;
  gap: 5px;
  cursor: pointer;
}

/* 🔹 Enlace de registro */
.login-text {
  font-size: 14px;
  margin-top: 15px;
}

.login-link {
  color: white;
  text-decoration: none;
  transition: color 0.3s ease-in-out;
}

.login-link:hover {
  color: #82b1ff;
}

.login-link:active {
  color: white;
}
</style>
