<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import api from '../services/axios'
import { usePasswordToggle } from '../services/verPassword'
import AlertComponent from '../components/AlertComponent.vue'

const router = useRouter()
const usuario = ref({
  username: '',
  password: ''
})

const login = async () => {
  try {
    const response = await api.post('/token/', {
      username: usuario.value.username,
      password: usuario.value.password,
    })

    // Guardar tokens en localStorage
    localStorage.setItem('access', response.data.access)
    localStorage.setItem('refresh', response.data.refresh)

    console.log('Inicio de sesión exitoso')
    localStorage.setItem('loginSuccess', 'true') // Para mostrar el compomente AlertComponent.vue
    router.push('/') // Redirige a la página de inicio

  } catch (error) {
    alert('Error al iniciar sesión')
    console.error(error)
  }
}

// Mostrar modal de alerta
const mostrarModal1 = ref(false)
const mostrarModal2 = ref(false)

onMounted(() => {
  const urlParams = new URLSearchParams(window.location.search)
  if (urlParams.get('cuenta-activada') === 'true') {
    mostrarModal1.value = true
    setTimeout(() => mostrarModal1.value = false, 3000)
  }

  if (urlParams.get('password-recuperada') === 'true') {
    mostrarModal2.value = true
    setTimeout(() => mostrarModal2.value = false, 3000)
  }
})

// Para mostrar o no el texto que se escribe en el input de contraseña
const { mostrarPassword, togglePassword } = usePasswordToggle()

</script>

<template>
  <div class="login-container">
    <div>
        <AlertComponent v-if="mostrarModal1" title="Correo electrónico verificado" message="¡Ya puedes iniciar sesión!" />
        <AlertComponent v-if="mostrarModal2" title="Contraseña recuperada con éxito" message="¡Ya puedes iniciar sesión!" />
        <Navbar />
    </div>
    <div class="login-box">
      <div class="icon-container">
        <font-awesome-icon :icon="['fas', 'user']" class="user-icon" />
      </div>
      <h2>INICIA SESIÓN</h2>
      <form @submit.prevent="login">
        <label for="username">Nombre de usuario</label>
        <input v-model="usuario.username" type="text" id="username" required />

        <!--<label for="password">Contraseña</label>
        <input v-model="usuario.password" :type="mostrarPassword ? 'text' : 'password'" id="password" required />-->

        <div class="input-password-container">
          <label for="password">Contraseña</label>
          <input
            v-model="usuario.password"
            :type="mostrarPassword ? 'text' : 'password'"
          />
          <span class="material-symbols-outlined icono-ojo" @click="togglePassword">
            {{ mostrarPassword ? 'visibility' : 'visibility_off' }}
          </span>
        </div>

        <div class="options">
          <label class="checkbox-container">
            <input type="checkbox" />
            <span class="checkmark"></span>
            <span class="check">Mantener sesión iniciada</span>
          </label>
          <router-link to="RecuperarPwd"><a class="forgot-password">¿Olvidó su contraseña?</a></router-link>
        </div>

        <button class="login-btn">Continuar</button>
      </form>

      <p class="register-text">
        ¿No tienes cuenta?
        <router-link to="Register"><a class="register-link">Regístrate aquí</a></router-link>
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

  .input-password-container {
  position: relative;
  }
  
  .input-password-container input {
    padding-right: 40px; /* espacio para el ícono */
  }

  .icono-ojo {
    position: absolute;
    right: 10px;
    top: 72%;
    transform: translateY(-50%);
    cursor: pointer;
    color: #555;
    font-size: 24px;
  }
  
  /* 🔹 Opciones debajo del input de contraseña */
  .options {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 14px;
    margin: 10px 0;
  }
  
  /* 🔹 Asegurar que el checkbox esté alineado con el texto */
  .checkbox-container {
    display: flex;
    align-items: center;
    gap: 5px;
    cursor: pointer;
  }
  
  .checkbox-container input {
    width: 16px;
    height: 16px;
  }
  
  /* 🔹 Enlaces de opciones */
  .options a, .check {
    text-decoration: none;
    color: white;
    transition: color 0.3s ease-in-out;
  }
  
  .options a:hover, .check:hover {
    color: #82b1ff;
  }
  
  .options a:active, .check:active {
    color: white;
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
  