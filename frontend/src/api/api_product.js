import axios from 'axios'

const api_product = axios.create({
    baseURL: 'http://192.168.1.128:8000/product',
    timeout: 1000,
})

export{ api_product } 