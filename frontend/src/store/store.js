import { reactive } from 'vue';

const state = reactive({
    cars: [],
    brands: [],
});

const setCars = (cars) => {
    state.cars = cars;
};

const setBrands = (brands) => {
    state.brands = brands;
}

export default {
    state,
    setCars,
    setBrands,
};