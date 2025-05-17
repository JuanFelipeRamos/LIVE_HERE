<script setup>
import { ref, onMounted } from 'vue'
import Navbar from '../components/NavbarComp.vue';
import AlertComponent from '../components/AlertComponent.vue'

const showAlert = ref(false)

onMounted(() => {
  if (localStorage.getItem('loginSuccess') === 'true') {
    showAlert.value = true
    localStorage.removeItem('loginSuccess')
    setTimeout(() => showAlert.value = false, 3000)
  }
})

</script>


<template>
    <div>
        <AlertComponent v-if="showAlert" />
        <Navbar />
    </div>
  
</template>


<style scoped>

body {
    display: flex;
  margin: 0;
  padding: 0;
}

</style>