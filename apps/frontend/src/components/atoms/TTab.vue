<template>
  <BTab v-bind="$attrs" class="t-tab">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BTab>
</template>

<style scoped lang="scss">
.t-tab {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
</style>
