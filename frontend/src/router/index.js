import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Navbar from '../components/NavbarComp.vue';

const routes = [
  {
    path: '/',
    component: Home
  },

  {
    path: '/Navbar',
    component: Navbar
  },
    
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
