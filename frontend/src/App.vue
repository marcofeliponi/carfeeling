<script setup>

import NavBar from './components/NavBar.vue'
import HomePage from './views/HomePage.vue'

</script>

<template>
  <div style="display: flex; justify-content: center;">
    <div class="app-navbar">
      <NavBar />
    </div>
    <div class="app-content">
      <HomePage />
    </div> 
  </div>
</template>

<style scoped lang="scss">
:global(body) {
  background-color: white;
}

.app-navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 75px;
  z-index: 100;
}

.app-content {
  display: flex;
  justify-content: center;
  width: 100%;
  height: 100%;
}
</style>
