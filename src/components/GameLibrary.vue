<template>
    <div class="container">
        <div v-for="item in data" :key="item.id" class="content">

            <img :src="item.pic" />
            <span>{{ item.name }}</span>
        </div>
        <div class="scale-on-hover">鼠标悬停我试试</div>
    </div>

</template>

<script setup>
const props = defineProps({
    data: {
        type: Object,
        required: true
    },
    size: {
        type: String,
        default: 'medium',
        validator: (value) => ['small', 'medium', 'large'].includes(value)
    },
    selected: {
        type: Boolean,
        default: false
    }
})
</script>

<style lang="scss" scoped>
/* Webkit浏览器隐藏滚动条 (Chrome, Safari, Opera) */
.container::-webkit-scrollbar {
    display: none;
}
.container {
     scrollbar-width: none; /* Firefox隐藏滚动条 */
    -ms-overflow-style: none; /* IE和Edge隐藏滚动条 */
    height: 180px;
    padding-top: 10px;
    overflow-x: auto;
    /* 允许横向滚动 */
    white-space: nowrap;
    /* 防止子元素换行 */
    padding-inline: 10px;

    .content {
        white-space: normal;
        /* 恢复内容内部的正常换行 */
        flex-shrink: 0;
        /* 防止元素被压缩 */
        padding-inline: 10px;
        position: relative;
        vertical-align: top;
        display: inline-block;

        img {
            transform-origin: left top;
            transition: all 0.5s ease;
            display: inline-block;
            width: 100px;
            height: 100px;
        }

        span {
            position: absolute;
            left: 100%;
            /* 定位到图片右侧 */
            bottom: 0;
            /* 与图片顶部对齐 */
            margin-left: 8px;
            /* 与图片保持间距 */
            white-space: nowrap;
            /* 防止文字换行 */
            opacity: 0;
            /* 默认隐藏 */
            transition: opacity 0.3s ease;
            pointer-events: none;
            /* 防止span干扰鼠标事件 */
            /* 默认隐藏 */
            color: white;
            text-shadow: 0 0 2px #fff
        }

        img:hover+span {
            opacity: 1;
            /* 鼠标悬停时显示 */
            /* 鼠标悬停时显示 */
        }

        img:hover {
            width: 140px;
            height: 140px;
        }
    }
}
</style>