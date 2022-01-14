<template>
  <div>
    <div class="table">
      <div class="table-header">
        <div
          class="row"
          style="font-size: 24px; font-weight: bold; color: white"
        >
          <div class="col-5 w-100">Name</div>
          <div class="col-2 w-100">Norm.P.</div>
          <div class="col-2 w-100">Disc.P.</div>
          <div class="col-2 w-100">Status</div>
          <div class="col-1 w-100"></div>
        </div>
      </div>
      <div class="table-item" v-for="item in packages" :key="item.id">
        <div class="row" style="font-size: 20px; color: white; line-height: 1">
          <div class="col-5 w-100" style="margin-left: 10px; text-align: left;">{{ item.promotion }}</div>
          <div class="col-2 w-100">{{ item.normal_price }}</div>
          <div class="col-2 w-100">{{ item.discount_price }}</div>
          <div class="col-2 w-100">
            <label class="switch">
              <input type="checkbox" v-model="item.status" @input="change_status(item, 'package')" />
              <span class="slider round"></span>
            </label>
          </div>
          <div class="col-1 w-100">
            <img
              @click="$router.push({ name: 'PackageDetail', params: { id: item.id }})"
              src="../../assets/icon/edit.png"
              style="width: 23px; height: 30px; margin: -3px 10px 20px 0px"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Switch from "../../components/main_component/Switch.vue";
import { api_promotion } from "../../api/api_promotion";

export default {
  name: "Package",
  props: ["items"],
  components: {
    Switch,
  },
  data() {
    return {
        input: '',
        packages: this.items,
    };
  },
  methods: {
    change_status(item) {
      item.status = !item.status
      const data = {status: item.status}
      api_promotion.put(`package/${item.id}`, data).then(() => {})
    }
  },
  watch: {
    input: function (val) {
      this.input = val;
      console.log(val, "val")
    },
  },
};
</script>

<style scoped>
.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 28px;
  margin-top: -3px;
}

/* Hide default HTML checkbox */
.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

/* The slider */
.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #fff;
  -webkit-transition: 0.4s;
  transition: 0.4s;
}

.slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 1px;
  background-color: #ccc;
  -webkit-transition: 0.4s;
  transition: 0.4s;
}

input:checked + .slider {
  background-color: #c5ffed;
}

input:focus + .slider {
  box-shadow: 0 0 1px #c5ffed;
}

input:checked + .slider:before {
  -webkit-transform: translateX(26px);
  -ms-transform: translateX(26px);
  transform: translateX(26px);
  background-color: #50d1aa;
}
/* Rounded sliders */
.slider.round {
  border-radius: 34px;
}

.slider.round:before {
  border-radius: 50%;
}
</style>