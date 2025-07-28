<script setup>
import { RouterView } from 'vue-router';
import { watch } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();

watch(route, (newRoute) => {
  const darkRoutes = [// Rutas que tendrán fondo oscuro
    '/Login',
    '/Register',
    '/ImgRegister',
    '/MsgActivarCuenta',
    '/RecuperarPwd',
    '/MsgRecuperarPwd',
    '/AddNewPwd',
  ];

  if (darkRoutes.includes(newRoute.path)) {
    document.body.style.backgroundColor = '#0c0c24';
  } else {
    document.body.style.backgroundColor = '#ffffff'; // Fondo blanco para otras
  }
}, { immediate: true });

</script>

<template>
  <div>
    <RouterView />
</div>
</template>


<style>

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  background-color: white;
  font-family: Arial, Helvetica, sans-serif;
  height: 100;
  margin: 0;
  padding: 0;
  color: black;
}

</style>
