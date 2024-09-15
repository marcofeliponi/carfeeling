<template>
    <div class="navbar">
        <div class="app-logo">
            <img src="@/assets/logo.png" alt="app-logo">
        </div>
        <div class="buttons" v-for="(value, key) in pages" :key="key">
            <NConfigProvider :themeOverrides="buttonThemes">
                <n-button 
                    :quaternary="page === key ? false : true" 
                    @click="goTo(key)"
                >
                    {{ value }}
                </n-button>
            </NConfigProvider>
        </div>
    </div>
</template>

<script>

import { NButton, NConfigProvider } from 'naive-ui';

export default {
    name: 'NavBar',

    components: {
        NButton,
        NConfigProvider,
    },

    data() {
        return {
            page: 'home',
            pages: {
                about: 'Saiba mais',
                home: 'Início',
                contact: 'Contato'
            },
            buttonThemes: {
                common: {
                    primaryColorHover: 'white',
                    primaryColorPressed: 'white',
                },
                Button: {
                    textColor: 'white',
                }
            }
        }
    },

    methods: {
        goTo(page) {
            console.log('goTo');
            this.page = page;
        }
    }
}
</script>

<style scoped lang="scss">
.navbar {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.8);
    border-bottom-left-radius: 18px;
    border-bottom-right-radius: 18px;
    background: linear-gradient(180deg, #000000 0%, var(--primary-color) 100%);
    
    .app-logo {
        display: flex;
        margin-left: 50px;
        left: 0;
        height: 30px;
        position: absolute;
    }

    .buttons {
        font-family: 'Montserrat', sans-serif;
        display: flex;
        justify-content: space-around;
        width: 10%;
    }
}
</style>