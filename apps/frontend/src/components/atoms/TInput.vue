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
interface Props {
  id?: string
  label?: string
  feedback?: string
  state?: boolean | null
}

const props = withDefaults(defineProps<Props>(), {
  id: () => `t-input-${Math.random().toString(36).substring(2, 9)}`,
  state: null
})
</script>

<style scoped lang="scss">
.t-label {
  font-weight: 600;
  color: #4a5568;
  font-size: 0.875rem;
  margin-bottom: 0.5rem;
  display: block;
}

.t-input {
  border-radius: 10px;
  background-color: #f8fafc;
  border: 1px solid #e2e8f0;
  padding: 0.625rem 1rem;
  transition: all 0.2s ease;

  &:focus {
    background-color: #ffffff;
    border-color: #2E5BFF;
    box-shadow: 0 0 0 4px rgba(46, 91, 255, 0.1);
    outline: none;
  }

  &.is-invalid {
    border-color: #ef4444;
    &:focus {
      box-shadow: 0 0 0 4px rgba(239, 68, 68, 0.1);
    }
  }
}

.t-feedback {
  display: block;
  font-size: 0.75rem;
  margin-top: 0.375rem;
  font-weight: 500;
}
</style>
