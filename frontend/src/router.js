import { createMemoryHistory, createRouter } from 'vue-router'

import HomePage from './views/HomePage.vue'
import CarConsult from './views/CarConsult.vue'

const routes = [
  { 
    path: '/',
    name: 'home',
    component: HomePage
  },
  {
    path: '/car-consult',
    name: 'carConsult',
    component: CarConsult
  },
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

export default router