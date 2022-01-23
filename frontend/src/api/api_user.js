import axios from 'axios'

const api_user = axios.create({
<<<<<<< HEAD
    baseURL: 'http://192.168.1.118:8000/user',
=======
    baseURL: 'http://192.168.1.128:8000/user',
>>>>>>> c8e81824b6adab14ca5d383fe3da09253804012e
    timeout: 1000,
})

export{ api_user }