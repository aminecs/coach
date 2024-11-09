<script setup lang="ts">
import { ref } from 'vue';
import Button from './components/Button.vue';
import type { Goal } from './types';

const emit = defineEmits(['changeStage']);

function onNext(goal: Goal) {
    emit('changeStage', 'Primary', { goal });
}
</script>

<template>
    <section class="container">
        <h3>What's your goal for your run today?</h3>
        <Button @click="onNext('5 kilometers')">
            <div class="icon">🏃</div>
            <div class="text">
                <b>5k</b> - A great challenge for beginner to intermindate runners.
            </div>
        </Button>
        <Button @click="onNext('10 kilometers')">
            <div class="icon">🏃</div>
            <div class="text">
                <b>10k</b> - Ready for the next level up? Challenge yourself with a 10k.
            </div>
        </Button>
        <Button @click="onNext('Marathon')">
            <div class="icon">🚶</div>
            <div class="text">
                <b>Marathon</b> - Ready for the next level up, champ? Go big with a marathon.
            </div>
        </Button>
        <Button @click="onNext('Custom')">
            <div class="icon">🔧</div>
            <div class="text">Set your own goal.</div>
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
