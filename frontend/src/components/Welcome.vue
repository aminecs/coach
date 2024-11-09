<script setup lang="ts">
import Button from './Button.vue';
import Brand from './Brand.vue';
</script>

<template>
<main class="container">
    <Brand />
    <h3>Achieve your running goals with Coach</h3>
    <Button @click="$emit('changeStage', 'Name')">
        Let's go 🔥
    </Button>
</main>
</template>

<style lang="scss" scoped>

</style>
