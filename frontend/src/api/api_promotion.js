import axios from 'axios'

const api_promotion = axios.create({
    baseURL: 'http://192.168.1.118:8000/promotion',
    timeout: 1000,
})

export{ api_promotion }