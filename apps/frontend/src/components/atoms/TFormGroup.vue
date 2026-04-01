<template>
  <BFormGroup v-bind="$attrs" class="t-form-group">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BFormGroup>
</template>

<style scoped>
.t-form-group :deep(.col-form-label) {
  font-weight: 600;
  color: #334155;
  padding-bottom: 0.5rem;
}
.t-form-group :deep(.form-text) {
  font-size: 13px;
  color: #64748b;
  margin-top: 0.5rem;
}
</style>
