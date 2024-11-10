<script setup lang="ts">
import { useTemplateRef } from 'vue';
import Button from './components/Button.vue';
import { coachInfo, type CoachName } from '@/types';

const emit = defineEmits(['changeStage']);

function onNext(coach: CoachName) {
    emit('changeStage', 'Motivation', { coach: coachInfo[coach] });
}

const gogginsBtn = useTemplateRef('goggins-btn');

function clickGoggins() {
    console.log('clicking goggins');
    gogginsBtn.value?.longPress();
}

defineExpose({ clickGoggins });

</script>

<template>
    <section class="container">
        <h3>Choose your coach</h3>
        <Button @click="onNext('goggins')" ref="goggins-btn">
            <img src="/goggins-profile.png">
            <div class="text">
                <p class="name">David Goggins</p>
                <p class="description">
                    David Goggins inspires people to push beyond their limits
                    with his relentless mindset and extreme resilience.
                </p>
            </div>
        </Button>
        <Button @click="onNext('dame')">
            <img src="/dame-profile.png">
            <div class="text">
                <p class="name">Dame Judi Dench</p>
                <p class="description">
                    Her wisdom, depth, and ability to inspire confidence through
                    kindness and grace will get you through the toughest of
                    circumstances.
                </p>
            </div>
        </Button>
        <Button @click="onNext('custom')">
            <img src="/custom-profile.png">
            <div class="text">
                <p class="name">Create your own coach</p>
                <p class="description">
                    Who motivates you? Share a 30-second voice clip so we can
                    use their voice to coach you.
                </p>
            </div>
        </Button>
    </section>
</template>

<style lang="scss" scoped>
button {
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

p {
    margin-top: 0.2rem;
    margin-bottom: 0.2rem;
}

.description {
    font-size: 0.8rem;
    font-weight: normal;
}

.container {
    gap: 1rem;
}
</style>
