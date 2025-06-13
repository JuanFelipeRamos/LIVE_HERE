import api from "./axios"

export const verPerfil = async () => {
  try {
    const token = localStorage.getItem('access')
    if (!token) {
      console.error('No hay token de acceso. Redirige al login.')
      return
    }

    const response = await api.get('/usuarios/perfil/', {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })

    return response.data
  } catch (error) {
    console.error('Error al obtener el perfil del usuario:', error)
  }
}