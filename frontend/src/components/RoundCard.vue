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
    font-family: 'Lato', sans-serif;;
    width: 450px;
    height: 450px; 
    background: linear-gradient(180deg, var(--primary-color) 0%, #000000 100%);
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center; 
    text-align: center; 
    font-size: 26px;
    color: white;
    padding: 32px;
    box-shadow: 0 0 17px rgba(0, 0, 0, 1);
  }
  </style>
  