<script setup lang="ts">
import Brand from './components/Brand.vue';
import Button from './components/Button.vue';
</script>

<template>
    <section class="container">
        <Brand size="big" />
        <h3>Unlock your potential with your personal AI running coach</h3>
        <Button @click="$emit('changeStage', 'Name')">
            Let's go 🔥
        </Button>
    </section>
</template>

<style lang="scss" scoped></style>
