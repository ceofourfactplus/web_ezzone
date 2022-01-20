import axios from "axios";

const api_pos = axios.create({
  baseURL: 'http://192.168.1.118:8000/pos',
});

export { api_pos };
