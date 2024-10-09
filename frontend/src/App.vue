<script setup>

import NavBar from './components/NavBar.vue'
import { RouterView } from 'vue-router'

</script>

<template>
  <div style="display: flex; justify-content: center;">
    <div class="app-navbar">
      <NavBar />
    </div>
    <div class="app-content">
      <RouterView />
    </div>
  </div>
</template>

<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,800;1,800&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Lato:wght@100;400&family=Montserrat:ital,wght@0,800;1,800&display=swap');

:global(body) {
  background-color: #F5F5F5;
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
  width: 100%;
  margin-top: 75px;
}
</style>
