<script setup>
import { ref, onMounted } from 'vue'
import api from '../services/axios';
import Navbar from '../components/NavbarComp.vue';

const user = ref(null)

const fetchUserProfile = async () => {
  try {
    const token = localStorage.getItem('access')
    if (!token) {
      console.error('No hay token de acceso. Redirige al login.')
      return
    }

    const response = await api.get('/usuario/perfil/', {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })

    user.value = response.data
  } catch (error) {
    console.error('Error al obtener el perfil del usuario:', error)
  }
}

onMounted(() => {
  fetchUserProfile()
})

</script>


<template>
  <div>
    <div class="navbar-wrapper">
      <Navbar />
    </div>
    <div class="profile-container" v-if="user">
      <div class="profile-card">
        <div class="profile-left">
          <font-awesome-icon :icon="['fas', 'user']" class="user-icon" />
        </div>

        <div class="profile-right">
          <h1 class="user-name">{{ user.first_name }} {{ user.last_name }}</h1>
          <p class="user-username">@{{ user.username }}</p>

          <div class="info-grid">
            <div class="info-block">
              <p class="label">Correo electrónico:</p>
              <p class="value">{{ user.email }}</p>
            </div>
            <div class="info-block">
              <p class="label">Teléfono:</p>
              <p class="value">{{ user.telefono }}</p>
            </div>
          </div>

          <div class="buttons">
            <button class="action-button">Editar perfil</button>
            <button class="action-button">Favoritos</button>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <p>Cargando...</p>
    </div>
  </div>
</template>



<style scoped>
.navbar-wrapper {
  background-color: #0c0c40;
}

.profile-container {
  display: flex;
  justify-content: center;
  padding: 2rem;
  padding-top: 90px;
}

.profile-card {
  display: flex;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 8px 10px rgba(0, 0, 0, 0.2);
  padding: 40px;
  max-width: 1000px;
  width: 100%;
  gap: 2rem;
  align-items: center;
}

.profile-left {
  display: flex;
  justify-content: center;
  align-items: center;
}

.user-icon {
  font-size: 6rem;
  color: #fff;
  background-color: #252258;
  padding: 2rem;
  border-radius: 50%;
}

.profile-right {
  flex: 1;
  width: 360px;
}

.user-name {
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 0.2rem;
}

.user-username {
  color: #555;
  margin-bottom: 2rem;
}

.info-grid {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 2rem;
  margin-bottom: 2.5rem;
}

.info-block {
  flex: 1 1 45%;
}

.label {
  font-weight: bold;
  margin-bottom: 0.3rem;
}

.value {
  border-bottom: 1px solid #aaa;
  padding-bottom: 0.2rem;
  color: #333;
  word-break: break-word;
}

.buttons {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.action-button {
  background-color: #252258;
  color: white;
  padding: 0.8rem 2rem;
  border-radius: 6px;
  font-weight: bold;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
  min-width: 160px;
}

.action-button:hover {
  background-color: #1d1b4e;
}

/* Responsive para móviles */
@media (max-width: 768px) {
  .profile-card {
    flex-direction: column;
    text-align: center;
  }

  .profile-left {
    margin-bottom: 1rem;
  }

  .info-grid {
    flex-direction: column;
  }

  .buttons {
    flex-direction: column;
    align-items: center;
  }

  .action-button {
    width: 100%;
  }
}
</style>
