import axios from 'axios'

const api_promotion = axios.create({
    baseURL: 'http://127.0.0.1:8000/promotion',
    timeout: 1000,
})

export{ api_promotion }