<script setup lang="ts">
import { ref, useTemplateRef } from 'vue';
import Button from './components/Button.vue';

const emit = defineEmits(['changeStage']);

const motivation = ref("");
function onNext() {
    emit('changeStage', 'Goal', { motivation });
}

const btn = useTemplateRef('btn');

function fillMotivation(newMotivation: string) {
    motivation.value = newMotivation;
    console.log(`newMotivation ${newMotivation}`);
    setTimeout(() => {
        btn.value?.longPress();
    }, 1500);
}

defineExpose({ fillMotivation });
</script>

<template>
    <section class="container">
        <h3>What is that motivates you</h3>
        <p>
            Tell you coach, and they'll keep you motivated when
            the run gets tough.
        </p>
        <textarea v-model="motivation" placeholder="What motivates me is..." @keyup.enter.native="onNext" />
        <Button @click="onNext" ref="btn">
            Next
        </Button>
    </section>
</template>

<style lang="scss" scoped>
textarea {
    width: 100%;
    font-size: 1rem;
    font-family: inherit;
    font-weight: 500;
    background-color: white;
    padding: 1rem 1.3rem;
    border-radius: 20px;
    min-height: 5rem;
}
</style>
