import { defineStore } from 'pinia'
import {computed, nextTick, ref, watch} from "vue";
import axiosInterface from "@/api/index.js";
import { useWebSocket } from "@vueuse/core";

const useChatsStore = defineStore('chats', () => {
    const chats = ref([]);
    const active = ref(0);
    let socket = null;

    const activeChat = computed(() => chats.value[active.value]);

    const socketUrl = computed(() =>
        activeChat.value?.id
            ? `${import.meta.env.VITE_WS}/ws/chat/${activeChat.value.id}`
            : ""
    );

    watch(socketUrl, (newUrl) => {
        if (socket) {
            socket.close();
            socket = null;
        }

        if (newUrl) {
            socket = new WebSocket(newUrl);

            socket.onopen = () => {
                console.log("WebSocket подключен");
            };

            socket.onmessage = (event) => {
                console.log("Новое сообщение:", event.data);

                const chat = JSON.parse(event.data);

                const index = chats.value.findIndex(c => c.id === chat.id);
                if (index !== -1) {
                    chats.value[index] = { ...chat };
                }

            };

            socket.onerror = (error) => {
                console.error("Ошибка WebSocket:", error);
            };

            socket.onclose = () => {
                console.log("WebSocket закрыт");
            };
        }
    }, { immediate: true });

    const saveChats = () => {
        localStorage.setItem("chats", JSON.stringify(chats.value.map(chat => chat.id)));
    };

    const createChat = async () => {
        await axiosInterface.post("chat/create").then(r => {
            chats.value.unshift(r.data);
            saveChats();
        }).catch(e => {
            console.error(e);
        });
    };

    const loadChats = async () => {
        const savedId = JSON.parse(localStorage.getItem("chats"));
        if (savedId && savedId.length > 0) {

            axiosInterface.post("chats", {id: savedId}).then(r => {
                chats.value = r.data;
            })

        } else {
            await createChat();
        }

    };

    const deleteChat = async (id) => {
        const chatIndex = chats.value.findIndex(chat => chat.id === id);

        if (chatIndex === active.value) {
            active.value = 0;
        }

        await axiosInterface.delete("chat", { data: { id } })
            .then(() => {
                chats.value = chats.value.filter(chat => chat.id !== id);
                saveChats();
            })
            .catch(e => {
                console.error(e);
                saveChats();
            });

        if(chats.value.length === 0) {
            await createChat();
        }
    };

    const selectChat = (id) => {
        const chatIndex = chats.value.findIndex(chat => chat.id === id);
        if (chatIndex !== -1) {
            active.value = chatIndex;
        } else {
            console.error(`Chat with id ${id} not found`);
        }
    };

    const scrollChat  = () => {
        nextTick(() => {
            const block = document.getElementById('chat');

            block.scrollTop = block.scrollHeight;
        })
    }

    loadChats();


    return { chats, createChat, deleteChat, activeChat, selectChat, active, scrollChat };
});

export default useChatsStore;
