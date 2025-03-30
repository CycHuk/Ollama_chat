<script setup>
import useMobileStore from "@/store/mobile.js";

const mobileStore = useMobileStore()
</script>

<template>
  <header class="flex flex-row justify-start items-center gap-2 lg:m-4  pb-1 md:pb-3 border-b-2 border-gray-700">
    <button @click="mobileStore.isChatList = !mobileStore.isChatList" class="mt-1 ml-2 md:hidden">
      <i :class="mobileStore.isChatList ? 'pi pi-times' : 'pi pi-align-justify'"></i>
    </button>
    <h1 class="font-extrabold text-2xl tracking-wide">Ollama Chat</h1>
  </header>
</template>

<style scoped>
</style>