<template>
    <div style="background-color: aqua;">
            12333
    </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { useRoute } from 'vue-router'
const route = useRoute()
const url = route.params.url
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
        await micropip.install(['requests', 'beautifulsoup4','pyodide_http'])
        console.log('Pyodide 初始化完成');
        
        await pyodide.runPythonAsync(`
import requests
from bs4 import BeautifulSoup
import pyodide_http
# 修补所有 HTTP 客户端
pyodide_http.patch_all()
# 使用 CORS 代理
cors_proxy = "https://corsproxy.io/?"
target_url = "https://www.gamer520.com/101336.html"
full_url = cors_proxy + target_url
print("开始请求...")
response_body = requests.get(full_url)
print(response_body.text)
soup_body = BeautifulSoup(response_body.text, 'html.parser')
`)
    } catch (e) {
        console.log(`Pyodide 初始化失败: ${e.message}`)
    }
})

</script>

<style lang="scss" scoped></style>