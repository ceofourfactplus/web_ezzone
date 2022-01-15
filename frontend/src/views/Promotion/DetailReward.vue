<template>
    <div>
        <nav-app>Detail Reward</nav-app>

        <!-- AreaBlockItem -->
        <div class="table-item"
            style="margin-left: 24px;
            margin-right: 24px;
            margin-top: 20px;
            margin-bottom: 20px;
            border-radius:20px;
            height: 820px;
            width: 672px;">

            <!-- Select Bar -->
            <div class="row BlockItem">
                
                <div class="col-6 w-100">
                <select
                name="category"
                id="category"
                v-model="category_id"
                style="background:#717171;height:50px;width:282px;"
                >
                <!-- <option
                    v-for="category in categories"
                    :key="category.id"
                    :value="category.id"
                >
                    {{ category.name }}
                </option> -->
                </select>
                </div>
                <div class="col-6 w-100" style="padding:0px;">
                    <div class="StatusItem"><b>Redeem</b></div>
                </div>
            </div>
            <div class="row BlockImg">
                
                <div class="col-6 w-100">
                <img src="../../assets/img/BG.png" alt="" style="width:282px;height: 298px;">
                </div>
                <div class="col-6 w-100 BlockRedeemPoint" style="padding:0px;">
                    <div class="RedeemPointItem">
                        <dir style="height:60px;margin:0px;padding:0px;line-height:55px;"><b>Redeem Point</b></dir>
                        <div class="table-item BlockPoint"><b>20</b></div>
                        <dir style="height:60px;margin:0px;padding:0px;line-height:55px;font-size:28px;">Total Value 500B.</dir>
                    </div>
                </div>
            </div>
            <div class="row AreaDescription">
                <div  class="col-12 w-100" style="height:50px;"><b>Description :</b></div>
                <div  class="col-12 w-100 BlockDescription" ></div>

            </div>
        
        
        </div>


    </div>

</template>

<script>
export default {  
  name: "DetailReward",
  components : {
      NavApp,
      SearchBar
      
  },
  data() {
      return{
        
      }
  },
  methods: {
      search(val) {
          console.log(val)
      }
  },

};

import NavApp from "../../components/main_component/NavApp.vue"
import SearchBar from "../../components/materials/SearchBar.vue"

</script>

<style scoped>

.BlockItem {
    width: 672px;
    position: relative;
    font-size: 23px;
    text-align: center;
    padding:0px;
    margin:0px;
    top: 30px;
}

.StatusItem {
    color: #EA7C69;
    font-size: 30px;
    height: 50px;
    width: 308px;
    padding: 10px;
    border-radius: 10px;
    border: 2px solid #EA7C69;
    line-height: 20px;
    margin-left:0px;
    margin-right:20px;
}

.BlockImg {
    width: 672px;
    position: relative;
    font-size: 23px;
    text-align: center;
    padding:0px;
    margin:0px;
    top: 60px;
    
}

.RedeemPointItem {
    color: #fff;
    font-size: 30px;
    height: 298px;
    width: 308px;
    padding-left:  2px;
    padding-right: 2px;
    border-radius: 30px;
    background-color:  #EA7C69;
    line-height: 20px;
    margin-left:0px;
    margin-right:20px;
}

.BlockPoint {
    height: 178px;
    margin: 0px;
    border-radius: 0px;
    font-size: 106px;
    line-height:160px;

}

.AreaDescription {
    margin: 20px;
    color: aliceblue;
    width: 615px;
    position: relative;
    font-size: 30px;
    text-align: left;
    padding:0px;
    margin-left:27px;
    top: 70px;

}

.BlockDescription {

    background-color: rgb(168, 190, 190);
    width: 100%;
    height: 305px;
    border-radius: 20px;
    position: relative;
    font-size: 30px;
    text-align: left;
    padding:0px;

}

</style>