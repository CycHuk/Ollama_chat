<script setup>
import useChatsStore from "@/store/chats.js";
import useMobileStore from "@/store/mobile.js";

const chatsStore = useChatsStore()
const mobileStore = useMobileStore()
</script>

<template>
  <div class="flex gap-2 border-b-2 border-zinc-700 items-center">
    <h2 class="text-3xl font-medium leading-tight">Чаты</h2>
    <button @click="chatsStore.createChat(); mobileStore.isChatList = false" class="flex items-center justify-center border-2 border-green-500 rounded-full text-green-500 text-sm p-0.5 leading-none mt-2">
      <i class="pi pi-plus"></i>
    </button>
  </div>

  <div v-for="chat in chatsStore.chats" class="flex gap-2 justify-between border-b-2 border-zinc-700 px-2 text-xl">
    <p v-if="chat.id !== chatsStore.activeChat.id" @click="chatsStore.selectChat(chat.id); mobileStore.isChatList = false" class="cursor-pointer text-gray-600">{{chat.title}}</p>
    <p v-else class="text-black">{{chat.title}}</p>
    <button @click="chatsStore.deleteChat(chat.id)" class="pi pi-times text-red-500 cursor-pointer"></button>
  </div>
</template>

<style scoped>

</style>