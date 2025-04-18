import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router';
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'; //Librería para íconos
// Importar los íconos que se van a usar
import { faSearch } from '@fortawesome/free-solid-svg-icons'; //Icono de búsqueda
import { faUser } from '@fortawesome/free-solid-svg-icons'; //Icono de usuario

// Agregar los íconos a la librería
library.add(faSearch);
library.add(faUser);

const app = createApp(App);
app.component('font-awesome-icon', FontAwesomeIcon);
app.use(router);
app.mount('#app');
