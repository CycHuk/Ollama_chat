<script setup>
import InputField from "@/components/chat/InputField.vue";
import MainField from "@/components/chat/MainField.vue";
import useChatsStore from "@/store/chats.js";

const ChatsStore = useChatsStore()

</script>

<template>
  <div class="w-full flex flex-col justify-between mx-2">
    <MainField />
    <InputField />
  </div>
</template>

<style scoped>

</style>