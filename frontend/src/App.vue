<script setup lang="ts">
import { ref } from 'vue';
import Welcome from './components/Welcome.vue';
import Name from './components/Name.vue';
import Brand from './components/Brand.vue';
import type { CoachName } from './types';
import Coach from './components/Coach.vue';

const stages = {
  Welcome,
  Name,
  Coach,
};

interface Profile {
  name?: string;
  coach?: CoachName;
}

const stage = ref<keyof typeof stages>('Welcome');
const profile = ref<Profile>({});

function changeStage(
  newStage: keyof typeof stages,
  newProfile: Profile,
) {
  stage.value = newStage;
  profile.value = {...profile.value, ...newProfile};
}
</script>

<template>
<main>
  <div class="container" v-if="stage !== 'Welcome'">
      <Brand />
  </div>
  <Transition>
    <component :is="stages[stage]" @change-stage="changeStage"></component>
  </Transition>
</main>

</template>

<style scoped>

</style>
