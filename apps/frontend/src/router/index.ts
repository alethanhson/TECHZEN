import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior: () => ({ top: 0 }),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue'),
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/RegisterView.vue'),
    },
    {
      path: '/products',
      name: 'products',
      component: () => import('../views/ProductCrud.vue'),
      meta: { requiresAuth: true, requiresAdmin: true }
    },
    {
      path: '/products/create',
      name: 'product-create',
      component: () => import('../views/ProductForm.vue'),
      meta: { requiresAuth: true, requiresAdmin: true }
    },
    {
      path: '/products/:id/edit',
      name: 'product-edit',
      component: () => import('../views/ProductForm.vue'),
      meta: { requiresAuth: true, requiresAdmin: true }
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: () => import('../views/AdminDashboard.vue'),
      meta: { requiresAuth: true, requiresAdmin: true }
    },
  ],
})

// eslint-disable-next-line @typescript-eslint/no-explicit-any
router.beforeEach((to: any) => {
  const token = localStorage.getItem('access_token')

  if (to.meta.requiresAuth && !token) {
    return { name: 'login' }
  }

  if (to.meta.requiresAdmin) {
    const userStr = localStorage.getItem('user')
    try {
      const user = userStr ? JSON.parse(userStr) : null

      const isAdmin = user && (user.is_superuser === true || (user.role && user.role.toLowerCase() === 'admin'))

      if (!isAdmin) {
        if (to.name === 'home') return true
        return { name: 'home' }
      }
    } catch (e) {
      return { name: 'login' }
    }
  }
})

export default router
