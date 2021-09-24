<template>
  <div class="pill">
    <span>
      <slot/>
    </span>
  </div>
</template>

<script>
export default {
  props: {
  }
}
</script>

<style lang="scss">
.pill {
  padding: 4px 8px;
  display: inline-block;
  background: #4fc3f7;
  border-radius: 128px;
}
</style>