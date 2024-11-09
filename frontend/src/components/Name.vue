<script setup lang="ts">
import { ref } from 'vue';
import Brand from './Brand.vue';
import Button from './Button.vue';

const name = ref("");
</script>

<template>
<main>
    <div class="">
        <Brand />
    </div>
    <div class="container">
        <h3>What's your name?</h3>
        <input v-model="name" placeholder="Your name" />
        <Button @click="$emit('changeStage', 'Coach')">
            Next
        </Button>
    </div>
</main>
</template>

<style lang="scss" scoped>
input {
    width: 100%;
    font-size: 1.1rem;
    font-family: inherit;
    font-weight: 500;
    background-color: white;
    padding: 1rem 1.3rem;
    border-radius: 20px;
}
</style>
