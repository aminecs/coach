<script setup lang="ts">
import { ref, useTemplateRef } from 'vue';
import Button from './components/Button.vue';

const emit = defineEmits(['changeStage']);

const name = ref("");
function onNext() {
    emit('changeStage', 'Coach', { name });
}

const btn = useTemplateRef("btn");

function setName(newName: string) {
    name.value = newName;
    setTimeout(() => {
        btn.value?.longPress();
    }, 1000);
}

defineExpose({ setName });
</script>

<template>
    <section class="container ">
        <h3>What's your name?</h3>
        <input v-model="name" placeholder="Your name" @keyup.enter.native="onNext" />
        <Button @click="onNext" ref="btn">
            Next
        </Button>
    </section>
</template>

<style lang="scss" scoped>
input {
    width: 70%;
    font-size: 1.1rem;
    font-family: inherit;
    font-weight: 500;
    background-color: white;
    padding: 1rem 1.3rem;
    border-radius: 20px;
}
</style>
