<script setup>
import InputField from "@/components/chat/InputField.vue";
import MainField from "@/components/chat/MainField.vue";
import { useWindowSize } from "@vueuse/core";
import useMobileStore from "@/store/mobile.js";
import ChatList from "@/components/mobile/ChatList.vue";
import {computed} from "vue";

const mobileStore = useMobileStore()

const { width } = useWindowSize();
const isMobile = computed(() => width.value < 768);

</script>

<template>
  <div v-if="mobileStore.isChatList  && isMobile" class="w-full">
    <ChatList />
  </div>
  <div v-else class="w-full flex flex-col justify-between mx-1 md:mx-2 max-h-full">
    <MainField />
    <InputField />
  </div>
</template>

<style scoped>

</style>