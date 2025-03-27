import {defineStore} from "pinia"
import {computed, ref, watch} from "vue";
import useChatsStore from "@/store/chats.js";
import axiosInterface from "@/api/index.js";


const useMessageStore = defineStore("messageStore", () => {
    const messages = ref([]);
    const ChatStore = useChatsStore();
    let socket = null;

    const socketUrl = computed(() =>
        ChatStore.activeChat?.id
            ? `${import.meta.env.VITE_WS}/ws/message/${ChatStore.activeChat.id}`
            : ""
    );

    watch(messages, (newUrl) => {
        ChatStore.scrollChat()
    })

    watch(
        () => ChatStore.activeChat,
        async (newVal) => {
            if (newVal) {
               await loadMessages(newVal.id);
            }
        },
        { immediate: true }
    );

    watch(socketUrl, (newUrl) => {
        if (socket) {
            socket.close();
            socket = null;
        }

        if (newUrl) {
            socket = new WebSocket(newUrl);

            socket.onopen = () => {
                console.log("Message WebSocket подключен");
            };

            socket.onmessage = (event) => {
                const message= JSON.parse(event.data);

                if (message.writer === "bot" && messages.value.at(-1).writer === "bot") {
                    messages.value.pop();
                }

                messages.value.push(message);
                ChatStore.scrollChat()
            };

            socket.onerror = (error) => {
                console.error("Message Ошибка WebSocket:", error);
            };

            socket.onclose = () => {
                console.log("Message WebSocket закрыт");
            };
        }
    }, { immediate: true });

    const loadMessages = async (chatId) => {
        await axiosInterface.post("/messages", {id: chatId}).then((response) => {
            messages.value = response.data.sort((a, b) => a.id - b.id);
        });
    };

    return { messages };
});

export default useMessageStore;