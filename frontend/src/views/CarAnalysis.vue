<template>
    <div class="main">
        <div v-if="loading">
            <h3 class="loading-message">Aguarde, estamos em alta velocidade para trazer seu resultado!</h3>
            <div class="loading-icon">
                <span>🏎️💨</span>
            </div>
        </div>
        <div v-else>
            <div class="title">
                <h1 v-html="dynamicTitle"></h1>
            </div>
            <div class="score-container">
                <div class="emoji">
                    <span v-if="score === 'VERY_BAD'">😡</span>
                    <span v-if="score === 'BAD'">😕</span>
                    <span v-if="score === 'REGULAR'">😐</span>
                    <span v-if="score === 'GOOD'">😊</span>
                    <span v-if="score === 'VERY_GOOD'">😍</span>
                    <span v-if="score === 'NO_SCORE'">🤔</span>
                </div>
                <div v-if="score !== 'NO_SCORE'" class="score">
                    <p>Nota Geral:</p>
                    <p :style="scoreColor">{{ analysis.score }} / 5</p>
                </div>
            </div>
            <div v-if="score !== 'NO_SCORE'" class="title" style="margin-top: 40px; font-size: 18px">
                <h3>O que as pessoas estão falando sobre {{ model }} {{ year }}:</h3>
            </div>
            <div class="reviews-container">
                <div class="positive-review" v-for="review in previewReviews.positives" :key="review">
                    <p>{{ formatReview(review) }}</p>
                </div>
                <div class="negative-review" v-for="review in previewReviews.negatives" :key="review">
                    <p>{{ formatReview(review) }}</p>
                </div>
            </div>
            <div v-if="score !== 'NO_SCORE'" class="footer">
                <NConfigProvider :themeOverrides="buttonThemes">
                    <n-button type="primary" round @click="openAnalysisModal">Visualizar análise completa</n-button>
                </NConfigProvider>
            </div>
            <div v-else class="no-data-footer">
                <NConfigProvider :themeOverrides="buttonThemes">
                    <n-button type="primary" round @click="goBackToHome">Voltar para a página inicial</n-button>
                </NConfigProvider>
            </div>
            <Modal v-if="isModalOpen" :title="`Análise completa do ${model} ${year}`" @close-modal="isModalOpen = false"
                :positiveReviews="analysis.positives" :negativeReviews="analysis.negatives"
                :neutralReviews="analysis.neutral" :scrapedSites="analysis.scraped_sites" :fipe-data="fipeData" />
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { NButton, NConfigProvider } from 'naive-ui';
import Modal from '../components/Modal.vue';
import { getFipeFromParallelum } from '../services/ParallelumFIPE_API';

