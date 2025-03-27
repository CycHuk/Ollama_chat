<script setup>
import { marked } from "marked";
import { computed } from "vue";

const props = defineProps({
  writer: String,
  message: String
});

const compiledMarkdown = computed(() => marked(props.message || ""));
</script>

<template>
  <div :class="writer === 'user' ? 'text-right' : 'text-left'" class="mb-2">
    <div
        :class="writer === 'bot' ? 'bg-gray-200' : 'bg-blue-500 text-white'"
        class="inline-block rounded-xl shadow-lg p-2 flex items-center justify-center max-w-lg"
    >
      <h2 v-if="writer !== 'user'" class="text-sm font-semibold">{{ writer }}</h2>
      <p class="mb-1" v-html="compiledMarkdown"></p>
    </div>
  </div>
</template>
