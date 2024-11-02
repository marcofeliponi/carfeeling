<template>
    <div class="main">
        <div class="header">
            <h1 class="title">{{ title }}</h1>
            <NIcon size="24" @click="closeModal" class="closeIcon">
                <Close />
            </NIcon>
        </div>
        <div class="content">
            <div class="reviews">
                <ul>
                    <li v-for="review in positiveReviews" :key="review">
                        {{ review }}
                    </li>
                </ul>
                <ul>
                    <li v-for="review in negativeReviews" :key="review">
                        {{ review }}
                    </li>
                </ul>
            </div>
            <div class="scrapedSites">
                <h3>Fontes usadas:</h3>
                <ul>
                    <li v-for="site in scrapedSites" :key="site">
                        <a :href="site" target="_blank">{{ site }}</a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
import { NIcon } from 'naive-ui';
import { Close } from '@vicons/ionicons5';

export default {
    name: 'CarAnalysis',

    components: {
        NIcon,
        Close
    },

    props: {
        title: {
            type: String,
            required: true
        },
        positiveReviews: {
            type: Array,
            required: true
        },
        negativeReviews: {
            type: Array,
            required: true
        },
        scrapedSites: {
            type: Array,
            required: true
        }
    },

    methods: {
        closeModal() {
            this.$emit('close-modal');
        }


    }
}
</script>

<style scoped lang="scss">
.main {
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    padding: 20px;
    margin: 0 auto;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 1000;
    width: 1100px;
    height: 650px;

    .header {
        display: flex;
        justify-content: center;
        align-items: center;
        font-family: 'Montserrat', sans-serif;
        font-size: 10px;
        color: var(--primary-color);

        .title {
            flex-grow: 1;
            text-align: center;
        }

        .closeIcon {
            cursor: pointer;
            margin-left: auto;
            margin-bottom: 40px;
        }
    }

    .content {
        overflow-y: auto;
        height: 90%;
    }

}
</style>