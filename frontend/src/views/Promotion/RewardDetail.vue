<template>
  <div>
    <nav-app :url_name="'Promotion'" :save="true" @save="edit">Reward Detail</nav-app>
    <div class="card-content">
      <div class="row">
        <!-- Left Side -->
        <div class="col-8 w-100" style="margin-left: 38px;">
          <!-- Input -->
          <div class="row" style="margin-top: 15px">
            <div class="col-12 w-100">
              <input type="text" class="input-top" placeholder="Reward Name" v-model="reward_item.reward" />
            </div>
          </div>
          <!-- Value -->
          <div class="row" style="margin-top: 15px">
            <div class="col-8 w-100">
              <div class="row">
                <div class="col-4 w-100 txt">Value</div>
                <div class="col-1 w-100 txt">:</div>
                <div class="col-5 w-100">
                  <input
                    type="text"
                    class="input-promotion"
                    style="width: 298px"
                    v-model="reward_item.value"
                  />
                </div>
              </div>
            </div>
          </div>
          <!-- Cost -->
          <div class="row" style="margin-top: 15px">
            <div class="col-8 w-100">
              <div class="row">
                <div class="col-4 w-100 txt">Cost</div>
                <div class="col-1 w-100 txt">:</div>
                <div class="col-5 w-100">
                  <input
                    type="text"
                    class="input-promotion"
                    style="width: 298px"
                    v-model="reward_item.cost"
                  />
                </div>
              </div>
            </div>
          </div>
          <!-- Qty -->
          <div class="row" style="margin-top: 15px">
            <div class="col-8 w-100">
              <div class="row">
                <div class="col-4 w-100 txt">Qty</div>
                <div class="col-1 w-100 txt">:</div>
                <div class="col-5 w-100">
                  <input
                    type="text"
                    class="input-promotion"
                    style="width: 298px"
                    v-model="reward_item.qty"
                  />
                </div>
              </div>
            </div>
          </div>
          <!-- Point -->
          <div class="row" style="margin-top: 15px">
            <div class="col-8 w-100">
              <div class="row">
                <div class="col-4 w-100 txt">Point</div>
                <div class="col-1 w-100 txt">:</div>
                <div class="col-5 w-100">
                  <input
                    type="text"
                    class="input-promotion"
                    style="width: 298px"
                    v-model="reward_item.point"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Right Side -->
        <div class="col-4 w-100">
          <div
            class="col-12 w-100"
            style="color: white; margin: 15px 10px 0px 0px"
          >
            Status&nbsp;:&nbsp; <Switch style="top: 9px" :value="reward_item.status" @switch="switch_active"/>
          </div>
          <div class="col-12 w-100" style="margin-top: 30px">
            <!-- Image -->
            <label id="select_img" for="file" style="margin-top: 0px">
              <img :src="show_img" class="image" v-if="show_img != null" />
              <img :src="reward_item.img" class="image" v-else />
            </label>
            <input
              type="file"
              @change="onFileChange"
              style="display: none"
              id="file"
              class="raw-image"
            />
          </div>
          <div class="col-12">
            <div class="checkbox-orange">
              <input
                type="checkbox"
                style="display: inline-block; top: 5px"
                v-model="reward_item.is_pre_order"
                class="ms-2"
              />
              <label
                class="ms-3"
              > Pre-order </label>
            </div>
          </div>
        </div>
      </div>
      <textarea
        style="
          width: 690px;
          height: 115px;
          border-radius: 10px;
          background: #717171;
          margin-top: 20px;
        "
        cols="30"
        rows="10"
        placeholder="Description"
        v-model="reward_item.description"
      ></textarea>
    </div>
    <div class="table" style="margin-top: 10px;">
      <div class="table-header" style="width: 762px; margin-left: -10px;">
        <div
          class="row"
          style="font-size: 24px; font-weight: bold; color: white"
        >
          <div class="col-5 w-100">Point Promotion</div>
          <div class="col-3 w-100">Price to Point</div>
          <div class="col-3 w-100">End Redeem</div>
          <div class="col-1 w-100"></div>
        </div>
      </div>
      <!-- Menu -->
      <div class="table-item" style="width: 762px; margin-left: -10px;" v-for="item in point_promotions_of_reward" :key="item.id">
        <div class="row" style="font-size: 20px; color: white; line-height: 1">
          <div class="col-5 w-100" style="margin-left: 30px; text-align: left">
            {{ item.point_promotion_set.promotion }}
          </div>
          <div class="col-3 w-100">{{ item.point_promotion_set.price_per_point }}</div>
          <div class="col-3 w-100">{{ format_date(item.point_promotion_set.end_reward_redemption) }}</div>
          <div class="col-1 w-100" style="margin-left: -20px;">
            <img
              src="../../assets/icon/bin.png"
              style="width: 23px; height: 30px; margin: -3px 10px 20px 0px"
              @click="delete_pro_of_reward(item)"
            />
          </div>
        </div>
      </div>
      <!-- Add Item -->
      <div class="table-item" style="width: 762px; margin-left: -10px;">
        <div class="row" style="font-size: 20px; color: white; line-height: 1">
          <div class="col-3 w-100" style="margin-left: 30px; text-align: left; color: #50D1AA;" @click="add_item = true">
            + Add Item
          </div>
        </div>
      </div>
      <!-- Point Promotion -->
      <div class="table-item" style="width: 762px; margin-left: -10px;" v-if="add_item">
        <div class="row" style="font-size: 20px; color: white; line-height: 1">
          <div class="col-3 w-100" style="margin-left: 20px; text-align: left; color: #50D1AA;">
            <select
                name="category"
                id="category"
                v-model="point_promotion_set"
                @change="select_point_promotion()"
                style="height: 30px; width: 259px; background: #717171; margin-top: -3px; color: white;"
              >
                <option value="Point Promotion" selected>
                  Point Promotion
                </option>
                <option
                  v-for="point in point_promotions"
                  :key="point.id"
                  :value="point"
                >
                  {{ point.promotion }}
                </option>
              </select>
          </div>
        </div>
      </div>
    </div>
    <!-- Card Popup -->
    <SavePopup :alert="alert" />
  </div>
