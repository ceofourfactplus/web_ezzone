<template>
  <div id="main-create" class="container">
    <!-- navbar create -->
    <nav-product>{{ $store.state.product.select_app }}</nav-product>

    <router-view></router-view>
  </div>
</template>

<script>
import { mapState} from 'vuex'
import NavProduct from "../../components/NavProduct.vue";
export default {
  components: { NavProduct },
  computed:mapState(['product']),
  name: "MainCreate",
  data() {
    return{ 
      select_files:''
    }
  },
  methods: {
    ChangeFile(event){
      this.select_files = event.target.files[0]
    },
    // uploads(){
    //   axios.get("")
    // }
  }
};
</script>

<style>
</style>