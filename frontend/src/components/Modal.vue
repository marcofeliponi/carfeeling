<template>
    <div class="modal-overlay">
        <div class="modal-content">
            <div class="header">
                <NIcon v-if="view === 'comparison'" size="24" @click="view = 'analysis'" class="action-icon">
                    <ArrowBack />
                </NIcon>
                <h1 class="title">{{ title }}</h1>
                <NIcon size="24" @click="closeModal" class="action-icon">
                    <Close />
                </NIcon>
            </div>
            <div v-if="view === 'analysis'" class="content">
                <div class="car-fipe">
                    <h3 class="fipe-title">{{ fipeTitle }}</h3>
                    <p class="fipe-value">{{ fipeData.price }}</p>
                    <p v-if="fipeData.warning" class="fipe-warning">{{ fipeData.warning }}</p>
                </div>
                <div class="reviews">
                    <ul>
                        <h3 class="positive-reviews-title">Comentários positivos:</h3>
                        <li v-for="review in positiveReviews" :key="review" class="review-item">
                            <NIcon style="margin-right: 20px" size="14">
                                <Person />
                            </NIcon>
                            {{ formatReview(review) }}
                        </li>
                        <span v-if="!positiveReviews.length" class="no-review">Sem comentários positivos mantidos pela
                            Inteligência
                            Artificial.</span>
                    </ul>
                    <ul>
                        <h3 class="negative-reviews-title">Comentários negativos:</h3>
                        <li v-for="review in negativeReviews" :key="review" class="review-item">
                            <NIcon style="margin-right: 20px" size="14">
                                <Person />
                            </NIcon>
                            {{ formatReview(review) }}
                        </li>
                        <span v-if="!negativeReviews.length" class="no-review">Sem comentários negativos mantidos pela
                            Inteligência
                            Artificial.</span>
                    </ul>
                    <ul>
                        <h3 class="neutral-reviews-title">Comentários neutros:</h3>
                        <li v-for="review in neutralReviews" :key="review" class="review-item">
                            <NIcon style="margin-right: 20px" size="14">
                                <Person />
                            </NIcon>
                            {{ formatReview(review) }}
                        </li>
                        <span v-if="!neutralReviews.length" class="no-review">Sem comentários neutros mantidos pela
                            Inteligência
                            Artificial.</span>
                    </ul>
                </div>
                <div class="scraped-sites">
                    <h3>Fontes usadas nesta análise:</h3>
                    <ul>
                        <li v-for="site in scrapedSites" :key="site" class="site-item">
                            <NIcon style="cursor: pointer; margin-right: 20px" size="14">
                                <a :href="site" target="_blank"></a>
                                <OpenOutline />
                            </NIcon>
                            <a :href="site" target="_blank" class="link">{{ site }}</a>
                        </li>
                    </ul>
                </div>
                <div class="compare-car-button">
                    <NConfigProvider :themeOverrides="buttonThemes">
                        <n-button size="large" type="primary" round @click="view = 'comparison'">Clique para comparar
                            com carros da mesma faixa de preço</n-button>
                    </NConfigProvider>
                </div>
            </div>
            <div v-if="view === 'comparison'">
                <div v-if="!carComparison?.scores?.length">
                    <h3 class="no-comparison-data">Ainda não temos dados suficientes para comparar este carro...<br>:(
                    </h3>
                </div>
                <div v-else class="comparison-data">
                    <div class="main-car">
                        <h3>{{ mainCar.model }}</h3>
                        <p style="font-family: 'Lato', sans-serif; font-size: 18px;">Preço: {{
                            formattedCarPrice(mainCar.price) }}</p>
                        <StarRating style="display: flex; justify-content: center;" :value="mainCar.score" />
                    </div>

                    <h3 style="color: var(--secondary-color); margin-top: 50px;">Clique em um modelo abaixo para
                        realizar uma
                        consulta detalhada:
                    </h3>
                    <div class="comparison-cars">
                        <div v-for="car in carComparison.scores" :key="car.model" class="comparison-item"
                            @click="consultComparisonCar(car)">
                            <h3>{{ car.model }}</h3>
                            <p style="font-size: 18px;">Preço: {{ formattedCarPrice(car.price) }}</p>
                            <StarRating :value="car.score" />
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import { NIcon, NConfigProvider, NButton } from 'naive-ui';
import { ArrowBack, Close, OpenOutline, Person } from '@vicons/ionicons5';
import StarRating from './StarRating.vue';

export default {
    name: 'CarAnalysis',

    components: {
        NIcon,
        Close,
        Person,
        OpenOutline,
        NConfigProvider,
        NButton,
        ArrowBack,
        StarRating
    },

    data() {
        return {
            buttonThemes: {
                common: {
                    primaryColorPressed: 'var(--primary-color)',
                    primaryColor: 'var(--primary-color)',
                    primaryColorHover: 'var(--primary-color)',
                },
                Button: {
                    textColor: 'white',
                }
            },
            view: 'analysis',
        }
    },

    props: {
        positiveReviews: {
            type: Array,
            required: true,
            default: () => []
        },
        negativeReviews: {
            type: Array,
            required: true,
            default: () => []
        },
        neutralReviews: {
            type: Array,
            required: true,
            default: () => []
        },
        scrapedSites: {
            type: Array,
            required: true,
            default: () => []
        },
        fipeData: {
            type: Object,
            required: true,
            default: () => ({})
        },
        carComparison: {
            type: Object,
            required: true,
            default: () => ({})
        },
        mainCar: {
            type: Object,
            required: true,
            default: () => ({})
        }
    },

    computed: {
        fipeTitle() {
            return this.fipeData?.date ? `Valor FIPE em ${this.fipeData.date}` : 'Valor FIPE';
        },

        title() {
            if (this.view === 'comparison') {
                return `Comparação de carros da mesma faixa de preço`;
            }

            return `Análise completa do ${this.mainCar.model} ${this.mainCar.year}`
        }
    },

    methods: {
        consultComparisonCar(car) {
            this.closeModal();
            this.$emit('consult-comparison-car', car);
        },

        formattedCarPrice(carPrice) {
            const priceNumber = Number(carPrice);

            if (isNaN(priceNumber)) return carPrice;

            const price = priceNumber.toLocaleString('pt-BR', {
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
            });

            return `R$ ${price}`;
        },

        closeModal() {
            this.$emit('close-modal');
        },

        formatReview(review) {
            const toRemove = ['Pontos positivos:', 'Pontos negativos:', 'Comentários:'];

            toRemove.forEach(word => {
                review = review.replace(word, ' ').trim();
            });

            if (
                (review.startsWith('"') && review.endsWith('"')) ||
                (review.startsWith("“") && review.endsWith("”")) ||
                (review.startsWith("'") && review.endsWith("'"))
            ) {
                review = review.slice(1, -1);
            }

            if (review[0] !== review[0].toUpperCase()) {
                review = review[0].toUpperCase() + review.slice(1);
            }

            return `"${review}"`;
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

            .action-icon {
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

            .fipe-warning {
                margin-top: 10px;
                font-size: 14px;
                color: black;
                max-width: 50%;
                text-align: center;
            }
        }

        .reviews {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            margin-top: 20px;

            .no-review {
                display: flex;
                justify-content: center;
                color: black;
            }

            ul {
                list-style-type: none;
                padding: 0;
                margin: 0;
                width: 70%;

                .positive-reviews-title,
                .negative-reviews-title,
                .neutral-reviews-title {
                    font-family: 'Montserrat', sans-serif;
                    font-size: 20px;
                    color: var(--primary-color);
                    margin-bottom: 20px;
                    text-align: center;
                    margin-top: 10px;
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
                }

                .neutral-reviews-title {
                    color: #808080;
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
            margin-top: 50px;

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

        .compare-car-button {
            display: flex;
            justify-content: center;
            margin-top: 50px;
            margin-bottom: 50px;
            font-family: 'Montserrat', sans-serif;
        }

        .no-comparison-data {
            font-family: 'Montserrat', sans-serif;
            font-size: 20px;
            color: var(--secondary-color);
            text-align: center;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }

        .comparison-data {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 40px;
        }

        .main-car {
            text-align: center;
            margin-bottom: 20px;
        }

        .comparison-cars {
            display: flex;
            margin-top: 40px;
            gap: 120px;
            justify-content: center;
        }

        .comparison-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            font-family: 'Lato', sans-serif;
            cursor: pointer;
        }

        h3 {
            font-family: 'Montserrat', sans-serif;
            font-size: 20px;
            color: var(--primary-color);
        }
    }
}
</style>