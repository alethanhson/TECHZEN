import { reactive, computed } from 'vue'
import type { UserResponse } from '../types/api'

interface AuthState {
  user: UserResponse | null
  token: string | null
  isAuthenticated: boolean
  isLoading: boolean
}

const state = reactive<AuthState>({
  user: JSON.parse(localStorage.getItem('user') || 'null'),
  token: localStorage.getItem('access_token'),
  isAuthenticated: !!localStorage.getItem('access_token'),
  isLoading: false,
})

export const useAuth = () => {
  const setUser = (user: UserResponse | null) => {
    state.user = user
    if (user) {
      localStorage.setItem('user', JSON.stringify(user))
    } else {
      localStorage.removeItem('user')
    }
  }

  const setToken = (token: string | null) => {
    state.token = token
    state.isAuthenticated = !!token
    if (token) {
      localStorage.setItem('access_token', token)
    } else {
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      localStorage.removeItem('user')
    }
  }

  const logout = () => {
    setUser(null)
    setToken(null)
  }

  return {
    state: computed(() => state),
    setUser,
    setToken,
    logout,
  }
}
