import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Navbar from '../components/NavbarComp.vue';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';

const routes = [
  {
    path: '/',
    component: Home
  },

  {
    path: '/Navbar',
    component: Navbar
  },

  {
    path: '/Login',
    component: Login
  },

  {
    path: '/Register',
    component: Register
  },
    
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
