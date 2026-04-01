<template>
  <BModal v-bind="$attrs" class="t-modal" :header-bg-variant="headerBgVariant" :header-text-variant="headerTextVariant">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BModal>
</template>

<script setup lang="ts">
import type { ColorVariant, TextColorVariant } from 'bootstrap-vue-next'

interface Props {
  headerBgVariant?: ColorVariant | null
  headerTextVariant?: TextColorVariant | null
}

withDefaults(defineProps<Props>(), {
  headerBgVariant: 'light',
  headerTextVariant: 'dark'
})
</script>

<style scoped lang="scss">
.t-modal :deep(.modal-content) {
  border-radius: 20px;
  border: none;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
  overflow: hidden;
  background: white;
}

.t-modal :deep(.modal-header) {
  border-bottom: 1px solid rgba(0, 0, 0, 0.03);
  padding: 1.25rem 1.75rem;
  
  &.bg-primary {
    background: linear-gradient(135deg, #2E5BFF 0%, #6610f2 100%) !important;
  }
}

.t-modal :deep(.modal-title) {
  font-weight: 700;
  letter-spacing: -0.01em;
  font-size: 1.25rem;
}

.t-modal :deep(.modal-body) {
  padding: 2rem 1.75rem;
  color: #4a5568;
  line-height: 1.6;
}

.t-modal :deep(.modal-footer) {
  border-top: 1px solid rgba(0, 0, 0, 0.03);
  padding: 1.25rem 1.75rem;
  background-color: #f8fafc;
}
</style>
