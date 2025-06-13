<script setup>
import { ref } from 'vue'
import Navbar from '../components/NavbarComp.vue';
import FileComponent from '../components/FileComponent.vue'

const username = ref('Felipe_Ramos2024')
const firstName = ref('Juan')
const lastName = ref('Ramos Rojas')
const email = ref('dshvbolad22@gmail.com')
const telefono = ref('3207341961')

</script>

<template>
    <div>
        <Navbar />
        <div class="form-wrapper">
          <div class="edit-form">
            <h1 class="form-title">Edita tu información</h1>
      
            <div class="form-group">
              <label>Nombre de usuario:</label>
              <input type="text" v-model="username" disabled />
            </div>
      
            <div class="form-row">
              <div class="form-group">
                <label>Nombres:</label>
                <input type="text" v-model="firstName" />
              </div>
              <div class="form-group">
                <label>Apellidos:</label>
                <input type="text" v-model="lastName" />
              </div>
            </div>
      
            <div class="form-row">
              <div class="form-group">
                <label>Correo electrónico:</label>
                <input type="email" v-model="email" />
              </div>
              <div class="form-group">
                <label>Teléfono:</label>
                <input type="text" v-model="telefono" />
              </div>
            </div>

      <hr class="divider" />

      <div class="form-group">
        <label>Foto de perfil:</label>
        <FileComponent />
      </div>

      <hr class="divider" />

      <div class="form-group">
        <button class="save-button">Guardar cambios</button>
      </div>
    </div>
  </div>
  </div>
</template>

<style scoped>
.form-wrapper {
  display: flex;
  justify-content: center;
  padding: 2rem;
  padding-top: 90px;
}

.edit-form {
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 8px 10px rgba(0, 0, 0, 0.2);
  padding: 40px;
  max-width: 800px;
  width: 100%;
}

.form-title {
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 2rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  font-weight: bold;
  display: block;
  margin-bottom: 0.5rem;
}

input[type="text"],
input[type="email"] {
  width: 100%;
  padding: 0.6rem;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 1rem;
}

input[disabled] {
  background-color: #eee;
  color: #666;
  cursor: not-allowed;
}

.form-row {
  display: flex;
  gap: 2rem;
  flex-wrap: wrap;
}

.divider {
  margin: 2rem 0;
  border: none;
  border-top: 1px solid #ccc;
}

.save-button {
  background-color: #252258;
  color: white;
  padding: 0.8rem 2rem;
  border-radius: 6px;
  font-weight: bold;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
  width: 100%;
  max-width: 250px;
}

.save-button:hover {
  background-color: #1d1b4e;
}

@media (max-width: 768px) {
  .form-row {
    flex-direction: column;
  }

  .save-button {
    width: 100%;
  }
}
</style>
