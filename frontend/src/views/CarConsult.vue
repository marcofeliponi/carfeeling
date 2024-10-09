<template>
    <div class="main">
        <div class="title">
            <h1>Selecione um modelo e analisaremos para você!</h1>
        </div>
        <div class="inputs">
            <div class="input-group">
                <p>Marca*</p>
                <NConfigProvider :themeOverrides="inputTheme">
                    <n-select v-model:value="selectedBrand" filterable placeholder="Selecione uma marca"
                        :options="brands" size="large" />
                </NConfigProvider>
            </div>
            <div class="input-group">
                <p>Modelo*</p>
                <NConfigProvider :themeOverrides="inputTheme">
                    <n-select v-model:value="selectedModel" filterable :disabled="!selectedBrand"
                        placeholder="Selecione um modelo" :options="models" size="large" />
                </NConfigProvider>
            </div>
            <div class="input-group">
                <p>Ano</p>
                <NConfigProvider :themeOverrides="inputTheme">
                    <n-select v-model:value="selectedYear" filterable :disabled="!selectedBrand || !selectedModel"
                        placeholder="Selecione o ano do modelo" :options="years" size="large" />
                </NConfigProvider>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { NSelect, NConfigProvider } from 'naive-ui';

export default {
    name: 'CarConsult',

    components: {
        NSelect,
        NConfigProvider
    },

    data() {
        return {
            loading: false,
            cars: [],
            carBrands: [],
            selectedBrand: '',
            selectedModel: '',
            selectedYear: '',
            inputTheme: {
                common: {
                    primaryColor: '#14213D',
                    primaryColorHover: '#14213D',
                    primaryColorPressed: '#14213D',
                }
            }
        }
    },

    mounted() {
        this.getBrands();
        this.getCars();
    },

    computed: {
        brands() {
            const brands = this.carBrands.map(car => {
                const upperCaseName = car.name.toUpperCase();

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
                    const upperCaseModel = car.model.toUpperCase();

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
        async getBrands() {
            try {
                this.loading = true;
                const response = await axios.get(`${import.meta.env.VITE_API_URL}/brands`);

                this.carBrands = response.data.brands;
            } catch (error) {
                console.error(error);
            } finally {
                this.loading = false;
            }
        },

        async getCars() {
            try {
                this.loading = true;
                const response = await axios.get(`${import.meta.env.VITE_API_URL}/cars`);

                this.cars = response.data.cars;
            } catch (error) {
                console.error(error);
            } finally {
                this.loading = false;
            }
        }
    }

}
</script>

<style scoped lang="scss">
.main {
    color: black;
    margin-top: 100px;

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
}
</style>