<script setup>
import useChatsStore from "@/store/chats.js";
import useMessageStore from "@/store/message.js";
import MessageBlock from "@/components/message/MessageBlock.vue";

const messageStore = useMessageStore()
const userStore = useChatsStore()
</script>

<template>
  <div class="bg-slate-50 w-full h-full rounded-md p-2 flex flex-col overflow-auto">
    <div class="flex flex-col w-full items-center border-b-2 border-zinc-700 mb-2">
      <h2 class="text-xl font-medium leading-tight pb-2">{{ userStore.activeChat?.title }}</h2>
    </div>

    <div class="w-full  max-h-full h-full overflow-y-auto p-2">
      <div class="flex-1 w-ful h-full">
        <div v-for="message in messageStore.messages" :key="message.id" class="w-full">
          <MessageBlock :message="message.message" :writer="message.writer" />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>