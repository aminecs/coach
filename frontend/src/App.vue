<script setup lang="ts">
import { ref } from 'vue';
import Welcome from './Welcome.vue';
import Name from './Name.vue';
import Brand from './components/Brand.vue';
import type { CoachName, Profile } from './types';
import Coach from './Coach.vue';
import Primary from './Primary.vue';
import Motivation from './Motivation.vue';
import Goal from './Goal.vue';
import Complete from './Complete.vue';

const stages = {
  Welcome,
  Name,
  Coach,
  Motivation,
  Goal,
  Primary,
  Complete
};

const stage = ref<keyof typeof stages>('Welcome');
const defaultProfile: Profile = {
  name: 'Amine',
  coach: {
    name: "David Goggins",
    img: "/goggins-profile.png",
  },
  motivation: 'dfadjsf dsjfads;f jkjds;j fkdsj f',
  goal: {
    name: "5 kilometers",
    emoji: "🏃",
  }
}
const profile = ref<Profile>(defaultProfile);

function changeStage(
  newStage: keyof typeof stages,
  newProfile: Profile,
) {
  stage.value = newStage;
  profile.value = { ...profile.value, ...newProfile };
  console.log(JSON.parse(JSON.stringify(profile.value)));
}
</script>

<template>
  <main>
    <div class="small-container" v-if="stage !== 'Welcome'">
      <Brand />
    </div>
    <Transition>
      <component :is="stages[stage]" @change-stage="changeStage" :profile="profile"></component>
    </Transition>
  </main>

</template>

<style scoped></style>
