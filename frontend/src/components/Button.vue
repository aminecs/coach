<script setup lang="ts">
import { useTemplateRef } from 'vue';

const buttonRef = useTemplateRef('btn');

const clickEvent = new MouseEvent('click');

const events = {
    pointerdown: new PointerEvent('pointerdown', {
        bubbles: true,
        cancelable: true,
        view: window,
        pressure: 1,
        pointerType: 'mouse'
    }),
    mousedown: new MouseEvent('mousedown', {
        bubbles: true,
        cancelable: true,
        view: window
    }),
    pointerup: new PointerEvent('pointerup', {
        bubbles: true,
        cancelable: true,
        view: window,
        pressure: 0,
        pointerType: 'mouse'
    }),
    mouseup: new MouseEvent('mouseup', {
        bubbles: true,
        cancelable: true,
        view: window
    })
};

function longPress() {
    console.log(`btn exist ${buttonRef.value}`);
    buttonRef.value?.classList.add("hover");
    setTimeout(() => {
        buttonRef.value?.classList.add("active");
        setTimeout(() => {
            buttonRef.value?.classList.remove("hover", "active");
            buttonRef.value?.dispatchEvent(clickEvent);
        }, 600);
    }, 100);
}

defineExpose({ longPress });
</script>

<template>
    <button ref="btn">
        <slot></slot>
    </button>
</template>

<style lang="scss">
button {
    font-size: 1.1rem;
    font-family: inherit;
    font-weight: 500;
    background-color: white;
    padding: 0.8rem 1.3rem;
    border-radius: 20px;
    border: 1px solid #555;
}

button:hover,
.hover {
    transform: translateY(-1px);
    cursor: pointer;
    box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
}

button:active,
.active {
    background-color: #d29300;
    color: white;
    box-shadow: rgba(1, 51, 60, 0.7) 0px 5px 5px;
}
</style>
