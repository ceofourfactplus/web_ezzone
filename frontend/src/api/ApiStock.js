import axios from 'axios'

const apiStock = axios.create({
    baseURL: 'http://127.0.0.1:8000/stock',
    timeout: 1000,
})

export{ apiStock }
