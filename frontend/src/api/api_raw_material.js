import axios from 'axios'

const api_raw_material = axios.create({
    baseURL: 'http://192.168.1.128:8000/raw_material',
    timeout: 1000,
})

export{ api_raw_material }