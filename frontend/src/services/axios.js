import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
})

api.interceptors.request.use(config => {
  const token = localStorage.getItem('access')

  // Evita enviar el token en las rutas públicas como /registro/ y /token/
  if (
    token &&
    !config.url.includes('/registro/') &&
    !config.url.includes('/token/')
  ) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export default api