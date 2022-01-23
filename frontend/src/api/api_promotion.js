import axios from 'axios'

const api_promotion = axios.create({
<<<<<<< HEAD
    baseURL: 'http://192.168.1.118:8000/promotion',
=======
    baseURL: 'http://192.168.1.128:8000/promotion',
>>>>>>> c8e81824b6adab14ca5d383fe3da09253804012e
})

export{ api_promotion }