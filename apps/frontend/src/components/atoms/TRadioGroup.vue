<template>
  <BFormRadioGroup v-bind="$attrs" class="t-radio-group">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BFormRadioGroup>
</template>

<style scoped>
.t-radio-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
.t-radio-group[stacked="false"] {
  flex-direction: row;
  gap: 1.5rem;
}
</style>
