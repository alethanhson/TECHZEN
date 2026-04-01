<template>
  <BImg v-bind="$attrs" class="t-img" />
</template>

<style scoped lang="scss">
.t-img {
  border-radius: 14px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
  transition: all 0.3s ease;
  object-fit: cover;
  
  &:hover {
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
  }
}
</style>
