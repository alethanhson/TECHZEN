import { reactive } from 'vue'

export interface ToastMessage {
  id: number;
  title: string;
  body: string;
  variant: 'success' | 'danger' | 'warning' | 'info';
  visible: boolean;
}

const state = reactive<{ toasts: ToastMessage[] }>({
  toasts: [],
})

let nextId = 1

export const useToast = () => {
  const showToast = (title: string, body: string, variant: ToastMessage['variant'] = 'success') => {
    const id = nextId++
    const toast: ToastMessage = { id, title, body, variant, visible: true }
    state.toasts.push(toast)
    console.log(`[Toast Store] New toast added: [${variant.toUpperCase()}] ${title}: ${body}`)
    
    // Auto remove after 5 seconds
    setTimeout(() => {
      state.toasts = state.toasts.filter(t => t.id !== id)
      console.log(`[Toast Store] Toast removed: ${id}`)
    }, 5000)
  }

  const success = (body: string, title = 'Success') => showToast(title, body, 'success')
  const error = (body: string, title = 'Error') => showToast(title, body, 'danger')
  const warning = (body: string, title = 'Warning') => showToast(title, body, 'warning')
  const info = (body: string, title = 'Info') => showToast(title, body, 'info')

  return {
    state,
    success,
    error,
    warning,
    info,
  }
}
