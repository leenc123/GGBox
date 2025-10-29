import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomePage.vue'
import Detail from '../views/GameDetail.vue'
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/detail/:url',
    name: 'Detail',
    component: Detail
  }
]
const router = createRouter({
  history: createWebHistory(),
  routes
})
export default router