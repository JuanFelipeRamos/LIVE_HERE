import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
})

// Interceptor para añadir el token en las solicitudes
api.interceptors.request.use(config => {
  let token = localStorage.getItem('access')

  if (!token) {
    token = sessionStorage.getItem('access')
  }

  if (
    token &&
    !config.url.includes('/registro/') &&
    !config.url.includes('/token/')
  ) {
    config.headers.Authorization = `Bearer ${token}`
  }

  return config
})

// Interceptor para manejar errores y renovar el token si expiró
api.interceptors.response.use(
  response => response,
  async error => {
    const originalRequest = error.config

    // Si recibimos 401 y no hemos intentado renovar el token todavía
    if (error.response && error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true
      try {
        let refresh = localStorage.getItem('refresh')
        let storageType = 'localStorage'

        if (!refresh) {
          refresh = sessionStorage.getItem('refresh')
          storageType = 'sessionStorage'
        }

        // Llama al endpoint para renovar el token
        const res = await axios.post('http://localhost:8000/api/token/refresh/', {
          refresh: refresh
        })

        const newAccessToken = res.data.access

        if (storageType === 'localStorage') {
          localStorage.setItem('access', newAccessToken)
        } else {
          sessionStorage.setItem('access', newAccessToken)
        }

        // Actualiza el token y vuelve a intentar la solicitud original
        originalRequest.headers.Authorization = `Bearer ${newAccessToken}`
        return api(originalRequest)
      } catch (refreshError) {
        console.error('Error al refrescar el token:', refreshError)

        // Borra los tokens si falló la renovación y redirige a login
        if (storageType === 'localStorage') {
          localStorage.removeItem('access')
          localStorage.removeItem('refresh')
          localStorage.removeItem('user')
        } else {
          sessionStorage.removeItem('access')
          sessionStorage.removeItem('refresh')
          sessionStorage.removeItem('user')
        }
        window.location.href = '/Login'
      }
    }

    return Promise.reject(error)
  }
)

export default api
