import axios from "axios";

const api_customer = axios.create({
  baseURL: 'http://192.168.1.118:8000/customer',
  timeout: 1000,
});

export { api_customer };
