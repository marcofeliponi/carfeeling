<template>
    <div class="circle-card">
      <p>{{ text }}</p>
    </div>
  </template>
  
  <script>
  export default {
    name: "RoundCard",
    props: {
      text: {
        type: String,
        default: "Insira um texto",
      },
    },
  };
  </script>
  
  <style scoped lang="scss">
  .circle-card {
    width: 450px;
    height: 450px; 
    background-color: var(--primary-color); 
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center; 
    text-align: center; 
    font-size: 26px;
    color: white;
    padding: 32px;
    border: var(--border-color) 2px solid;
  }
  </style>
  