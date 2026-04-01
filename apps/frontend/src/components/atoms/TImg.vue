<template>
  <BImg v-bind="$attrs" class="t-img" />
</template>

<style scoped>
.t-img {
  border-radius: 12px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
  transition: opacity 0.3s ease;
}

.t-img:not([rounded="0"]) {
  border-radius: 12px;
}
</style>
