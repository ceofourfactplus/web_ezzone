import axios from 'axios'

const api_user = axios.create({
<<<<<<< HEAD
    baseURL: 'http://192.168.1.128:8000/user',
=======
    baseURL: 'http://192.168.1.118:8000/user',
>>>>>>> 31e8f32076cd7b14cf48ff679a20298ed462c551
    timeout: 1000,
})

export{ api_user }