export default {
    name: 'CarAnalysis',

    components: {
        NButton,
        NConfigProvider,
        Modal,
    },

    data() {
        return {
            loading: false,
            isModalOpen: false,
            brand: this.$route.query.brand,
            model: this.$route.query.model,
            year: this.$route.query.year,
            price: this.$route.query.price,
            analysis: {},
            buttonThemes: {
                common: {
                    primaryColorPressed: 'var(--primary-color)',
                    primaryColor: 'var(--primary-color)',
                    primaryColorHover: 'var(--primary-color)',
                },
                Button: {
                    textColor: 'white',

                }
            }
        }
    },

    async mounted() {
        this.loading = true;
        await this.getCarAnalysis();
        await this.getCarFipe();
        this.loading = false;
    },

    computed: {
        scoreColor() {
            if (this.score === 'VERY_BAD') {
                return 'color: red;';
            }
            if (this.score === 'BAD') {
                return 'color: orange;';
            }
            if (this.score === 'REGULAR') {
                return 'color: orange;';
            }
            if (this.score === 'GOOD') {
                return 'color: green;';
            }
            if (this.score === 'VERY_GOOD') {
                return 'color: green;';
            }

            return 'color: black;';
        },

        previewReviews() {
            if (this.score === 'VERY_BAD') {
                return {
                    negatives: this.analysis.negatives?.slice(0, 3),
                    positives: []
                }
            }
            if (this.score === 'BAD' || this.score === 'REGULAR') {
                return {
                    negatives: this.analysis.negatives?.slice(0, 2),
                    positives: this.analysis.positives?.slice(0, 1)
                }
            }
            if (this.score === 'GOOD') {
                return {
                    negatives: this.analysis.negatives?.slice(0, 1),
                    positives: this.analysis.positives?.slice(0, 2)
                }
            }
            if (this.score === 'VERY_GOOD') {
                return {
                    negatives: [],
                    positives: this.analysis.positives?.slice(0, 3)
                }
            }

            return {
                negatives: [],
                positives: []
            }
        },

        score() {
            if (this.analysis.score <= 2) {
                return 'VERY_BAD'
            }
            if (this.analysis.score <= 3) {
                return 'BAD'
            }
            if (this.analysis.score <= 3.5) {
                return 'REGULAR'
            }
            if (this.analysis.score <= 4.5) {
                return 'GOOD'
            }
            if (this.analysis.score >= 4.5) return 'VERY_GOOD'

            return 'NO_SCORE'
        },

        dynamicTitle() {
            if (this.score === 'VERY_BAD') {
                return '<span style="color: red;">A compra deste veículo não é aconselhável.</span>';
            }

            if (this.score === 'BAD') {
                return '<span style="color: orange;">Considere cuidadosamente antes de adquirir este veículo.</span>';
            }

            if (this.score === 'REGULAR') {
                return '<span style="color: orange;">A compra deste veículo pode ser válida, mas com alguns cuidados.</span>';
            }

            if (this.score === 'GOOD') {
                return '<span style="color: green;">Este veículo é uma boa opção para compra.</span>';
            }

            if (this.score === 'VERY_GOOD') {
                return '<span style="color: green;">Altamente recomendado: um excelente veículo para aquisição.</span>';
            }

            return '<span style="display: block; width: 50%; margin: 0 auto; text-align: justify; text-align-last: center;"> Desculpe, ainda não temos dados suficientes para analisar este veículo, tente novamente mais tarde.</span>';
        }
    },

    methods: {
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

        goBackToHome() {
            this.$router.push('/');
        },

        async getCarFipe() {
            const parallelumCarFipe = await getFipeFromParallelum(this.brand, this.model, this.year, this.formattedCarPrice(this.price));

            this.fipeData = parallelumCarFipe;
        },

        formattedCarPrice(carPrice) {
            const price = Number(carPrice).toLocaleString('pt-BR', {
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
            });

            return `R$ ${price}`;
        },

        openAnalysisModal() {
            this.isModalOpen = true;
        },

        async getCarAnalysis() {
            const queryParams = this.year ? `?year=${this.year}` : '';

            const response = await axios.get(`${import.meta.env.VITE_API_URL}/analysis/${this.model}${queryParams}`)
                .catch(error => {
                    console.log(error)
                })

            this.analysis = response.data?.analysis?.[0] || {};
        }
    }
}

</script>

<style scoped lang="scss">
.main {
    margin-top: 40px;
    color: black;

    .title {
        display: flex;
        justify-content: center;
        font-family: 'Montserrat', sans-serif;
    }

    .loading-message {
        display: flex;
        justify-content: center;
        font-family: 'Montserrat', sans-serif;
        font-size: 34px;
        margin-top: 110px;
        color: var(--secondary-color)
    }

    .loading-icon {
        display: flex;
        justify-content: center;
        font-size: 140px;
        margin-top: 50px;
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        animation: cruising 3s linear infinite;
    }

    @keyframes cruising {
        0% {
            transform: translateX(-50%);
            opacity: 1;
        }

        50% {
            transform: translateX(-60%);
            opacity: 0;
        }

        100% {
            transform: translateX(-50%);
            opacity: 1;
        }
    }

    .score-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        margin-top: 10px;
    }

    .emoji {
        font-size: 80px;
        margin-bottom: 10px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        animation: bounce 1.3s infinite;

        @keyframes bounce {

            0%,
            20%,
            50%,
            80%,
            100% {
                transform: translateY(0);
            }

            40% {
                transform: translateY(-30px);
            }

            60% {
                transform: translateY(-15px);
            }
        }
    }

    .score p {
        font-size: 28px;
        font-family: 'Montserrat', sans-serif;
        color: var(--primary-color);
    }

    .reviews-container {
        display: flex;
        justify-content: center !important;
        text-align: center;
        margin-top: 10px;

        .positive-review,
        .negative-review {
            padding: 30px;
            width: 80%;
            font-family: 'Montserrat', sans-serif;
            font-size: 16px;
        }

        .positive-review {
            color: green
        }

        .negative-review {
            color: red;
        }
    }

    .footer,
    .no-data-footer {
        display: flex;
        justify-content: center;
        font-family: 'Montserrat', sans-serif;
    }

    .no-data-footer {
        margin-top: 40px;
    }
}
</style>