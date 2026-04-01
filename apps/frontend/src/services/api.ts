const BASE_URL = import.meta.env.VITE_API_URL || '/api'

interface ApiResponse<T> {
  success: boolean
  data: T
  message: string
  error: any
}

async function request<T>(url: string, options: RequestInit = {}): Promise<T> {
  const res = await fetch(`${BASE_URL}${url}`, {
    headers: { 'Content-Type': 'application/json', ...options.headers },
    ...options,
  })

  const json: ApiResponse<T> = await res.json()

  if (!res.ok || !json.success) {
    throw new Error(json.message || `HTTP ${res.status}`)
  }

  return json.data
}

/** Factory tạo CRUD service cho bất kỳ entity nào */
export function createCrudService<T>(resource: string) {
  return {
    getAll: (params?: Record<string, any>) => {
      const query = params ? '?' + new URLSearchParams(params).toString() : ''
      return request<T[]>(`/${resource}${query}`)
    },
    getById: (id: number) => request<T>(`/${resource}/${id}`),
    create: (data: any) => request<T>(`/${resource}`, { method: 'POST', body: JSON.stringify(data) }),
    update: (id: number, data: any) => request<T>(`/${resource}/${id}`, { method: 'PUT', body: JSON.stringify(data) }),
    delete: (id: number) => request<any>(`/${resource}/${id}`, { method: 'DELETE' }),
  }
}

export default { request, createCrudService }
