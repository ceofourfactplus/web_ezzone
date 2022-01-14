import axios from 'axios'

const api_raw_material = axios.create({
    baseURL: '127.0.0.1:8000/raw_material',
    timeout: 1000,
})

export{ api_raw_material }