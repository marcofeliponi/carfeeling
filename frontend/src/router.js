import { createMemoryHistory, createRouter } from 'vue-router'

import HomePage from './views/HomePage.vue'
import CarConsult from './views/CarConsult.vue'
import CarAnalysis from './views/CarAnalysis.vue'
import AiChat from './views/AiChat.vue'

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
  {
    path: '/car-analysis',
    name: 'carAnalysis',
    component: CarAnalysis
  },
  {
    path: '/ai-chat',
    name: 'AiChat',
    component: AiChat
  }
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

export default router