import {createRouter, createWebHistory} from "vue-router"

const routers = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            component: () => import("@/layouts/ChatLayout.vue"),
            children: [
                {
                    path: "/",
                    name: "Chat",
                    component: () => import("@/pages/ChatView.vue"),
                }
            ]
        }
    ]
})

export default routers