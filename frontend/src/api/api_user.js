import axios from 'axios'

const api_user = axios.create({
    baseURL: 'http://192.168.1.118:8000/user',
    timeout: 1000,
})

export{ api_user }