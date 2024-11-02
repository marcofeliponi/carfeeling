<template>
    <div class="navbar">
        <div class="app-logo" @click="goToHome()">
            <img src="@/assets/logo.png" alt="app-logo">
        </div>
    </div>
</template>

<script>

export default {
    name: 'NavBar',

    data() {
        return {
        }
    },

    computed: {
        actualPage() {
            return this.$route.name;
        }
    },

    methods: {
        goToHome() {
            this.$router.push('/');
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
        height: 30px;
        cursor: pointer;
    }
}
</style>