<script setup>
</script>

<template>
  <div class="login-container">
    <div class="login-box">
      <div class="icon-container">
        <font-awesome-icon :icon="['fas', 'envelope']" class="user-icon" />
      </div>
      <h2>REVISA TU CORREO ELECTRÓNICO</h2>
      <p>Tu cuenta se creó exitosamente, ahora debes activarla dando click en el enlace que te enviamos a tu correo electrónico. De lo contrario, no podrás iniciar sesión.</p>
      <p class="register-text"><router-link to="Register">Volver</router-link></p>
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

/* 🔹 Asegurar que el checkbox esté alineado con el texto */
.checkbox-container {
  display: flex;
  align-items: center;
  gap: 5px;
  cursor: pointer;
}

/* 🔹 Enlaces de opciones */
.check {
  text-decoration: none;
  color: white;
  transition: color 0.3s ease-in-out;
}

.check:hover {
  color: #82b1ff;
}

.check:active {
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
