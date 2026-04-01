<template>
  <BCarouselSlide v-bind="$attrs" class="t-carousel-slide">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BCarouselSlide>
</template>

<style scoped lang="scss">
.t-carousel-slide :deep(.carousel-caption) {
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 18px;
  padding: 1.75rem;
  bottom: 2rem;
  left: 10%;
  right: 10%;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  color: #1a202c;
  text-align: left;
}

.t-carousel-slide :deep(.carousel-caption h3) {
  font-weight: 700;
  margin-bottom: 0.75rem;
  font-size: 1.75rem;
  letter-spacing: -0.02em;
  color: #1a202c;
}

.t-carousel-slide :deep(.carousel-caption p) {
  font-weight: 500;
  margin-bottom: 0;
  color: #4a5568;
  line-height: 1.6;
}
</style>
