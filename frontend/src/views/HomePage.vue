<template>
    <div class="home">
        <div>
            <h1 class="title">Bem-vindo ao Car Feeling!</h1>
            <h2 class="description">Simplificamos sua escolha automotiva.</h2>
            <h4 class="sub-description">
                Analisamos dados de especialistas e clientes reais<br> para oferecer resultados precisos com
                Inteligência Artificial.
            </h4>
        </div>
        <div class="start-button">
            <n-button style="width: 300px; height: 50px;" :loading="loading" color="#14213D" size="large"
                @click="start">
                Começar
            </n-button>
        </div>
        <div class="tire-footer">
            <img src="@/assets/tire.png" alt="Tire" class="tire-img" />
        </div>
    </div>
</template>

<script>

import { NButton } from 'naive-ui';

export default {
    name: 'HomePage',

    components: {
        NButton
    },

    data() {
        return {
            loading: false
        }
    },

    computed: {

    },

    methods: {
        start() {
            const tireImg = document.querySelector('.tire-img')
            tireImg.style.transform = 'rotate(360deg)'

            setTimeout(() => {
                this.$router.push('/car-consult')
            }, 1000)
        }
    }
};
</script>

<style scoped lang="scss">
.home {
    margin-top: 110px;
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

    .sub-description {
        margin-top: 10px;
        font-family: 'Lato', sans-serif;
        color: var(--secondary-color);
        font-size: 22px;
    }

    .start-button {
        margin-top: 80px;
        font-family: 'Montserrat', sans-serif;
    }

    .tire-footer {
        position: fixed;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        height: 45%;
        pointer-events: none;

        .tire-img {
            transition: transform 2.0s ease-in-out;
            width: 1000px;
        }
    }
}
</style>