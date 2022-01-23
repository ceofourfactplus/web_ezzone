import axios from "axios";

const api_customer = axios.create({
<<<<<<< HEAD
  baseURL: 'http://192.168.1.118:8000/customer',
=======
  baseURL: 'http://192.168.1.128:8000/customer',
>>>>>>> c8e81824b6adab14ca5d383fe3da09253804012e
  timeout: 1000,
});

export { api_customer };
