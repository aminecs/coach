export const coachInfo = {
  goggins: {
    name: "David Goggins",
    img: "/goggins-profile.png",
  },
  dame: {
    name: "Dame Judi Dench",
    img: "/dame-profile.png",
  },
  custom: {
    name: "Custom",
    img: "/custom-profile.png",
  },
};

export type CoachName = keyof typeof coachInfo;

// export type Goal = "5 kilometers" | "10 kilometers" | "Marathon" | "Custom";

export const goalInfo = {
  "5k": {
    name: "5k",
    emoji: "🏃",
    desc: "A great challenge for beginner to intermindate runners.",
  },
  "10k": {
    name: "10k",
    emoji: "🏃",
    desc: "Ready for the next level up? Challenge yourself with a 10k.",
  },
  marathon: {
    name: "Marathon",
    emoji: "🚶",
    desc: "Go big or go home. Ready for a marathon, champ?",
  },
  custom: {
    name: "Custom",
    emoji: "🔧",
    desc: "Set your own goal.",
  },
};

export type GoalName = keyof typeof goalInfo;

export interface Profile {
  name?: string;
  coach?: {
    name: string;
    img: string;
  };
  motivation?: string;
  goal?: {
    name: string;
    emoji: string;
    desc: string;
  };
}
