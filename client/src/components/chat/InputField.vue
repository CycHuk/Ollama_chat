<script setup>
import {computed, ref} from "vue"
import useChatsStore from "@/store/chats.js";
import axiosInterface from "@/api/index.js";

const ChatStore = useChatsStore()

const isInputEnabled = computed(() =>
    ChatStore.activeChat && ChatStore.activeChat.can_user_write !== undefined
        ? ChatStore.activeChat.can_user_write
        : false
)

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
        :disabled="!isInputEnabled"
    />
    <button
        @click="sendMessage"
        class="ml-4 px-6 py-2 bg-blue-500 text-white font-semibold rounded-lg shadow-md hover:bg-blue-600 transition-all"
    >
      Отправить
    </button>
  </div>
</template>

<style scoped>

</style>