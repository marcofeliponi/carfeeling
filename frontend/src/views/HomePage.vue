<template>
    <div class="home">
        <div>
            <h1 class="title">Bem-vindo ao Car Feeling!</h1>
            <h2 class="description">Clientes reais, avaliações reais.</h2>
        </div>
        <div class="round-card">
            <RoundCard text="Nossos resultados são gerados em uma análise através de Inteligência Artificial, com dados disponibilizados na Internet por especialistas e clientes reais." />        
        </div>
        <div class="arrow-button">
            <Icon style="cursor: pointer" color="black" size="100">
                <CaretDownSharp/>
            </Icon>
        </div>
    </div>
</template>

<script>

import RoundCard from '../components/RoundCard.vue';
import { CaretDownSharp } from '@vicons/ionicons5'
import { Icon } from '@vicons/utils'

export default {
    name: 'HomePage',

    components: {
        RoundCard,
        CaretDownSharp,
        Icon
    },

    data() {
    }
};
</script>

<style scoped lang="scss">
.home {
    margin-top: 80px;
    font-weight: bold;
    text-align: center;
    
    .title {
        font-family: 'Montserrat', sans-serif;
        color: black;
         font-size: 50px;
    }

    .description {
        font-family: 'Montserrat', sans-serif;
        color: var(--secondary-color);
        font-size: 27px;
    }
    
    .round-card {
        margin-top: 50px;
        display: flex;
        justify-content: center;
    }

    .arrow-button {
        margin-top: 15px;
        display: flex;
        justify-content: center;
        animation-name: floating;
        animation-duration: 3s;
        animation-iteration-count: infinite;
        animation-timing-function: ease-in-out;

        @keyframes floating {
            from { transform: translate(0,  0px); }
            65%  { transform: translate(0, 30px); }
            to   { transform: translate(0, -0px); }    
        }    }
}
</style>