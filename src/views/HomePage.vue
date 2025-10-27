<template>
  <div class="container" :style="containerStyle">
    <img style="position: absolute;width: 100%;height: 100%;z-index: -1;"
      src="https://img1.baidu.com/it/u=1068231705,1341969959&fm=253&fmt=auto&app=138&f=JPEG?w=800&h=500" />
    <div class="gradient-bg"/>
    <div v-for="item in titleMenu" :key="item.id" class="menu" @click="selectedId = item.id">
      <CommonText :text="item.title" :size="TextSize.LARGE" :selected="selectedId == item.id"  />
    </div>
    <GameLibrary :data="gameLibrary"></GameLibrary>
  </div>
</template>

<script setup>
import CommonText from '../components/text/CommonText.vue';
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { TextSize } from '../components/text/constants';
import GameLibrary from '../components/GameLibrary.vue';


const windowHeight = ref(window.innerHeight)
const windowWidth = ref(window.innerWidth)
const selectedId = ref(0) //菜单选中项
const titleMenu = ref([{ title: '库', id: 0 }, { title: '浏览', id: 1 }]) //菜单选项
const gameLibrary = ref([{name:'1233',pic:'https://img1.baidu.com/it/u=1005000719,311741344&fm=253&fmt=auto&app=138&f=JPEG?w=889&h=500',id:0},{name:'1233',pic:'https://gips1.baidu.com/it/u=1692916706,3187136387&fm=3074&app=3074&f=PNG?w=2560&h=1440',id:1},{name:'1233',pic:'https://gips0.baidu.com/it/u=1057963292,1043636754&fm=3074&app=3074&f=PNG?w=2560&h=1440',id:2},
  {name:'1233',pic:'https://img1.baidu.com/it/u=1005000719,311741344&fm=253&fmt=auto&app=138&f=JPEG?w=889&h=500',id:0},{name:'1233',pic:'https://gips1.baidu.com/it/u=1692916706,3187136387&fm=3074&app=3074&f=PNG?w=2560&h=1440',id:1},{name:'1233',pic:'https://gips0.baidu.com/it/u=1057963292,1043636754&fm=3074&app=3074&f=PNG?w=2560&h=1440',id:2},
  {name:'1233',pic:'https://img1.baidu.com/it/u=1005000719,311741344&fm=253&fmt=auto&app=138&f=JPEG?w=889&h=500',id:0},{name:'1233',pic:'https://gips1.baidu.com/it/u=1692916706,3187136387&fm=3074&app=3074&f=PNG?w=2560&h=1440',id:1},{name:'1233',pic:'https://gips0.baidu.com/it/u=1057963292,1043636754&fm=3074&app=3074&f=PNG?w=2560&h=1440',id:2}
])
const updateDimensions = () => {
  windowHeight.value = window.innerHeight
  windowWidth.value = window.innerWidth
}
// 计算容器样式
const containerStyle = computed(() => {
  return {
    width: windowWidth.value + 'px',
    height: windowHeight.value + 'px'
  }
})
onMounted(() => {
  window.addEventListener('resize', updateDimensions)
})
onUnmounted(() => {
  window.removeEventListener('resize', updateDimensions)
})


</script>

<style lang="scss" scoped>
.container {

  position: relative;

  .gradient-bg {
    position: absolute;
    width: 100%;
    height: 100%;
    z-index: -1;
    background: radial-gradient(circle at 70% 70%,
        /* 中心点靠右一点 */
        transparent 0%,
        transparent 30%,
        rgba(0, 0, 0, 0.9) 70%,
        #000 100%);
    transition: all 0.5s ease;
  }
  .menu{
    display: inline-block;
    margin-left: 20px;
    margin-top: 20px;
  }

  /* 确保padding和border包含在宽高内 */
  #particles-js {
    position: absolute;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #0f0f0f 0%, #1a1a2e 50%, #16213e 100%);
    z-index: 1;
  }
}
</style>