import axios from "axios";

const api_pos = axios.create({
<<<<<<< HEAD
  baseURL: 'http://192.168.1.118:8000/pos',
=======
  baseURL: 'http://192.168.1.128:8000/pos',
>>>>>>> c8e81824b6adab14ca5d383fe3da09253804012e
});

export { api_pos };
