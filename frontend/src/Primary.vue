<script setup lang="ts">
import { computed, ref } from 'vue';
import Button from './components/Button.vue';
import { socket, type Profile } from './types';

const emit = defineEmits(['changeStage']);

const { profile } = defineProps<{
    profile: Profile
}>();

const started = ref<boolean>(false);
const running = ref<boolean>(false);
const elapsed = ref<number>(0.);
const timerId = ref<number>(0);
const distance = ref<number>(0);
const distanceId = ref<number>(0);
const showMansion = ref<boolean>(false);

function onStart() {
    started.value = true;
    running.value = true;
    setTimeout(() => {
        distanceId.value = setInterval(() => distance.value += 1, 300);
    }, 2000);
    timerId.value = setInterval(() => elapsed.value += 1, 1000);
    fetch("http://127.0.0.1:8200?" + new URLSearchParams({
        name: profile.name!,
        goal: profile.goal?.name!,
    }), {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    });
}

function onPlayPause() {
    if (running.value) {
        running.value = false;
        clearInterval(timerId.value);
        clearInterval(distanceId.value);
    } else {
        running.value = true;
        timerId.value = setInterval(() => elapsed.value += 1, 1000);
        distanceId.value = setInterval(() => distance.value += 1, 300);
    }
}

const zeroPad = (num, places) => String(num).padStart(places, '0')

const elapsedFormatted = computed(() => {
    const minute = Math.round(elapsed.value / 60);
    const seconds = elapsed.value % 60;
    return `${minute}:${zeroPad(seconds, 2)}`;
});

const distanceFormatted = computed(() => {
    const km = Math.round(distance.value / 1000);
    const m = Math.round(distance.value % 1000 / 10);
    return `${km}.${zeroPad(m, 2)}`;
});

socket.on('video', () => {
    showMansion.value = true;
    setTimeout(() => showMansion.value = false, 7000);
});

const onStop = () => {
    fetch("http://127.0.0.1:8200/terminate", {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    });
    fetch("http://127.0.0.1:8200/api/leaderboard", {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
    });
    emit('changeStage', 'Complete');
};
</script>

<template>
    <section class="container">
        <div class="row">
            <div class="status">
                <div class="profile">{{ profile.goal.emoji }}</div>
                <div class="text">
                    <p class="name">{{ profile.goal.name }}</p>
                    <p class="description">Goal</p>
                </div>
            </div>
            <div class="status">
                <img class="profile" :src="profile.coach?.img">
                <div class="text">
                    <p class="name">{{ profile.coach?.name }}</p>
                    <p class="description">Coach</p>
                </div>
            </div>
        </div>
        <div class="main" v-if="!started">
            <Button class="start" @click="onStart">
                Start
            </Button>
        </div>
        <video autoplay muted loop v-else-if="showMansion">
            <source src="/mansion.mp4" type="video/mp4">
        </video>
        <div v-else class="main">
            <div class="row other">
                <div class="stat">
                    <h2>7'07</h2>
                    <p>Pace</p>
                </div>
                <div class="stat">
                    <h2>135</h2>
                    <p>BPM</p>
                </div>
                <div class="stat">
                    <h2>{{ elapsedFormatted }}</h2>
                    <p>Time</p>
                </div>
            </div>
            <div class="row km">
                <div class="stat"><span>{{ distanceFormatted }}</span>km</div>
            </div>
            <div class="row controls">
                <Button @click="onPlayPause">
                    <fa-icon :icon="['fa-solid', running ? 'fa-pause' : 'fa-play']" />
                </Button>
                <Button @click="onStop">
                    <fa-icon icon="fa-solid fa-stop" />
                </Button>
            </div>
        </div>
        <div class="row">
            <div class="status">
                <img src="/playing.png">
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

.other {
    gap: 0;
}

.km {
    justify-content: center;

    span {
        font-size: 4rem;
    }
}

.controls {
    justify-content: center;

    button {
        width: 5rem;
        height: 5rem;
        border-radius: 2.5rem;
    }
}

.status {
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 15px;
    padding: 1rem;
    width: 100%;
    display: flex;
    gap: 1rem;
    align-items: center;
    -webkit-backdrop-filter: blur(8px);
    backdrop-filter: blur(8px);
    background-color: rgba(255, 255, 255, 0.1);
}

img {
    width: 4rem;
    height: 4rem;
}

.profile {
    font-size: 2.5rem;
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

.main {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.stat {
    text-align: center;
    padding: 1rem;
    min-width: 7rem;

    h2 {
        font-size: 2.5rem;
    }
}

video {
    width: calc(100% + 4rem);
    margin: 0 -2rem;
}
</style>
