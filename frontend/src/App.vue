<script setup>

import NavBar from './components/NavBar.vue'

</script>

<template>
  <div class="app-navbar">
    <NavBar />
  </div>

</template>

<style scoped lang="scss">
.app-navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 100;
}
</style>
