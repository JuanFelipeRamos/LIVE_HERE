import api from "./axios"

export const verPerfil = async () => {
  try {
    const tokenLocal = localStorage.getItem('access')
    const tokenStorage = sessionStorage.getItem('access')
    
    if (!tokenLocal && !tokenStorage) {
      console.error('No hay token de acceso. Redirige al login.')
      return
    }

    let token = tokenLocal || tokenStorage

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