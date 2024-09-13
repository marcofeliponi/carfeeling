<template>
    <div class="home">
        <div class="description">
            <h1 style="color: var(--text-color); font-size: 50px;">Bem-vindo ao Car Feeling!</h1>
            <h2 style="color: black">Tenha acesso à diversas avaliações de clientes reais sobre veículos de seu interesse.</h2>
        </div>
        <div class="round-card">
            <RoundCard text="Nossos resultados são gerados em uma análise através de Inteligência Artificial, com dados disponibilizados na Internet por especialistas e clientes reais." />        
        </div>
        <div class="arrow-button">
            <Icon style="cursor: pointer" color="#408507" size="100">
                <ArrowDown/>
            </Icon>
        </div>
    </div>
</template>

<script>

import RoundCard from '../components/RoundCard.vue';
import { ArrowDown } from '@vicons/ionicons5'
import { Icon } from '@vicons/utils'

export default {
    name: 'HomePage',

    components: {
        RoundCard,
        ArrowDown,
        Icon
    },

    data() {
    }
};
</script>

<style scoped lang="scss">
.home {
    margin-top: 90px;
    
    .description {
        text-align: center;
        font-family: 'Roboto', sans-serif;
        font-weight: bold;
    }
    
    .round-card {
        margin-top: 40px;
        display: flex;
        justify-content: center;
    }

    .arrow-button {
        margin-top: 25px;
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