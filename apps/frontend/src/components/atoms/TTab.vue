<template>
  <BTab v-bind="$attrs" class="t-tab">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BTab>
</template>

<style scoped>
.t-tab {
  transition: opacity 0.3s ease;
}
</style>
