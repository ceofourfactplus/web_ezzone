import axios from "axios";

const api_customer = axios.create({
  baseURL: 'http://127.0.0.1:8000/customer',
  timeout: 1000,
});

export { api_customer };
