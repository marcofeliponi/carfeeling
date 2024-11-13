<template>
    <div class="home">
        <div>
            <h1 class="title">Bem-vindo ao Car Feeling!</h1>
            <h2 class="description">Simplificamos sua escolha automotiva.</h2>
            <h4 class="sub-description">
                Utilizamos Inteligência Artificial e Web Scraping para analisar dados da internet, coletando opiniões de
                especialistas e consumidores sobre carros nacionais e oferecendo insights que ajudam na sua decisão.
            </h4>
        </div>
        <div class="consult-button">
            <n-button style="width: 400px; height: 50px;" :loading="loading" color="#14213D" size="large"
                @click="start('consult')">
                Consultar Análise da Inteligência Artificial
            </n-button>
        </div>
        <div class="chat-button">
            <n-button style="background-color: var(--secondary-color); width: 400px; height: 50px;" :loading="loading"
                color="#14213D" size="large" @click="start('chat')">
                Conversar com a Inteligência Artificial
            </n-button>
        </div>
        <div class="tire-footer">
            <img src="@/assets/tire.png" alt="Tire" class="tire-img" />
        </div>
    </div>
</template>

<script>

import { NButton } from 'naive-ui';
import axios from 'axios';

export default {
    name: 'HomePage',

    components: {
        NButton,
    },

    data() {
        return {
            loading: false
        }
    },

    computed: {

    },

    methods: {
        async getBrands() {
            try {
                const response = await axios.get(`${import.meta.env.VITE_API_URL}/brands`);

                return response.data.brands;
            } catch (error) {
                console.error(error);
            }
        },

        async getCars() {
            try {
                const response = await axios.get(`${import.meta.env.VITE_API_URL}/cars`);

                return response.data.cars;
            } catch (error) {
                console.error(error);
            }
        },

        async start(type) {
            const tireImg = document.querySelector('.tire-img')

            tireImg.classList.add('spinning');

            const [brands, cars] = await Promise.all([
                this.getBrands(), this.getCars()
            ]);

            this.$store.setCars(cars);
            this.$store.setBrands(brands);

            this.$router.push({
                path: '/car-consult',
                query: {
                    type,
                }
            })

            tireImg.classList.remove('spinning');
        }
    }
};
</script>

<style scoped lang="scss">
.home {
    margin-top: 70px;
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

    .consult-button {
        margin-top: 50px;
        font-family: 'Montserrat', sans-serif;
    }

    .chat-button {
        margin-top: 30px;
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
            transition: transform 1.0s ease-in-out;
            width: 1000px;
        }

        .spinning {
            animation: spin 1s linear infinite;
        }

        @keyframes spin {
            from {
                transform: rotate(0deg);
            }

            to {
                transform: rotate(360deg);
            }
        }
    }
}
</style>