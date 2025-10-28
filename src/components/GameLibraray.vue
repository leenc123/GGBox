<template>
    <div class="grid-fixed" :style="{ maxHeight: mainHeight, overflow: 'auto' }" ref="containerRef">
        <div v-for="item in games" :key="item.id" class="content">
            <img :src="item.pic"></img>
            <span class="title-overlay">{{ item.name }}</span>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import initSqlJs from 'sql.js'
import { debounce } from 'lodash'
let pyodide = null
let db = null
// 初始化数据库
const initDatabase = async () => {
    try {
        const SQL = await initSqlJs({
            locateFile: file => `https://sql.js.org/dist/${file}`
        })
        // 直接从 data 目录加载
        const response = await fetch('https://raw.githubusercontent.com/leenc123/GGBox/main/ggbox.db');
        if (!response.ok) throw new Error('数据库文件未找到');

        const arrayBuffer = await response.arrayBuffer();
        const uint8Array = new Uint8Array(arrayBuffer);

        db = new SQL.Database(uint8Array);
        console.log('数据库加载成功！');

        console.log('数据库初始化成功')
    } catch (error) {
        console.error('数据库初始化失败:', error)
    }
}
// 分页状态
const pagination = ref({
    currentPage: 1,
    pageSize: 40,
    total: 0,
    totalPages: 0
})
onMounted(async () => {
    if (containerRef.value) {
        containerRef.value.addEventListener('scroll', handleScroll)
    }
    await initDatabase()
    getGames()
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
await micropip.install('requests')
print('12333')
`)
    } catch (e) {
        console.log(`Pyodide 初始化失败: ${e.message}`)
    }
})
onUnmounted(() => {
    if (containerRef.value) {
        containerRef.value.removeEventListener('scroll', handleScroll)
    }
})
const containerRef = ref(null)
const loading = ref(false)
const hasMore = ref(true)
const handleScroll = debounce(() => {
    if (!containerRef.value) return
    const { scrollTop, scrollHeight, clientHeight } = containerRef.value
    if (scrollTop + clientHeight >= scrollHeight - 30 && !loading.value && hasMore.value) {
        getGames(pagination.value.currentPage + 1)
    }
}, 200) // 200ms 防抖延迟
const games = ref([])
const getGames = (page = 1) => {
    if (!db) return
    loading.value = true
    // 更新当前页码
    pagination.value.currentPage = page

    // 计算偏移量
    const offset = (page - 1) * pagination.value.pageSize

    // 获取总数
    const countResult = db.exec('SELECT COUNT(*) as total FROM games')
    const total = countResult[0]?.values[0][0] || 0
    hasMore.value = total / pagination.value.pageSize >= page
    console.log(`totalNum${total}`)
    console.log(`totalSize${total / pagination.value.pageSize}`)
    const result = db.exec(`SELECT * FROM games LIMIT ${pagination.value.pageSize} 
    OFFSET ${offset}`)
    loading.value = false
    if (result.length > 0) {
        const columns = result[0].columns
        const values = result[0].values
        if (pagination.value.currentPage == 1) {
            games.value = values.map(row => {
                const games = {}
                columns.forEach((col, index) => {
                    games[col] = row[index]
                })
                return games
            })
        } else {
            games.value = [...games.value, ...values.map(row => {
                const games = {}
                columns.forEach((col, index) => {
                    games[col] = row[index]
                })
                return games
            })]
        }

    }
}
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
        position: relative;
        overflow: hidden;
        aspect-ratio: 1 / 1;
        width: 100%;
        /* 宽度占满网格单元格 */
        height: auto;
        /* 高度根据宽高比自动计算 */
        background-color: aqua;

        img {
            object-fit: cover;
            /* 关键：填充整个容器 */
            width: 100%;
            height: 100%;
        }

        .title-overlay {
            position: absolute;
            bottom: 0;
            left: 0;
            background: linear-gradient(transparent, rgba(0, 0, 0, 0.7));
            color: white;
            padding: 8px 4px;
            text-align: left;
            font-size: 14px;
            z-index: 2;
        }
    }
}
</style>