<template>
  <BFormGroup v-bind="$attrs" class="t-form-group">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BFormGroup>
</template>

<style scoped lang="scss">
.t-form-group :deep(.col-form-label) {
  font-weight: 600;
  color: #4a5568;
  padding-bottom: 0.5rem;
  font-size: 0.875rem;
}
.t-form-group :deep(.form-text) {
  font-size: 0.8125rem;
  color: #718096;
  margin-top: 0.5rem;
}
</style>
