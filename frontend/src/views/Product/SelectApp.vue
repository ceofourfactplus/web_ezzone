<template>
  <div class="container">
    <div class="row mt-3">
      <button @click="link('Product')" style="color: black" class="circle bg-warning center">
       All Product
      </button>
      <button @click="link('Topping')" style="color: black" class="circle bg-light center">
        Topping
      </button>
      <button @click="link('SaleChannel')"  class="circle-s bg-primary center">
        Sale Channel
      </button>
    </div>
    <div class="row mt-5">
      <button class="circle bg-success center" @click="link('Category')">
        Category
      </button>
      <button class="circle bg-danger center " @click="link('TypeTopping')">
       Set Topping
      </button>
    </div>
  </div>
</template>

<script>
export default {
  methods:{
    link(to){
      this.$router.push({name:to})
      this.$store.state.product.select_app = to
    }
  }
};
</script>

<style scoped>

.circle {
  width: 300px;
  height: 300px;
  line-height: 70%;
  border-radius: 50%;
  font-size: 50px;
  color: #fff;
  text-align: center;
  background: #fa7e7edd;
  transition: width 1s, height 1s, font-size 1s , font-weight 1s;
}

.circle:hover{
  width: 250px;
  height: 250px;
  font-size: 35px;
  font-weight: bold
}

.circle-s {
  width: 300px;
  height: 300px;
  line-height: 70%;
  border-radius: 50%;
  font-size: 45px;
  color: #fff;
  text-align: center;
  background: #fa7e7edd;
  transition: width 1s, height 1s, font-size 1s , font-weight 1s;
}

.circle-s:hover{
  width: 250px;
  height: 250px;
  font-size: 35px;
  font-weight: bold
}
.center {
  margin: auto;
  padding: 10px;
}
</style>