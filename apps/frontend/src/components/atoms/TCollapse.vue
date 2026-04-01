<template>
  <BCollapse v-bind="$attrs" class="t-collapse">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BCollapse>
</template>

<style scoped lang="scss">
.t-collapse {
  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}
</style>
