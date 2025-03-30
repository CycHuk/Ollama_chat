import {defineStore} from 'pinia'
import {ref} from "vue";

const useMobileStore = defineStore('mobile', () => {
    const isChatList = ref(false)

    return {isChatList}
})

export default useMobileStore