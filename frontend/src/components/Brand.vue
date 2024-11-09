<script setup lang="ts">
defineProps<{
    size?: 'big' | 'small'
}>();
</script>

<template>
<img src="/Logo.png" :class="size ?? 'small'" />
</template>

<style lang="scss" scoped>
.big {
    width: 60%;
}
.small {
    width: 40%;
}
</style>
