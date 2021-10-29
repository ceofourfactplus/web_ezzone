<template>
  <div class="container">
    <table class="table table-dark table-striped">
      <thead>
        <tr>
          <th>#</th>
          <th>Stock</th>
          <th>Amount</th>
          <th>Min Stock</th>
          <th>Avg Price</th>
          <th>Detail</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in to_buy_data" :key="item.id">
          <td>{{ index }}</td>
          <td>{{ item.name }}</td>
          <td>{{ item.amount }}</td>
          <td>{{ item.minstock }}</td>
          <td>{{ item.avg_price }}</td>
          <td><button class="btn btn-danger">detail</button></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import apiStock from "../../api/ApiStock.js";

export default {
  name: 'Tobuy',
  data() {
    return { 
      to_buy_data:[]
    }
  },
  mounted(){
    apiStock.get("to-buy").then((response)=>{
      this.to_buy_data = response.data
      console.log(this.to_buy_data)
    })
  }
};
</script>

<style>
</style>