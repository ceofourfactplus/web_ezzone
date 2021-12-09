import axios from 'axios'

const apiPOS = axios.create({
    baseURL: 'http://127.0.0.1:8000/pos',
    timeout: 1000,
})

export{ apiPOS }