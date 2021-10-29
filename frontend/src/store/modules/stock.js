// import auth from "axios"

export default {
  namespace: true,
  state:{
    stock_select:{
      id:1,
      name: '',
      minstock: 0,
      balance: 0,
      avg_price: 0,
      max_price: 0,
      min_price: 0,
      code: '',
      category_set:{
        name: '',
      },
      frequency_data: []
    },
  },
}