import axios from 'axios'

const api_product = axios.create({
    baseURL: 'http://127.0.0.1:8000/product',
    // timeout: 4000,
})

export{ api_product } 