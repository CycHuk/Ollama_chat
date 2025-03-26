import axios from "axios";

const axiosInterface = axios.create({
    baseURL: import.meta.env.VITE_SERVER_URL,
    timeout: 10000,
    headers: {'accept': 'application/json', 'content-type': 'application/json'},
});

export default axiosInterface