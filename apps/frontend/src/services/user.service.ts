import api from './api'
import type { UserResponse, UserUpdate } from '../types/api'

const resource = 'users'
const crud = api.createCrudService<UserResponse>(resource)

export const UserService = {
  ...crud,
  async getMe(): Promise<UserResponse> {
    return api.request<UserResponse>(`/${resource}/me`)
  },
}

export default UserService
