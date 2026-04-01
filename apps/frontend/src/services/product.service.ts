import api from './api'
import type { ProductResponse, ProductCreate, ProductUpdate } from '../types/api'

const resource = 'products'
const crud = api.createCrudService<ProductResponse>(resource)

export const ProductService = {
  ...crud,
  create: (data: ProductCreate) => crud.create(data),
  update: (id: number, data: ProductUpdate) => crud.update(id, data),
}

export default ProductService
