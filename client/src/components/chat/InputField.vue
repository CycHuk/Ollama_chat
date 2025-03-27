<script setup>
import {computed, ref} from "vue"
import useChatsStore from "@/store/chats.js";
import axiosInterface from "@/api/index.js";

const ChatStore = useChatsStore()

const inputField = ref("")

const sendMessage = async () => {
  if (inputField.value) {

    const text = inputField.value
    inputField.value = "";

    await axiosInterface.post("/messages/create", {id: ChatStore.activeChat.id, message: text}).then(r => {
      console.log("Successfully created");
    })

  } else {
    console.log("Сообщение пустое, ничего не отправлено.");
  }
};

</script>


<template>
  <div class="flex justify-between items-center w-full py-2">
    <input
        v-model="inputField"
        class="flex-1 px-4 py-2 bg-slate-50 border border-slate-500 rounded-lg focus:outline-none focus:border-slate-600"
        placeholder="Введите сообщение..."
    />
    <button
        @click="sendMessage"
        :class="ChatStore.activeChat && ChatStore.activeChat.can_user_write ? 'bg-blue-500 hover:bg-blue-600' : 'bg-stone-500'"
        class="ml-4 px-6 py-2  text-white font-semibold rounded-lg shadow-md  transition-all"
        :disabled="!ChatStore.activeChat || !ChatStore.activeChat.can_user_write"
    >
      Отправить
    </button>
  </div>
</template>

<style scoped>

</style>