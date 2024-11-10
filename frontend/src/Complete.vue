<script setup lang="ts">
import { ref } from 'vue';
import Button from './components/Button.vue';
import type { Goal, Profile } from './types';

const { profile } = defineProps<{
    profile: Profile
}>();

const emit = defineEmits(['changeStage']);


</script>

<template>
    <section class="container">
        <h2>Run completed</h2>
        <div class="status">
            <img :src="profile.coach?.img">
            <div class="text">
                <p class="name">Coach <b>{{ profile.coach?.name }}</b></p>
                <p class="description">You did it {{ profile.name }}, I'm proud of you 💪</p>
            </div>
        </div>
        <div class="status goal">
            <h3>Goal - {{ profile.goal.name }} <span class="emoji">{{ profile.goal.emoji }}</span></h3>
            <div class="metrics1">
                <h1>5.00</h1> km
            </div>
            <div class="metrics2">
                <div>
                    <h3>6:44</h3>
                    <p>Avg. pace</p>
                </div>
                <div>
                    <h3>135</h3>
                    <p>BPM</p>
                </div>
                <div>
                    <h3>34:17</h3>
                    <p>Time</p>
                </div>
            </div>
        </div>
        <Button @click="$emit('changeStage', 'Leaderboard')">See leaderboard 🏆</Button>
    </section>
</template>

<style lang="scss" scoped>
.container {
    gap: 1.5rem;
}

img {
    width: 4rem;
    height: 4rem;
}

.status {
    border: 1px solid rgba(255, 255, 255, 0.2);
    font-size: 1rem;
    border-radius: 15px;
    padding: 0.5rem 1rem;
    width: 100%;
    display: flex;
    gap: 1rem;
    align-items: center;
    -webkit-backdrop-filter: blur(8px);
    backdrop-filter: blur(8px);
    background-color: rgba(255, 255, 255, 0.1);
}

.goal {
    background-color: white;
    color: black;
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 1rem;
}

.text {
    text-align: left;
}

.emoji {
    font-size: 1.5rem;
}

.metrics1 {
    display: flex;
    gap: 0.5rem;
    align-items: center;
    font-size: 1.5rem;

    h1 {
        font-size: 3rem;
        display: inline;
        margin: 0;
    }
}

.metrics2 {
    display: flex;
    flex-direction: row;
    gap: 2rem;

    p {
        margin-top: 0.2rem;
        margin-bottom: 0.2rem;
    }

    >div {
        display: flex;
        flex-direction: column;
        gap: 0;


    }
}
</style>
