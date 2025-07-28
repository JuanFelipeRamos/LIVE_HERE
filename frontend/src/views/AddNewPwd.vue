<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '../services/axios'

const router = useRouter()
const route = useRoute()

const uidb64 = route.query.uidb64
const token = route.query.token

console.log("uidb64:", uidb64)
console.log("token:", token)

const usuario = ref({
  password: '',
  passwordConfirmada: ''
})

const addNewPassword = async () => {
  if (usuario.value.password !== usuario.value.passwordConfirmada){
    console.log("error, las contraseñas no coinciden")
    alert("Error, las contraseñas ongresadas no coinciden entre ellas, deben ser iguales")
    return
  }

  try {
    const response = await api.post(`/usuarios/recuperar_pwd/${uidb64}/${token}/`, {
      password: usuario.value.password
    })
    
    console.log(response.data)

    usuario.value = {
      password: '',
      passwordConfirmada: ''
    }

    router.push('/Login?password-recuperada=true')
  } catch (error) {
    console.error("Error al recuperar contraseña:", error)
    alert("Hubo un problema al cambiar tu contraseña.")
  }
}

</script>

<template>
  <div class="login-container">
    <div class="login-box">
      <div class="icon-container">
        <font-awesome-icon icon="fa-solid fa-unlock" class="user-icon" />
      </div>
      <h2>CREA UNA NUEVA CONTRASEÑA</h2>
      <form @submit.prevent="addNewPassword">
        <label for="username">Nueva contraseña</label>
        <input v-model="usuario.password" type="password" id="username" required />

        <label for="password">Confirmar contraseña</label>
        <input v-model="usuario.passwordConfirmada" type="password" id="password" required />

        <button class="login-btn">Continuar</button>
      </form>

      <p class="register-text">
        <router-link to="Login"><a class="register-link">Salir</a></router-link>
      </p>
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
  
  /* 🔹 Corregir inputs: fondo blanco, texto negro */
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

  #username {
    margin-bottom: 10px;
  }
  
  /* 🔹 Botón de login */
  .login-btn {
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
  