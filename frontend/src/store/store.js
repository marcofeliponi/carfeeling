import { reactive } from 'vue';

const state = reactive({
    cars: [],
    brands: [],
    userToken: null,
});

const setCars = (cars) => {
    state.cars = cars;
};

const setBrands = (brands) => {
    state.brands = brands;
}

const setUserToken = (token) => {
    state.userToken = token;
}

export default {
    state,
    setCars,
    setBrands,
    setUserToken,
};