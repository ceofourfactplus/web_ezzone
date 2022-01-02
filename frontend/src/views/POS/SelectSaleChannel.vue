<template>
  <div>
    <nav-app>Sale Channel</nav-app>
    <div class="center">
      <div class="row">
        <div v-for="channel in sale_channel" :key="channel.id" @click="$router.push({name:'KeyOrder',params:{sale_channel_id:channel.id}})" class="col-6 mb-3">
          <img :src="channel.img" alt="">
          {{channel.sale_channel}}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { api_product } from '../../api/api_product';
import NavApp from "../../components/main_component/NavApp.vue";
export default {
  components: { NavApp },
  mounted(){
    api_product.get('sale-channel/').then((response)=>{
      this.sale_channel = response.data
    })
  },
  data(){
    return{
      sale_channel:[]
    }
  }
};
</script>

<style scoped>
.center{
  margin: auto;
  width: 75%;
  margin-top: 40px;
}
.col-6{
  margin:auto;
}
img{
  width: 120px;
  height: 120px;
  border-radius: 10px;
}
div{
  font-size: 30px;
  color:#fff;
  font-weight: 700;
}
</style>