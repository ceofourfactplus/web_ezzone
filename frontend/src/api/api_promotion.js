import axios from 'axios'

const api_promotion = axios.create({
    baseURL: 'http://127.0.0.1:8000/promotion',
})

export{ api_promotion }