<template>
  <div>
    <!-- TODO -->
  </div>
</template>

<script>
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
                this.cars = await fetch(`${import.meta.env.VITE_API_URL}/cars`);
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