import axios from 'axios'

const api_user = axios.create({
    baseURL: 'http://127.0.0.1:8000/user',
})

export{ api_user }