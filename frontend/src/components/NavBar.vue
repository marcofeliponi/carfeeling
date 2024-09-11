<template>
    <div class="navbar">
        <div class="app-logo">
            <Icon color="white" size="48">
                <CarOutline />
            </Icon>
        </div>
        <div class="hamburger-button">
            <Icon class="menu-icon" color="white" size="40" @click="openMenu">
                <MenuOutline>
                </MenuOutline>
            </Icon>
        </div>
    </div>
</template>

<script>
import { CarOutline, MenuOutline } from '@vicons/ionicons5'
 import { Icon } from '@vicons/utils'

export default {
    name: 'NavBar',

    components: {
        CarOutline,
        Icon,
        MenuOutline
    },

    methods: {
        openMenu() {
            console.log('menu opened')
        }
    }
}
</script>

<style scoped lang="scss">
.navbar {
    width: 100%;
    height: 100%;
    background-color: var(--primary-color);
    display: flex;
    align-items: center;

    .app-logo {
        width: 50%;
        height: 50%;
        display: flex;
        justify-content: end;
    }

    .hamburger-button {
        width: 50%;
        height: 50%;
        display: flex;
        justify-content: end;
        margin-right: 10px;

        .menu-icon {
            cursor: pointer;
        }
    }

}
</style>