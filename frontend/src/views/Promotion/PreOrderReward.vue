<template>
    <div>
        <nav-app :url_name="'Redemption'" reward_menu="true">Pre-Order Reward</nav-app>
    <!-- SearchBlock -->
        <div class="row" style="max-width:672px;">
            <div class="col-10 w-100 BlockSearch">
                <SearchBar @search="search" /> 
            </div>
            <div class="col-2 w-100 BlockSelect">
                <select
                name="category"
                id="category"
                v-model="category_id"
                style="height: 45px; width: 137px;"
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
        </div>
            
    <!-- Header -->
        <div class="table-header" id="Header">
            <div class="row" 
            style="width: 672px;
            height:50px;
            margin: 0px;">
                <div class="col-1 w-100"></div>
                <div class="col-4 w-100" style="padding-left:30px;">Reward</div>
                <div class="col-2 w-100">Qty</div>
                <div class="col-3 w-100">Cust Name</div>
                <div class="col-2 w-100">Status</div>
            </div>

        </div>
    <!-- Item -->
            <div class="row table-item" id="BlockItem" style="line-height:50px;" v-for="item in rewards" :key="item.id">
                <div class="col-1" style="background-color:#717171;
                border-radius: 10px;
                width: 40px;
                height:40px;
                margin:5px;
                left:3px;
                position:relative;
                ">
                <img :src="require(`../../../../backend${item.reward_set.img}`)" alt="" style=";height: 40px;width: 40px;left:-11px;top:-9px;position:relative;"></div>
                <div class="col-4 w-100" style="text-align:left;">{{ item.reward_set.reward }}</div>
                <div class="col-2 w-100">{{ item.reward_set.qty }}</div>
                <div class="col-3 w-100">{{ item.customer_set.nick_name }}</div>
                <div class="col-2 w-100" style="padding:0px;"><img src="../../assets/icon/cooking-status.png" alt="" style="height:38px;width:100px;top:-4px;position:relative;"></div>
            </div>
    </div>
</template>

<script>
import NavApp from "../../components/main_component/NavApp.vue"
import SearchBar from "../../components/materials/SearchBar.vue"
import { api_promotion } from "../../api/api_promotion"

export default {  
  name: "PreOrderReward",
  components : {
      NavApp,
      SearchBar,
  },
  data() {
      return{
        rewards: [],
        temp_rewards: [],
      }
  },
  methods: {
      fetchRewards() {
        api_promotion.get("exchange-history/").then((response) => {
            console.log(response.data, "rewards");
            response.data.forEach((element) => {
                console.log(element.reward_set.is_pre_order, 'element')
                if (element.reward_set.is_pre_order) {
                    this.rewards.push(element)
                    this.temp_rewards.push(element)
                }
            })
        });
    },
      search(val) {
          console.log(val)
      },
  },
    beforeMount() {
        this.fetchRewards()
    }
};

</script>

<style scoped>
.BlockSearch {
    min-width: 615px;
    height: 45px;
    margin-left: 20px;
    margin-right: 20px;
    margin-top: 10px;
    margin-bottom: 20px;

}

.BlockSelect {

    position: relative;
    top: 9px;

}

#Header {
    width: 770px;
    height: 50px;
    margin-left: 24px;
    margin-right: 24px;
    margin-top: 10px;
    margin-bottom: 20px;
    color: #ffffff;
    position: relative;
    line-height:45px;
    font-size:26px;
    padding:0px;
}

#BlockItem {
    width: 672px;
    height: 50px;
    margin-left: 24px;
    margin-right: 24px;
    margin-top: 10px;
    position: relative;
    font-size: 23px;
    text-align: center;
    padding:0px;
}

</style>