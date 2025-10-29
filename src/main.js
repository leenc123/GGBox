import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
const app = createApp(App)
try {
  app.use(router)
  console.log('路由初始化成功')
} catch (error) {
  console.error('路由初始化失败:', error)
}
app.mount('#app')
