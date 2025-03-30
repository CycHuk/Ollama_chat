<script setup>
import Header from "@/components/Header.vue";
import ChatList from "@/components/chat/ChatList.vue";
</script>

<template>
  <div class="flex flex-col justify-between h-full p-2 bg-slate-200 border-2 rounded-md border-slate-400 drop-shadow-lg">
    <Header />
    <main class="flex justify-between h-full w-full overflow-auto my-2">
      <div class="w-72 bg-slate-50 rounded-md p-2 hidden md:block">
        <ChatList />
      </div>
      <RouterView />
    </main>
  </div>
</template>


<style scoped>

</style>