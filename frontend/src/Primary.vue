<script setup lang="ts">
import Button from './components/Button.vue';
import type { Profile } from './types';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

const { profile } = defineProps<{
    profile: Profile
}>();

</script>

<template>
    <section class="container">
        <div class="row">
            <div class="status">
                <div class="text">
                    <p class="name">Goal</p>
                    <p class="description">5K</p>
                </div>
            </div>
            <div class="status">
                <img :src="profile.coach?.img">
                <div class="text">
                    <p class="name">Coach</p>
                    <p class="description">{{ profile.coach?.name }}</p>
                </div>
            </div>
        </div>
        <div class="main">
            <Button class="start">
                Start
            </Button>
        </div>
        <div class="row">
            <div class="status">
                <img :src="profile.coach?.img">
                <div class="text">
                    <p class="meta">
                        <fa-icon icon="fa-brands fa-spotify" />
                        Spotify · Daily Mix 2
                    </p>
                    <p class="name">Sprinter</p>
                    <p class="description">Dave & Central cee</p>
                </div>
            </div>
        </div>
    </section>
</template>

<style lang="scss" scoped>
.container {
    justify-content: space-between;
}

.row {
    width: 100%;
    display: flex;
    gap: 2rem;
    justify-content: space-between;
}

.status {
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 15px;
    padding: 1rem;
    width: 100%;
    display: flex;
    gap: 1rem;
    align-items: center;
}

img {
    width: 4rem;
    height: 4rem;
}

.text {
    text-align: left;
}

.meta {
    font-size: 0.7rem;
    margin-bottom: 1rem;
}

p {
    margin-top: 0.2rem;
    margin-bottom: 0.2rem;
}

.description {
    font-size: 0.8rem;
    font-weight: normal;
}

.start {
    width: 10rem;
    height: 10rem;
    border-radius: 5rem;
}

.main {}
</style>
