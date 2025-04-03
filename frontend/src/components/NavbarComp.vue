<script setup>

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
      <ul class="nav-links">
        <li><a href="#">CATEGORÍAS</a></li>
        <li><a href="#">INICIAR SESIÓN</a></li>
      </ul>
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
  font-size: 1.5rem;
  font-weight: bold;
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
}

.search-bar input {
  border: none;
  outline: none;
  padding: 8px;
  flex-grow: 1;
  font-size: 1rem;
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

.nav-links {
  list-style: none;
  display: flex;
  gap: 20px;
  font-size: 1rem;
}

.nav-links a {
  color: white;
  text-decoration: none;
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

  .nav-links {
    flex-direction: column;
    gap: 10px;
    margin-top: 10px;
  }
}

input {
  background-color: white;
  border-radius: 22px;
  width: 100%;
  color: black;
  outline: none;
  padding: 12px 35px 12px 10px;
}
</style>
