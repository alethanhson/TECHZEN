import api from './api'
import type { TokenResponse, UserResponse, RegisterRequest } from '../types/api'

export const AuthService = {
  async login(formData: Record<string, string>): Promise<TokenResponse> {
    const body = new URLSearchParams()
    for (const key in formData) {
      const value = formData[key]
      if (value !== undefined) {
        body.append(key, value)
      }
    }
    
    return api.request<TokenResponse>('/auth/login', {
      method: 'POST',
      body,
    })
  },

  async register(data: RegisterRequest): Promise<UserResponse> {
    return api.request<UserResponse>('/auth/register', {
      method: 'POST',
      body: JSON.stringify(data),
    })
  },

  async refresh(refreshToken: string): Promise<TokenResponse> {
    return api.request<TokenResponse>('/auth/refresh', {
      method: 'POST',
      body: JSON.stringify({ refresh_token: refreshToken }),
    })
  },
}

export default AuthService