</template>

<script>
import SavePopup from "../../components/main_component/SavePopup.vue"
import NavApp from "../../components/main_component/NavApp.vue";
import Switch from "../../components/main_component/Switch.vue";
import { api_promotion } from "../../api/api_promotion";


export default {
  name: "RewardDetail",
  components: {
    SavePopup,
    NavApp,
    Switch,
  },
  mounted() {
  },
  data() {
    return {
      new_img: false,
      alert: false,
      add_item: false,
      img: null,
      show_img: null,
      reward_item: {},
      temp_date: null,
      point_promotion_set: {},
      point_promotion_id: null,
      point_promotions: [],
      point_promotions_of_reward: [],
    };
  },
  mounted () {
    // this.fetchPointPromotion()
    // this.fetchConditionRewards()
    // this.fetchRewards()
  },
  methods: {
    edit() {
     const data = new FormData();
      data.append("id", this.reward_item.id);
      data.append("reward", this.reward_item.reward);
      data.append("value", this.reward_item.value);
      data.append("qty", this.reward_item.qty);
      data.append("point", this.reward_item.point);
      data.append("cost", this.reward_item.cost);
      data.append("description", this.reward_item.description);
      data.append("status", this.reward_item.status);
      data.append("update_by_id", this.$store.state.auth.userInfo.id);
      data.append("create_by_id", this.$store.state.auth.userInfo.id);
      if(this.new_img) {
          data.append("img", this.img, this.img.name);
      }

      api_promotion.put('reward/', data).then((response) => {
        console.log(response.data)
        this.point_promotions_of_reward.forEach(el => {
          const condition_reward = {
            id: el.id,
            point_promotion_id: el.point_promotion_id,
            reward_id: el.reward_id,
            point: el.point,
          }
          api_promotion.put('condition-reward/', condition_reward).then(() => {
            this.alert = true;
            setTimeout(() => {
              this.alert = false;
              this.$router.push({ name: "Promotion" });
            }, 2000);
          })
        });
      })
    },
    fetchRewards() {
      api_promotion.get(`reward/${this.$route.params.id}`).then((response) => {
        console.log(response.data, 'rw')
        this.reward_item = response.data
      })
    },
    fetchConditionRewards() {
        api_promotion.get(`condition-reward/${this.$route.params.id}`).then((response) => {
            console.log(response.data, 'crw')
            this.point_promotions_of_reward = response.data
        })
    },
    fetchPointPromotion() {
      api_promotion.get("point/").then((response) => {
        this.point_promotions = response.data;
      });
    },
    onFileChange(e) {
      console.log(e, "e");
      this.img = e.target.files[0];
      this.new_img = true
      if (this.img) {
        const reader = new FileReader();
        reader.onload = (e) => (this.show_img = e.target.result);
        reader.readAsDataURL(this.img);
      }
      console.log(this.img, "img");
    },
    switch_active(val) {
      this.reward_item.status = val
    },
    select_point_promotion() {
      var pp_id = this.point_promotion_set.id
      if (!this.point_promotions_of_reward.includes(this.point_promotion_set)) {
          const condition_reward = {
            point_promotion_id: pp_id,
            reward_id: this.$route.params.id,
            point: this.point_promotion_set.point,
          }
          api_promotion.post('condition-reward/', condition_reward).then(() => {
              this.point_promotions_of_reward.push(this.point_promotion_set)
          })
      }
      this.add_item = false
    },
    delete_pro_of_reward(item) {
        api_promotion.put(`condition-reward/${item.id}`).then(() => {
            var idx = this.point_promotions_of_reward.indexOf(item)
            this.point_promotions_of_reward.splice(idx, 1);
        })
    },
    format_date(date) {
      var temp_date = date.split("-");
      return `${temp_date[2]}/${temp_date[1]}/${temp_date[0]}`;
    },
  },
  beforeMount() {
    this.fetchRewards()
    this.fetchConditionRewards()
    this.fetchPointPromotion()
  }
};
</script>

<style scoped>
#select_img {
  width: 170px;
  height: 170px;
  border-radius: 20px;
  margin-right: 12px;
  background-color: #c4c4c4;
}
.image {
  width: 170px;
  height: 170px;
  border-radius: 20px;
}
.colon {
  font-size: 30px;
  text-align: center;
  margin: 20px 0px 0px -40px;
  color: white;
}
.input-top {
  width: 448px;
  height: 50px;
  background: rgb(113, 113, 113);
  border-radius: 12px;
  color: white;
  float: left;
  margin: 10px 0px 0px 0px;
}
.input-code {
  width: 167px;
  height: 53px;
  background: #717171;
  border-radius: 10px;
  color: white;
}
#txt-right-side {
  margin-left: -40px;
}
.txt {
  font-size: 30px;
  color: white;
  text-align: left;
}
.card-content {
  width: 765px;
  height: 500px;
  background: #303344;
  border-radius: 20px;
  margin: 15px 0px 0px 27px;
  font-size: 30px;
  font-weight: bold;
}
template {
  color: white;
}
</style>