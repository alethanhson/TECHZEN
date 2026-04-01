<template>
  <BFormCheckboxGroup v-bind="$attrs" class="t-checkbox-group">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BFormCheckboxGroup>
</template>

<style scoped>
.t-checkbox-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
.t-checkbox-group[stacked="false"] {
  flex-direction: row;
  gap: 1.5rem;
}
</style>
