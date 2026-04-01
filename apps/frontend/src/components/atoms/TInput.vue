<template>
  <div class="t-input-group mb-3">
    <label v-if="label" :for="id" class="form-label t-label">{{ label }}</label>
    <BFormInput
      v-bind="$attrs"
      :id="id"
      class="t-input"
      :state="state"
    />
    <div v-if="feedback" class="t-feedback" :class="{ 'invalid-feedback': state === false, 'valid-feedback': state === true }">
      {{ feedback }}
    </div>
  </div>
</template>

<script setup lang="ts">
import type { BaseFormInputProps } from 'bootstrap-vue-next'

interface Props extends /* @vue-ignore */ BaseFormInputProps {
  id?: string
  label?: string
  feedback?: string
  state?: boolean | null
}

withDefaults(defineProps<Props>(), {
  id: () => `t-input-${Math.random().toString(36).substr(2, 9)}`,
  state: null
})

</script>

<style scoped>
.t-label {
  font-weight: 600;
  color: #374151;
  font-size: 14px;
  margin-bottom: 4px;
}

.t-input {
  border-radius: 6px;
  background-color: #f9fafb;
}

.t-input:focus {
  background-color: #ffffff;
  box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.1);
}

.t-feedback {
  display: block;
  font-size: 12px;
  margin-top: 4px;
}
</style>
