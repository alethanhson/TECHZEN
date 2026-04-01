/**
 * TECHZEN API - TypeScript Definitions (OpenAPI 3.1.0)
 */

export interface TokenResponse {
  access_token: string;
  refresh_token: string;
  token_type: string;
  user?: UserResponse;
}

export interface UserResponse {
  id: number;
  username: string;
  email: string;
  is_active: boolean;
  is_superuser?: boolean;
  role: RoleResponse;
}

export interface RoleResponse {
  id: number;
  name: string;
  description: string | null;
}

export interface TagResponse {
  id: number;
  name: string;
}

export interface ProductResponse {
  id: number;
  code: string;
  name: string;
  description: string | null;
  price: number;
  quantity: number;
  is_active: boolean;
  tags: TagResponse[];
}

export interface ProductCreate {
  code: string;
  name: string;
  description?: string | null;
  price?: number;
  quantity?: number;
  is_active?: boolean;
  tags?: string[];
}

export interface ProductUpdate {
  code?: string | null;
  name?: string | null;
  description?: string | null;
  price?: number | null;
  quantity?: number | null;
  is_active?: boolean | null;
  tags?: string[];
}

export interface RegisterRequest {
  username: string;
  email: string;
  password: string;
  role_id?: number;
}

export interface UserUpdate {
  email?: string | null;
  password?: string | null;
  is_active?: boolean | null;
  role_id?: number | null;
}

export interface TokenRefreshRequest {
  refresh_token: string;
}

export interface ValidationError {
  loc: (string | number)[];
  msg: string;
  type: string;
}

export interface HTTPValidationError {
  detail?: ValidationError[];
}

/** Unified API Wrapper (Backend Specific) */
export interface ApiResponse<T> {
  success: boolean;
  data: T;
  message: string;
  error: unknown;
}
