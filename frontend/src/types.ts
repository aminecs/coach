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

export type Goal = "5 kilometers" | "10 kilometers" | "Marathon" | "Custom";

export interface Profile {
  name?: string;
  coach?: {
    name: string;
    img: string;
  };
  motivation?: string;
  goal?: Goal;
}
