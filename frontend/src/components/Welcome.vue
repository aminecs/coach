<script setup lang="ts">
import Brand from './Brand.vue';
import Button from './Button.vue';
</script>

<template>
<section class="container">
    <Brand />
    <h3>Achieve your running goals with Coach</h3>
    <Button @click="$emit('changeStage', 'Name')">
        Let's go 🔥
    </Button>
</section>
</template>

<style lang="scss" scoped>

</style>
