import axios from 'axios'

const api_raw_material = axios.create({
    baseURL: 'http://192.168.1.118:8000/raw_material',
})

export{ api_raw_material }