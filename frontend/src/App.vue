<script setup lang="ts">
import { ref, useTemplateRef } from 'vue';
import Welcome from './Welcome.vue';
import Name from './Name.vue';
import Brand from './components/Brand.vue';
import { socket, type Profile } from './types';
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
    desc: "A great challenge for beginner to intermindate runners."
  }
}
const profile = ref<Profile>(defaultProfile);

const comp = useTemplateRef('component');

async function changeStage(
  newStage: keyof typeof stages,
  newProfile: Profile,
) {
  stage.value = newStage;
  profile.value = { ...profile.value, ...newProfile };
  console.log(JSON.parse(JSON.stringify(profile.value)));
  let param = undefined;
  switch (newStage) {
    case 'Name':
      param = 'name';
      break;
    // case 'Coach':
    //   param = 'coach';
    //   break;
    // case 'Goal':
    //   param = 'goal'
    //   break;
    case 'Motivation':
      param = 'motivation'
      break;
  }
  if (param !== undefined) {
    await fetch("http://127.0.0.1:8200/api/audio?" + new URLSearchParams({ param }), {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    });
    // const res = await resp.text();
    // console.log(res);
    // switch (newStage) {
    //   case 'Name':
    //     comp.value?.setName(res);
    //     break;
    //   // case 'Coach':
    //   //   comp.value?.clickGoggins();
    //   //   break;
    //   case 'Motivation':
    //     comp.value?.fillMotivation(res);
    //     break;
    // }
  }
}

socket.on('name', (newName) => {
  console.log(`name ${newName}`);
});

socket.on('motivation', (newMotivation) => {
  console.log(`motivation ${newMotivation}`);
});

</script>

<template>
  <main>
    <div class="small-container" v-if="stage !== 'Welcome'">
      <Brand />
    </div>
    <Transition>
      <component :is="stages[stage]" @change-stage="changeStage" :profile="profile" ref="component"></component>
    </Transition>
  </main>

</template>

<style scoped></style>
