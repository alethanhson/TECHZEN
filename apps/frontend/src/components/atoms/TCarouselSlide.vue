<template>
  <BCarouselSlide v-bind="$attrs" class="t-carousel-slide">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BCarouselSlide>
</template>

<style scoped>
.t-carousel-slide :deep(.carousel-caption) {
  background: rgba(30, 41, 59, 0.4);
  backdrop-filter: blur(8px);
  border-radius: 12px;
  padding: 1.5rem;
  bottom: 1.5rem;
  left: 5%;
  right: 5%;
}
.t-carousel-slide :deep(.carousel-caption h3) {
  font-weight: 800;
  margin-bottom: 0.5rem;
  font-size: 1.5rem;
}
.t-carousel-slide :deep(.carousel-caption p) {
  font-weight: 500;
  margin-bottom: 0;
  opacity: 0.9;
}
</style>
