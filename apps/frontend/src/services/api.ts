import axios from 'axios'
import type { AxiosInstance, AxiosRequestConfig, AxiosResponse } from 'axios'

// Cấu hình URL API mặc định cho test (thường là localhost:8080)
const baseURL = import.meta.env.VITE_API_URL || 'http://localhost:8080/api'

const api: AxiosInstance = axios.create({
  baseURL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 5000,
})

// Bộ đánh chặn (Interceptors) để xử lý lỗi hoặc thêm token nếu cần
api.interceptors.response.use(
  (response: AxiosResponse) => response.data,
  (error) => {
    console.error('API Error:', error.response?.data || error.message)
    return Promise.reject(error)
  }
)

export const createCrudService = (resource: string) => ({
  getAll: (params?: any) => api.get(`/${resource}`, { params }),
  getById: (id: string | number) => api.get(`/${resource}/${id}`),
  create: (data: any) => api.post(`/${resource}`, data),
  update: (id: string | number, data: any) => api.put(`/${resource}/${id}`, data),
  delete: (id: string | number) => api.delete(`/${resource}/${id}`),
})

export default api
