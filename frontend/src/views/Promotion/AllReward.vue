<template>
    <div>
        <nav-app :url_name="'Redemption'" :reward_menu="true">All Reward</nav-app>

        <!-- Search Bar -->
        <div class="row" style="max-width:772px; margin:0px;">
            <div class="col-7 w-100 BlockSearch">
                <SearchBar @search="serchByTyping"/> 
            </div>
            <div class="col-5 w-100 BlockUserPoints">
                <div class="row" style="padding: 0px;width: 266px;margin-right: 0px;margin-left: 0px;line-height:35px;">
                    <div class="col-2 w-100" style="margin-left:-15px;margin-top:-2px;"><img src="../../assets/icon/user-icon.png" alt=""></div>
                    <div class="col-5 w-100 ItmeUserPoints">{{ $store.state.promotion.customer.nick_name }}</div>
                    <div class="col-1 w-100" style="max-width:2px;">:</div>
                    <div class="col-2 w-100 ItmeUserPoints" style="left:-20px;" v-if="$store.state.promotion.customer_point.length != 0">{{ $store.state.promotion.customer_point[0].point }}</div>
                    <div class="col-2 w-100 ItmeUserPoints" style="left:-20px;" v-else>0</div>
                    <div class="col-2 w-100 ItmeUserPoints">Point</div>

                </div>

            </div>
        </div>

        <!-- AreaBlockItem -->
        <!-- <div class="col-12"
        style="margin-left: 24px;
        margin-right: 24px;
        margin-top: 20px;
        margin-bottom: 20px;
        border-radius:20px;
        height: 100%px;
        width: 672px;"> --> -->
        <!-- BlockItme -->

            <div class="row" style="width: 97%; margin-left: 20px;">
                <div class="col-3 BlockItem" v-for="reward in rewards" :key="reward.id">
                    <div class="PictureItem">
                        <img :src="reward.img" alt="" style="height: 120px;width: 120px;">
                    </div>
                    <div class="FontItem">{{ reward.reward }}</div>
                    <div class="FontItem">{{ reward.point }} Points</div>
                    <div class="SeeDetail" @click="see_detail(reward)">See Details</div>
                </div>
            </div>   
        </div>
</template>

<script>
import { api_promotion} from "../../api/api_promotion"

export default {  
  name: "AllReward",
  components : {
      NavApp,
      SearchBar
  },
  data() {
      return{
        rewards: [],
        temp_rewards: [],
      }
  },
  methods: {
      fetchRewards() {
        api_promotion.get("reward/").then((response) => {
            console.log(response.data, "rewards");
            this.rewards = response.data;
            this.temp_rewards = response.data;
        });
    },
    see_detail(reward) {
        this.$store.state.promotion.reward_detail = reward
        this.$router.push({ name: "RewardName"})
    },
    serchByTyping(val) {
      var temp = [];
      if (val == "") {
        this.rewards = this.temp_rewards;
      } else {
        this.temp_rewards.forEach((element) => {
          if (element.reward.indexOf(val) + 1 != 0) {
            temp.push(element);
          }
        });
        this.rewards = temp;
      }
    },
      search(val) {
          console.log(val)
      },
  },
  beforeMount() {
      this.fetchRewards()
  }

};

import NavApp from "../../components/main_component/NavApp.vue"
import SearchBar from "../../components/materials/SearchBar.vue"

</script>

<style scoped>

.BlockSearch {
    height: 45px;
    margin-left: 20px;
    margin-right: 20px;
    margin-top: 10px;
    margin-bottom: 20px;
}

.BlockUserPoints {
    color:#fff;
    font-size: 18px;
    background-color: #303344;
    height: 45px;
    margin-left: 20px;
    margin-right: 20px;
    margin-top: 10px;
    margin-bottom: 20px;
    padding: 0px;
    border: 2px solid #EA7C69;
    border-radius: 20px;


}

.ItmeUserPoints {

    padding: 0px;
    text-align: left;

}

.BlockItem {
    padding-top: 10px;
    width: 90%;
    height: 240px;
    border-radius: 10px;
    background-color: #303344;
}

.PictureItem {
    height: 120px;
}

.FontItem {
    color:#fff;
    font-size: 20px;
}

.SeeDetail {
    color: #EA7C69;
    border: 2px solid #EA7C69;
    border-radius: 20px;
    height: 30px;
    width: 110px;
    margin: auto; 
    margin-top: 10px; 
}

</style>