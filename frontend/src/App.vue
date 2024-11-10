<script setup lang="ts">
import { computed, ref, useTemplateRef } from 'vue';
import Welcome from './Welcome.vue';
import Name from './Name.vue';
import Brand from './components/Brand.vue';
import { socket, type Profile } from './types';
import Coach from './Coach.vue';
import Primary from './Primary.vue';
import Motivation from './Motivation.vue';
import Goal from './Goal.vue';
import Complete from './Complete.vue';
import Leaderboard from './Leaderboard.vue';

const stages = {
  Welcome,
  Name,
  Coach,
  Motivation,
  Goal,
  Primary,
  Complete,
  Leaderboard
};

const stage = ref<keyof typeof stages>('Welcome');
const defaultProfile: Profile = {
  name: 'Amine',
  coach: {
    name: "David Goggins",
    img: "/goggins-profile.png",
  },
  motivation: 'I want a house, to be a unicorn founder and a bunch of cash.',
  goal: {
    name: "5 kilometers",
    emoji: "🏃",
    desc: "A great challenge for beginner to intermindate runners."
  }
}
const profile = ref<Profile>(defaultProfile);

const comp = useTemplateRef('component');

const indicator = useTemplateRef('indicator');

async function changeStage(
  newStage: keyof typeof stages,
  newProfile: Profile,
) {
  indicator.value?.classList.remove('recording');
  stage.value = newStage;
  profile.value = { ...profile.value, ...newProfile };
  console.log(JSON.parse(JSON.stringify(profile.value)));
  let param = undefined;
  switch (newStage) {
    case 'Name':
      param = 'name';
      break;
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
  }
}

socket.on('name', (newName) => {
  console.log(`name ${newName}`);
  comp.value?.setName(newName);
});

socket.on('motivation', (newMotivation) => {
  console.log(`motivation ${newMotivation}`);
  comp.value?.fillMotivation(newMotivation);
});

const recording = ref(false);
const recordingText = computed(() => {
  if (recording.value) {
    return "Voice control active";
  } else {
    return "Voice control off";
  }
});
const showVoiceControl = computed(() => {
  return stage.value === 'Name' || stage.value === 'Coach' || stage.value === 'Motivation' || stage.value === 'Goal';
});

socket.on('recording', () => {
  recording.value = true;
  indicator.value?.classList.add('recording');
});

socket.on('stopRecording', () => {
  recording.value = false;
  indicator.value?.classList.remove('recording');
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
    <div class="start-indicator" v-if="stage === 'Welcome'">
      <img src="/indicator.png">
      <div>
        Say 'Hey Coach' to activate voice control
      </div>
    </div>
    <div class="indicator" v-if="showVoiceControl">
      <div ref="indicator">
        <img :src="!recording ? '/indicator.png' : 'indicator-active.png'">
        {{ recordingText }}
      </div>
    </div>
  </main>
</template>

<style scoped>
.indicator {
  display: flex;
  justify-content: center;

  img {
    width: 2rem;
    margin-right: 0.5rem;
  }

  div {
    font-size: 0.9rem;
    font-weight: 100;
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 2rem;
    padding: 0.5rem 0.8rem;
    /* width: 4rem;
    height: 4rem; */
    display: flex;
    align-items: center;
    justify-content: center;
    /* -webkit-backdrop-filter: blur(8px);
    backdrop-filter: blur(8px);
    background-color: rgba(255, 255, 255, 0.3); */
  }

  .recording {
    background-color: white;
    color: black;
  }
}

.start-indicator {
  img {
    width: 3rem;
    margin: 0.5rem;
  }

  font-size: 0.9rem;
}
</style>
