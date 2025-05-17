<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const isLoggedIn = ref(false)
const router = useRouter()

onMounted(() => {
  const token = localStorage.getItem('access')
  isLoggedIn.value = !!token
})

function logout() {
  localStorage.removeItem('access')
  localStorage.removeItem('refresh')
  isLoggedIn.value = false
  closeModal()
  router.push('/')
  console.log('Sesión cerrada con éxito')
}

// Para el menú modal
const showModal = ref(false)

function openModal() {
  showModal.value = true
}

function closeModal() {
  showModal.value = false
}

function handleOverlayClick(e) {
  if (e.target.classList.contains('modal-overlay')) {
    closeModal()
  }
}

</script>

<template>
  <nav class="navbar">
    <div class="container">
      <div class="logo">
        <img src="/public/Logo_LIVE_HERE.png" alt="Logo LIVE HERE" class="imgLogo">
      </div>
      <div class="search-bar">
        <input type="text" placeholder="Encuentra casas, apartamentos y más" />
        <button>
          <font-awesome-icon :icon="['fas', 'magnifying-glass']" class="lupa" />
        </button>
      </div>

      <!-- Si SÍ está logueado -->
      <div class="middle-link" v-if="isLoggedIn">
        <a href="#">PUBICAR</a>
      </div>

      <div class="middle-link">
        <a href="#">CATEGORÍAS</a>
        <!-- <font-awesome-icon :icon="['fas', 'caret-down']" /> -->
      </div>

      <!-- Si NO está logueado -->
      <ul class="nav-links" v-if="!isLoggedIn">
        <li>
          <router-link to="/Login">
            <a>INICIAR SESIÓN</a>
          </router-link>
        </li>
      </ul>
      <div class="menu-wrapper" v-else>
        <font-awesome-icon icon="bars" class="menu-icon" @click="openModal" />
      </div>
      
      <!-- Modal lateral -->
      <div v-if="showModal" class="modal-overlay" @click="handleOverlayClick">
        <div class="modal-menu">
          <p class="volver" @click="closeModal">
            <font-awesome-icon :icon="['fas', 'arrow-left']" /> Volver
          </p>
          <ul>
            <li><a href="#">Ver perfil</a></li>
            <li><a href="#" @click="logout">Cerrar sesión</a></li>
          </ul>
        </div>
      </div>
    </div>
  </nav>
</template>


<style scoped>
.navbar {
  background-color: #101349;
  color: white;
  padding: 10px 20px;
  width: 100%;
  box-sizing: border-box;
  position: fixed;
  top: 0;
  left: 0;
}

.container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
}

.logo {
  display: flex;
  align-items: center;
}

.imgLogo {
  width: 100px;
}

.search-bar {
  display: flex;
  align-items: center;
  background: white;
  padding: 8px;
  border-radius: 25px;
  width: 40%;
  max-width: 450px;
  position: relative;
  margin-left: 90px;
}

.search-bar input {
  border: none;
  outline: none;
  padding: 3px;
  flex-grow: 1;
  font-size: 1rem;
}

.search-bar input::placeholder {
  font-size: 14px;
}

.search-bar button {
  background: none;
  border: none;
  cursor: pointer;
  padding: 5px;
}

.lupa {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 16px;
  color: gray;
  cursor: pointer;
}

.lupa:hover {
  color: rgb(90, 90, 90);
}

.middle-link {
  flex: 1;
  text-align: right;
  padding-right: 20px;
}

.middle-link a,
.nav-links a {
  text-decoration: none;
  font-size: 1rem;
  color: white;
  transition: color 0.3s ease-in-out;
}

.nav-links {
  list-style: none;
  display: flex;
  font-size: 1rem;
}

.middle-link a:hover,
.nav-links a:hover {
  color: #4A90E2;
}

.middle-link a:active,
.nav-links a:active {
  color: #9dc2ff;
}

input {
  background-color: white;
  border-radius: 22px;
  width: 100%;
  color: black;
  outline: none;
  padding: 12px 35px 12px 10px;
}

/* Responsivo */
@media (max-width: 1024px) {
  .container {
    flex-direction: column;
    text-align: center;
  }

  .search-bar {
    width: 100%;
    max-width: 400px;
    margin-top: 10px;
  }

  .middle-link {
    margin-top: 10px;
  }

  .nav-links {
    flex-direction: row;
    justify-content: center;
    margin-top: 10px;
  }
}

@media (max-width: 768px) {
  .container {
    flex-direction: column;
    text-align: center;
  }

  .search-bar {
    width: 100%;
    max-width: 350px;
    margin-top: 10px;
  }

  .middle-link {
    margin-top: 10px;
  }

  .nav-links {
    flex-direction: column;
    gap: 10px;
    margin-top: 10px;
  }
}

.menu-icon {
  font-size: 32px;
  color: white;
  cursor: pointer;
  transition: color 0.3s ease-in-out;
  margin: 0;
  padding: 0 10px 0 0;
}

.menu-icon:hover {
  color: #4A90E2;
}

.modal-overlay {
  position: fixed;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(4px);
  display: flex;
  justify-content: flex-end;
  z-index: 999;
}

.modal-menu {
  background-color: #101349;
  color: white;
  width: 250px;
  height: 100%;
  padding: 20px;
  box-shadow: -2px 0 5px rgba(0,0,0,0.2);

  transform: translateX(100%);
  animation: slideIn 0.3s forwards;
}

@keyframes slideIn {
  to {
    transform: translateX(0%);
  }
}

.modal-menu ul {
  list-style: none;
  padding: 0;
  margin-top: 20px;
}

.modal-menu ul li a {
  display: block;
  color: white;
  padding: 10px 0;
  text-decoration: none;
  transition: color 0.3s ease-in-out;
}

.modal-menu ul li a:hover {
  color: #4A90E2;
}

.modal-menu ul li a:active {
  color: #9dc2ff;
}

.volver {
  cursor: pointer;
  font-weight: bold;
  display: flex;
  align-items: center;
  gap: 5px;
  border-bottom: 1px solid white;
  padding-bottom: 5px;
}

.volver:hover {
  color: #4A90E2;
}

.volver:active {
  color: #9dc2ff;
}

.menu-wrapper {
  display: flex;
  justify-content: flex-end;
  flex: 1;
  padding-right: 0px;
}

</style>
