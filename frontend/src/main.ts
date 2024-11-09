import "./assets/main.scss";

import { createApp } from "vue";
import App from "./App.vue";
import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faPlay, faPause, faStop } from "@fortawesome/free-solid-svg-icons";
import { faSpotify } from "@fortawesome/free-brands-svg-icons";

library.add(faSpotify, faPlay, faPause, faStop);

createApp(App).component("fa-icon", FontAwesomeIcon).mount("#app");
