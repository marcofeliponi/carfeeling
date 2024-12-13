<template>
    <div class="main">
        <div v-if="type === 'chat' && notAuthenticated">
            <div class="title">
                <h1>Para prosseguir é necessário autenticar-se com o Google:</h1>
            </div>
            <GoogleLogin style="display: flex; justify-content: center"
                :clientId="googleClientId"
                :callback="onSuccess" :error="onFailure" :buttonConfig="{ size: 'large' }" />
        </div>
        <div v-else>
            <div class="title">
                <h1>{{ title }}</h1>
            </div>
            <div class="inputs">
                <div class="input-group">
                    <p>Marca*</p>
                    <NConfigProvider :themeOverrides="theme">
                        <n-select v-model:value="selectedBrand" filterable placeholder="Selecione uma marca"
                            :options="brands" size="large" @click="validateInputs('brands')" />
                    </NConfigProvider>
                </div>
                <div class="input-group">
                    <p>Modelo*</p>
                    <NConfigProvider :themeOverrides="theme">
                        <n-select v-model:value="selectedModel" filterable :disabled="!selectedBrand"
                            placeholder="Selecione um modelo" :options="models" size="large"
                            @click="validateInputs('models')" />
                    </NConfigProvider>
                </div>
                <div class="input-group">
                    <p>Ano</p>
                    <NConfigProvider :themeOverrides="theme">
                        <n-select v-model:value="selectedYear" filterable :disabled="!selectedBrand || !selectedModel"
                            placeholder="Selecione o ano do modelo" :options="years" size="large" />
                    </NConfigProvider>
                </div>
            </div>
            <div class="confirm-button">
                <NConfigProvider :themeOverrides="theme">
                    <n-button @click="consult" type="primary" size="large" :disabled="!selectedBrand || !selectedModel">
                        {{ consultButtonLabel }}
                    </n-button>
                </NConfigProvider>
            </div>
        </div>
    </div>
</template>

<script>
import { NSelect, NConfigProvider, NButton } from 'naive-ui';
import { GoogleLogin } from 'vue3-google-login'

export default {
    name: 'CarConsult',

    components: {
        NSelect,
        NConfigProvider,
        NButton,
        GoogleLogin
    },

    data() {
        return {
            cars: [],
            carBrands: [],
            selectedBrand: '',
            selectedModel: '',
            selectedYear: '',
            type: this.$route.query.type,
            notAuthenticated: true,
            theme: {
                common: {
                    primaryColor: '#14213D',
                    primaryColorHover: '#14213D',
                    primaryColorPressed: '#14213D',
                }
            },
            googleClientId: '754776355560-gq45cbnfua1jlb7g0cnbktj616n3b7op.apps.googleusercontent.com' // not a secret, it's ok to be exposed
        }
    },

    async mounted() {
        this.cars = this.$store.state.cars;
        this.carBrands = this.$store.state.brands;
    },

    computed: {
        title() {
            return this.type === 'consult'
                ? 'Selecione um modelo e analisaremos para você!'
                : 'Selecione um modelo para iniciar o chat com a IA!';
        },

        consultButtonLabel() {
            return this.type === 'consult'
                ? 'Consultar'
                : 'Iniciar Chat';
        },

        brands() {
            const brands = this.carBrands.map(brand => {
                const upperCaseName = brand.name.toUpperCase();

                return {
                    label: upperCaseName,
                    value: upperCaseName
                }
            });

            return brands.sort((a, b) => a.label.localeCompare(b.label));
        },

        models() {
            const cars = this.cars.filter(
                car => car.brand.toUpperCase() === this.selectedBrand
            )
                .map(car => {
                    const upperCaseModel = car.model;

                    return {
                        label: upperCaseModel,
                        value: upperCaseModel,
                        year: car.year,
                        price: car.price
                    }
                });

            return cars.sort((a, b) => a.label.localeCompare(b.label));
        },

        years() {
            return this.models
                .filter((car, index, self) =>
                    index === self.findIndex((t) => (
                        t.year === car.year
                    ))
                )
                .sort((a, b) => a.year - b.year)
                .map(car => ({
                    label: car.year,
                    value: car.year
                }));
        }
    },

    methods: {
        onFailure() {
            this.notAuthenticated = true;
        },

        onSuccess(response) {
            this.notAuthenticated = false;
            this.$store.setUserToken(response.credential);
        },

        validateInputs(type) {
            if (type === 'brands') {
                if (this.selectedModel) this.selectedModel = '';
                if (this.selectedYear) this.selectedYear = '';
            }

            if (type === 'models') {
                if (this.selectedYear) this.selectedYear = '';
            }
        },

        consult() {
            this.$router.push({
                path: this.type === 'consult' ? '/car-analysis' : '/ai-chat',
                query: {
                    brand: this.selectedBrand,
                    model: this.selectedModel,
                    year: this.selectedYear,
                    price: this.models.find(car => car.value === this.selectedModel).price
                }
            });
        },
    }

}
</script>

<style scoped lang="scss">
.main {
    color: black;
    margin-top: 80px;

    .title {
        margin-bottom: 40px;
        display: flex;
        justify-content: center;
        font-family: 'Montserrat', sans-serif;
        color: var(--primary-color)
    }

    .inputs {
        width: 500px;
        margin: 0 auto;
        display: flex;
        flex-direction: column;
        font-family: 'Lato', sans-serif;

        .input-group {
            margin-bottom: 20px;

            p {
                margin-bottom: 6px;
                margin-left: 2px;
            }
        }
    }

    .confirm-button {
        font-family: 'Montserrat', sans-serif;
        display: flex;
        justify-content: center;
        margin-top: 40px;
    }
}
</style>