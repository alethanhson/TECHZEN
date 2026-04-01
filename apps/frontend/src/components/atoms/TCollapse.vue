<template>
  <BCollapse v-bind="$attrs" class="t-collapse">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BCollapse>
</template>

<style scoped>
.t-collapse {
  transition: height 0.35s ease-in-out;
}
</style>
