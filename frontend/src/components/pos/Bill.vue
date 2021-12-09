<template>
  <table class="table table-dark table-striped">
    <thead>
      <tr>
        <th>#</th>
        <th>name</th>
        <th>topping</th>
        <th>flavour level</th>
        <th>size</th>
        <th>amount</th>
        <th>price</th>
        <th>edit</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(product, index) in order.cart" :key="index" style="height:20px;">
        <th>{{ product.product.code }}</th>
        <th>{{ product.product.name }}</th>
        <th>
          <div v-if="product.topping.length != 0">
            <div v-for="topping in product.topping" :key="topping.id">
              {{ topping.name }}
            </div>
          </div>
          <div v-else>
            -
          </div>
        </th>
        <th>{{ sweet(product.flavour_level) }}</th>
        <th>{{ product.size}}</th>
        <th>{{ product.amount }}</th>
        <th>{{ product.total_price }}</th>
        <th><button class="btn btn-danger">edit</button></th>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  props: ["order"],
  methods:{
    sweet(s){
      if(s=='none'){
        return "no"
      }if(s=='low'){
        return "+"
      }if(s=='medium'){
        return "++"
      }if(s=='very'){
        return "+++"
      }
    }
  }
};
</script>

<style>
</style>