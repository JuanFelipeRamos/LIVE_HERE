import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router';
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'; //Librería para íconos
// Importar los íconos que se van a usar
import { faSearch, faUser, faArrowLeft, faBars, faCircleCheck, faXmark } from '@fortawesome/free-solid-svg-icons';

// Agregar los íconos a la librería
library.add(faSearch, faUser, faArrowLeft, faBars, faCircleCheck, faXmark);

const app = createApp(App);
app.component('font-awesome-icon', FontAwesomeIcon);
app.use(router);
app.mount('#app');
