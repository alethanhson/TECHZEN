# Vue 3 Composition API Cheat Sheet

## 1. Modern API Setup
### Composition API with `<script setup>`
```vue
<script setup lang="ts">
import { ref, reactive, computed, watch, onMounted } from 'vue'

// Basic Reactive Variables
const count = ref(0) // Used for primitives: string, number, boolean
const user = reactive({ name: 'Thanh Son', age: 25 }) // Used for objects/arrays

// Derived State
const doubleCount = computed(() => count.value * 2)

// Functions (Methods)
const increment = () => {
  count.value++
}

// Watchers
watch(count, (newVal, oldVal) => {
  console.log(`Count changed from ${oldVal} to ${newVal}`)
})

// Deep Watch
watch(() => user.name, (newVal) => {
  console.log('Username changed to', newVal)
}, { deep: true, immediate: true })

// Lifecycle Hooks
onMounted(() => {
  console.log('Component is now mounted!')
})
</script>

<template>
  <div class="p-4">
    <h1>{{ user.name }}'s Counter</h1>
    <p>Count: {{ count }} (Double: {{ doubleCount }})</p>
    <button @click="increment" class="btn btn-primary">Increment</button>
  </div>
</template>
```

## 2. Component Communication
### Props and Emits
```vue
<script setup lang="ts">
// Props 정의
const props = defineProps<{
  title: string
  items: string[]
  active?: boolean // Optional prop
}>()

// Emits 정의
const emit = defineEmits<{
  (e: 'update:active', value: boolean): void
  (e: 'submit', id: number): void
}>()

const handleClick = () => {
  emit('submit', 42)
  emit('update:active', !props.active)
}
</script>
```

## 3. Template Refs (Accessing DOM/Components)
```vue
<script setup lang="ts">
import { ref, onMounted } from 'vue'

const inputRef = ref<HTMLInputElement | null>(null)

onMounted(() => {
  inputRef.value?.focus()
})
</script>

<template>
  <input ref="inputRef" type="text" />
</template>
```

## 4. Provide / Inject (State management)
```vue
// Parent.vue
<script setup>
import { provide, ref } from 'vue'
const theme = ref('dark')
provide('themeKey', theme)
</script>

// Child.vue
<script setup>
import { inject } from 'vue'
const theme = inject('themeKey', 'light') // 'light' is default value
</script>
```

## 5. Composables (Reusable logic)
```ts
// useCounter.ts
import { ref } from 'vue'

export function useCounter(initialValue = 0) {
  const count = ref(initialValue)
  const increment = () => count.value++
  const decrement = () => count.value--
  
  return { count, increment, decrement }
}

// In Component:
const { count, increment } = useCounter(10)
```

## 6. Vue Router 4
```ts
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

// Programmatic navigation
const goToHome = () => {
  router.push({ name: 'Home' })
}

// Accessing params
const userId = route.params.id
```

## 7. Axios + Vue 3 Fetch Pattern
```ts
import axios from 'axios'
import { ref } from 'vue'

const items = ref([])
const loading = ref(false)
const error = ref(null)

const fetchItems = async () => {
  loading.value = true
  try {
    const response = await axios.get('/api/items')
    items.value = response.data
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
}
```
