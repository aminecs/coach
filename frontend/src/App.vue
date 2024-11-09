<script setup lang="ts">
import { ref } from 'vue';
import Welcome from './components/Welcome.vue';
import Name from './components/Name.vue';

const stages = {
  Welcome,
  Name,
};

const stage = ref('Welcome');

function changeStage(newStage) {
  console.log(`change to ${newStage}`);
  stage.value = newStage;
}
</script>

<template>
  <Transition>
    <component :is="stages[stage]" @change-stage="changeStage"></component>
  </Transition>
</template>

<style scoped>
  
</style>
