/* eslint-disable @typescript-eslint/no-explicit-any */
import { useToast } from '../store/toast'
import type { ApiResponse } from '../types/api'

const BASE_URL = import.meta.env.VITE_API_URL || '/api'

async function request<T>(url: string, options: RequestInit = {}): Promise<T> {
  const toast = useToast()
  const token = localStorage.getItem('access_token')

  const headers = new Headers(options.headers)
  if (!headers.has('Content-Type') && !(options.body instanceof URLSearchParams)) {
    headers.set('Content-Type', 'application/json')
  }

  if (token) {
    headers.set('Authorization', `Bearer ${token}`)
  }

  try {
    const res = await fetch(`${BASE_URL}${url}`, {
      ...options,
      headers,
    })

    const json: ApiResponse<T> = await res.json()

    if (!res.ok || !json.success) {
      const errorMsg = json.message || `Error ${res.status}`
      console.warn(`[API Client] Request failed: ${url}`, { status: res.status, errorMsg, json })
      toast.error(errorMsg)
      if (res.status === 401) {
        localStorage.removeItem('access_token')
        localStorage.removeItem('user')
      }

      throw new Error(errorMsg)
    }

    if (['POST', 'PUT', 'DELETE'].includes(options.method || 'GET')) {
      let message = json.message || 'Thao tác thành công'
      if (message === 'Successfully') message = 'Thành công!'
      toast.success(message)
    }

    return json.data
  } catch (err: any) {
    if (!(err instanceof Error)) {
      useToast().error('An unexpected error occurred')
    }
    throw err
  }
}

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
