<template>
    <div class="main">
        <div v-if="!loading">
            <div class="title">
                <h1>Selecione um modelo e analisaremos para você!</h1>
            </div>
            <div class="inputs">
                <div class="input-group">
                    <p>Marca*</p>
                    <NConfigProvider :themeOverrides="theme">
                        <n-select v-model:value="selectedBrand" filterable placeholder="Selecione uma marca"
                            :options="brands" size="large" />
                    </NConfigProvider>
                </div>
                <div class="input-group">
                    <p>Modelo*</p>
                    <NConfigProvider :themeOverrides="theme">
                        <n-select v-model:value="selectedModel" filterable :disabled="!selectedBrand"
                            placeholder="Selecione um modelo" :options="models" size="large" />
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
                        Consultar
                    </n-button>
                </NConfigProvider>
            </div>
        </div>
        <div v-else>
            <n-spin style="display: flex;" size="large" />
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { NSelect, NConfigProvider, NButton, NSpin } from 'naive-ui';

export default {
    name: 'CarConsult',

    components: {
        NSelect,
        NConfigProvider,
        NButton,
        NSpin
    },

    data() {
        return {
            loading: false,
            cars: [],
            carBrands: [],
            selectedBrand: '',
            selectedModel: '',
            selectedYear: '',
            theme: {
                common: {
                    primaryColor: '#14213D',
                    primaryColorHover: '#14213D',
                    primaryColorPressed: '#14213D',
                }
            }
        }
    },

    async mounted() {
        this.loading = true;

        await this.getBrands();
        await this.getCars();

        this.loading = false;
    },

    computed: {
        brands() {
            const brands = this.carBrands.map(brand => {
                const upperCaseName = brand.name.toUpperCase();

                return {
                    label: upperCaseName,
                    value: upperCaseName
                }
            });

            return brands;
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
                        year: car.year
                    }
                });

            return cars
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
        consult() {
            this.$router.push({
                path: '/car-analysis',
                query: {
                    brand: this.selectedBrand,
                    model: this.selectedModel,
                    year: this.selectedYear
                }
            });
        },

        async getBrands() {
            try {
                const response = await axios.get(`${import.meta.env.VITE_API_URL}/brands`);

                this.carBrands = response.data.brands;
            } catch (error) {
                console.error(error);
            }
        },

        async getCars() {
            try {
                const response = await axios.get(`${import.meta.env.VITE_API_URL}/cars`);

                this.cars = response.data.cars;
            } catch (error) {
                console.error(error);
            }
        }
    }

}
</script>

<style scoped lang="scss">
.main {
    color: black;
    margin-top: 130px;

    .title {
        margin-bottom: 40px;
        display: flex;
        justify-content: center;
        font-family: 'Montserrat', sans-serif;
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