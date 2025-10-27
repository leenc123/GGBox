<template>
  <span class="text" :style="{ fontSize: fontSize, color: selected ? '#FFFFFF':'gray',textShadow: selected? '0 0 5px #fff,0 0 10px #fff':'' }">
    {{ text }}
  </span>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
onMounted(() => {

})

const fontSize = computed(() => {
  switch (props.size) {
    case 'small':
      return '12px'
    case 'medium':
      return '16px'
    case 'large':
      return '20px'
    default:
      return '16px'
  }
})
const props = defineProps({
  text: {
    type: String,
    required: true
  },
  size: {
    type: String,
    default: 'medium',
    validator: (value) => ['small', 'medium', 'large'].includes(value)
  },
  selected: {
    type :Boolean,
    default:false
  }
})
</script>

<style lang="scss" scoped>
.text {
  width: auto;
  color: gray;
}

.text:hover {
  cursor: pointer;
  color: white;
}
</style>