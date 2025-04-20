import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
  // withCredentials: true // si usas cookies, como con Django + JWT (implementar después)
})

export default api