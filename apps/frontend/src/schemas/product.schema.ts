import { z } from 'zod';

export const productSchema = z.object({
  name: z.string().min(3, 'Tên sản phẩm phải có ít nhất 3 ký tự').max(255, 'Tên quá dài'),
  code: z.string().min(2, 'Mã sản phẩm không hợp lệ').regex(/^[A-Z0-9_-]+$/i, 'Mã chỉ được chứa chữ, số, dấu gạch ngang'),
  description: z.string().nullable().optional(),
  price: z.coerce.number({ invalid_type_error: 'Giá phải là một con số' }).min(0, 'Giá không được âm'),
  quantity: z.coerce.number({ invalid_type_error: 'Số lượng phải là một con số' }).int('Số lượng phải là số nguyên').min(0, 'Số lượng không được âm'),
  status: z.enum(['active', 'inactive']),
  tags: z.array(z.string()).optional().default([]),
});

export type ProductFormValues = z.infer<typeof productSchema>;
