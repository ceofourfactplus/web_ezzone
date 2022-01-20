import axios from "axios";

const api_pos = axios.create({
  baseURL: 'http://127.0.0.1:8000/pos',
});

export { api_pos };
