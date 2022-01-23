import axios from 'axios'

const api_raw_material = axios.create({
<<<<<<< HEAD
    baseURL: 'http://192.168.1.118:8000/raw_material',
=======
    baseURL: 'http://192.168.1.128:8000/raw_material',
    timeout: 1000,
>>>>>>> c8e81824b6adab14ca5d383fe3da09253804012e
})

export{ api_raw_material }