<script setup lang="ts">
import Brand from './components/Brand.vue';
import Button from './components/Button.vue';

const emit = defineEmits(['changeStage']);

function onClick() {
    emit('changeStage', 'Name');
    fetch("http://127.0.0.1:8200/api/start_onboarding", {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    });
}

</script>

<template>
    <section class="container">
        <Brand size="big" />
        <h3>Unlock your potential with your personal AI running coach</h3>
        <Button @click="onClick">
            Let's go 🔥
        </Button>
    </section>
</template>

<style lang="scss" scoped></style>
