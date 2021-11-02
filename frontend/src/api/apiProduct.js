import axios from 'axios'

const apiProduct = axios.create({
    baseURL: 'http://127.0.0.1:8000/product',
    timeout: 1000,
})

export{ apiProduct }