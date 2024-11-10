<script setup lang="ts">
import { ref } from 'vue';
import Button from './components/Button.vue';
import { goalInfo, type GoalName } from './types';

const emit = defineEmits(['changeStage']);

function onNext(goal) {
    emit('changeStage', 'Primary', { goal });
}
</script>

<template>
    <section class="container">
        <h3>What's your goal for your run today?</h3>
        <Button v-for="goal in goalInfo" @click="onNext(goal)">
            <div class="icon">{{ goal.emoji }}</div>
            <div class="text">
                <b>{{ goal.name }}</b> - {{ goal.desc }}
            </div>
        </Button>
    </section>
</template>

<style lang="scss" scoped>
.container {
    gap: 1rem;
}

button {
    display: flex;
    width: 100%;
    text-align: left;
    font-size: 0.9rem;
    gap: 1rem;
    align-items: center;
    font-weight: normal;

    .icon {
        flex: 1;
        font-size: 2rem;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .text {
        flex: 7;
        text-align: left;
    }
}
</style>
