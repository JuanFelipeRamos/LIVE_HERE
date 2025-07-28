import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Navbar from '../components/NavbarComp.vue';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';
import AlertComponent from '../components/AlertComponent.vue';
import FileComponent from '../components/FileComponent.vue';
import VerPerfil from '../views/VerPerfil.vue';
import EditarPerfil from '../views/EditarPerfil.vue';
import MsgActivarCuenta from '../components/MsgActivarCuenta.vue';
import MsgRecuperarPwd from '../components/MsgRecuperarPwd.vue';
import RecuperarPwd from '../views/RecuperarPwd.vue';
import AddNewPwd from '../views/AddNewPwd.vue';

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

  {
    path: '/AlertComponent',
    component: AlertComponent,
    props: true,
  },

  {
    path: '/FileComponent',
    component: FileComponent,
    //props: true,
  },

  {
    path: '/VerPerfil',
    component: VerPerfil
  },

  {
    path: '/EditarPerfil',
    component: EditarPerfil
  },

  {
    path: '/MsgActivarCuenta',
    component: MsgActivarCuenta
  },

  {
    path: '/RecuperarPwd',
    component: RecuperarPwd
  },

  {
    path: '/MsgRecuperarPwd',
    component: MsgRecuperarPwd
  },

  {
    path: '/AddNewPwd',
    component: AddNewPwd
  },
    
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
