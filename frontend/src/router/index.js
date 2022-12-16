import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../pages/home.vue'
import LogVue from '../pages/log.vue'
import manageVue from '../pages/manage.vue'
const routes = [
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  {
    path: '/',
    name: 'log',
    component: LogVue
  },
  {
    path: '/manage',
    name: 'management',
    component: manageVue
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
