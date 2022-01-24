import axios from 'axios'

const api_promotion = axios.create({
    baseURL: 'http://192.168.1.118:8000/promotion/',
})

export{ api_promotion }