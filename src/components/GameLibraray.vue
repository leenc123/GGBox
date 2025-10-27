<template>
    <div class="grid-fixed" :style="{ maxHeight: mainHeight, overflow: 'auto' }">
        <div v-for="i in 123" class="content"></div>
    </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
let pyodide = null
onMounted(async () => {
    try {
        // 动态导入 Pyodide
        pyodide = await loadPyodide({
            indexURL: "https://cdn.jsdelivr.net/pyodide/v0.23.4/full/"
        })
        // 安装必要的包
        await pyodide.loadPackage(['micropip'])
        const micropip = pyodide.pyimport('micropip')
        await micropip.install(['requests', 'beautifulsoup4'])
        console.log('Pyodide 初始化完成');
        await pyodide.runPythonAsync(`
import micropip
await micropip.install('numpy')
import math
`)
    } catch (e) {
        console.log(`Pyodide 初始化失败: ${e.message}`)
    }
})
const props = defineProps({
    height: {
        type: Number,
        required: true,
        default: 400
    }
})
const mainHeight = computed(() => {
    return props.height - 70 + 'px'
})
</script>

<style lang="scss" scoped>
.grid-fixed {
    margin-top: 10px;
    padding-inline: 10px;
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    /* 4列等宽 */
    gap: 15px;

    .content {
        aspect-ratio: 1 / 1;
        width: 100%;
        /* 宽度占满网格单元格 */
        height: auto;
        /* 高度根据宽高比自动计算 */
        background-color: aqua;
    }
}
</style>