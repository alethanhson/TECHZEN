import { reactive, readonly } from 'vue'
import type { UserResponse } from '../types/api'

const STORAGE_KEYS = {
  USER: 'user',
  ACCESS_TOKEN: 'access_token',
  REFRESH_TOKEN: 'refresh_token',
} as const

function getStorage<T>(key: string): T | null {
  try {
    const raw = localStorage.getItem(key)
    return raw ? JSON.parse(raw) : null
  } catch {
    return null
  }
}

function setStorage(key: string, value: unknown) {
  if (value === null || value === undefined) {
    localStorage.removeItem(key)
  } else {
    localStorage.setItem(key, JSON.stringify(value))
  }
}

interface AuthState {
  user: UserResponse | null
  token: string | null
  isAuthenticated: boolean
  isLoading: boolean
}

const state = reactive<AuthState>({
  user: getStorage<UserResponse>(STORAGE_KEYS.USER),
  token: localStorage.getItem(STORAGE_KEYS.ACCESS_TOKEN),
  isAuthenticated: !!localStorage.getItem(STORAGE_KEYS.ACCESS_TOKEN),
  isLoading: false,
})

function clearStorage() {
  localStorage.removeItem(STORAGE_KEYS.ACCESS_TOKEN)
  localStorage.removeItem(STORAGE_KEYS.REFRESH_TOKEN)
  localStorage.removeItem(STORAGE_KEYS.USER)
}

function setUser(user: UserResponse | null) {
  state.user = user
  setStorage(STORAGE_KEYS.USER, user)
}

function setToken(token: string | null | undefined) {
  if (token === undefined) {
    console.warn('[Auth Store] setToken called with undefined, ignoring to prevent accidental logout.')
    return
  }

  state.token = token
  state.isAuthenticated = !!token

  if (token) {
    localStorage.setItem(STORAGE_KEYS.ACCESS_TOKEN, token)
  } else {
    clearStorage()
    state.user = null
  }
}

function setLoading(value: boolean) {
  state.isLoading = value
}

function logout() {
  setToken(null)
}

function initAuth() {
  const token = localStorage.getItem(STORAGE_KEYS.ACCESS_TOKEN)
  const user = getStorage<UserResponse>(STORAGE_KEYS.USER)

  state.token = token
  state.user = user
  state.isAuthenticated = !!token
}

export function useAuth() {
  return {
    state: readonly(state),
    setUser,
    setToken,
    setLoading,
    logout,
    initAuth,
  }
}
