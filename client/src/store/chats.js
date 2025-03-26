import { defineStore } from 'pinia'
import {computed, ref, watchEffect} from "vue";
import axiosInterface from "@/api/index.js";

const useChatsStore = defineStore('chats', () => {
    const chats = ref([]);
    const active = ref(0);

    const activeChat = computed(() => chats.value[active.value]);

    const socketUrl  = computed(() => `${import.meta.env.VITE_WS}/ws/chat/${activeChat.value.id}`);

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

    loadChats();

    return { chats, createChat, deleteChat, activeChat, selectChat, active, socketUrl };
});

export default useChatsStore;
