<template>
    <div class="modal-overlay">
        <div class="modal-content">
            <div class="header">
                <h1 class="title">{{ title }}</h1>
                <NIcon size="24" @click="closeModal" class="close-icon">
                    <Close />
                </NIcon>
            </div>
            <div class="content">
                <div class="car-fipe">
                    <h3 class="fipe-title">Valor médio FIPE em 2024:</h3>
                    <p class="fipe-value">{{ formattedCarPrice }}</p>
                </div>
                <div class="reviews">
                    <ul>
                        <h3 class="positive-reviews-title">Comentários positivos:</h3>
                        <li v-for="review in positiveReviews" :key="review" class="review-item">
                            <NIcon style="margin-right: 20px" size="14">
                                <Person />
                            </NIcon>
                            {{ review }}
                        </li>
                        <span v-if="!positiveReviews.length">Sem comentários positivos mantidos pela Inteligência
                            Artificial.</span>
                    </ul>
                    <ul>
                        <h3 class="negative-reviews-title">Comentários negativos:</h3>
                        <li v-for="review in negativeReviews" :key="review" class="review-item">
                            <NIcon style="margin-right: 20px" size="14">
                                <Person />
                            </NIcon>
                            {{ review }}
                        </li>
                        <span v-if="!negativeReviews.length">Sem comentários negativos mantidos pela Inteligência
                            Artificial.</span>
                    </ul>
                </div>
                <div class="scraped-sites">
                    <h3>Fontes usadas:</h3>
                    <ul>
                        <li v-for="site in scrapedSites" :key="site" class="site-item">
                            <NIcon  style="cursor: pointer; margin-right: 20px" size="14">
                                <a :href="site" target="_blank"></a>
                                <OpenOutline />
                            </NIcon>
                            <a :href="site" target="_blank" class="link">{{ site }}</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import { NIcon } from 'naive-ui';
import { Close, OpenOutline, Person } from '@vicons/ionicons5';

export default {
    name: 'CarAnalysis',

    components: {
        NIcon,
        Close,
        Person,
        OpenOutline
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
        },
        carPrice: {
            type: String,
            required: true
        }
    },

    computed: {
        formattedCarPrice() {
            const price = Number(this.carPrice).toLocaleString('pt-BR', {
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
            });

            return `R$ ${price}`;
        }
    },

    methods: {
        closeModal() {
            this.$emit('close-modal');
        },
    }
}
</script>

<style scoped lang="scss">
.modal-overlay {
    background-color: rgba(0, 0, 0, 0.6);
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1000;
    display: flex;
    justify-content: center;
    align-items: center;

    .modal-content {
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
            font-size: 11px;
            color: var(--primary-color);

            .title {
                flex-grow: 1;
                text-align: center;
            }

            .close-icon {
                cursor: pointer;
                margin-left: auto;
                margin-bottom: 40px;
            }
        }

        .content {
            overflow-y: auto;
            height: 90%;
        }

        .car-fipe {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 40px;
            margin-bottom: 40px;
            font-family: 'Montserrat', sans-serif;

            .fipe-title {
                font-size: 20px;
                color: var(--primary-color);
            }

            .fipe-value {
                font-size: 30px;
                color: var(--secondary-color);
            }
        }

        .reviews {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            margin-top: 20px;

            ul {
                list-style-type: none;
                padding: 0;
                margin: 0;
                width: 70%;

                .positive-reviews-title,
                .negative-reviews-title {
                    font-family: 'Montserrat', sans-serif;
                    font-size: 20px;
                    color: var(--primary-color);
                    margin-bottom: 20px;
                    text-align: center;
                }

                li {
                    font-family: 'Lato', sans-serif;
                    font-size: 16px;
                    margin-bottom: 50px;
                }

                span {
                    font-family: 'Lato', sans-serif;
                    font-size: 16px;
                    color: var(--secondary-color);
                }

                .positive-reviews-title {
                    color: green;
                }

                .negative-reviews-title {
                    color: red;
                    margin-top: 30px;
                }

                .review-item {
                    display: flex;
                    align-items: center;
                }
            }
        }

        .scraped-sites {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 20px;
            
            h3 {
                font-size: 20px;
                color: var(--secondary-color);
                font-family: 'Montserrat', sans-serif;
                margin-bottom: 20px;
            }

            ul {
                list-style-type: none;
                padding: 0;
                margin: 0;
                width: 70%;

                li {
                    font-family: 'Lato', sans-serif;
                    font-size: 16px;
                    margin-bottom: 20px;
                }

                a {
                    color: var(--primary-color);
                }
            }

            .site-item {
                display: flex;
                align-items: center;

                .link {
                    &:hover {
                        text-decoration: underline;
                    }
                }
            }
        }
    }
}
</style>