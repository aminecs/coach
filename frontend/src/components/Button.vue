<script setup lang="ts">
// defineProps<{

// }>();
</script>

<template>
<button>
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
}

button:hover {
    transform: translateY(-1px);
    cursor: pointer;
    box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
}
</style>
