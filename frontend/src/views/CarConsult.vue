<template>
  <div>
    <!-- TODO -->
  </div>
</template>

<script>
import axios from 'axios';

export default {

    data() {
        return {
            loading: false,
            cars: [],
        }
    },

    mounted() {
        this.getCars();
    },

    methods: {
        async getCars() {
            try {
                this.loading = true;
                this.cars = await axios.get(`${import.meta.env.VITE_API_URL}/cars`);
            } catch (error) {
                console.error(error);
            } finally {
                this.loading = false;                
            }
        }
    }

}
</script>

<style>

</style>