<template>
  <div style="top:30%">
    <div class="show-pickup-popup">
      <!-- Nav -->
      <div class="row">
        <div class="col-12 txt-for-add" style="width: 100%">
          Raw Material Detail
        </div>
        <div class="col">
          <img
            @click="$emit('show_status')"
            src="../../assets/icon/Union.png"
            style="
              top: 10px;
              right: 10px;
              position: absolute;
              width: 50px;
              height: 50px;
            "
          />
        </div>
      </div>
      <div class="content-wrapper">
        <div class="row">
          <div class="col-4">
            <!-- Select Image -->
            <div class="row">
              <div class="col-12" style="padding: 0px">
                <label id="select_img" for="file">
                  <img :src="show_img" class="image" v-if="show_img != null"/>
                  <div class="edit-block">Edit</div>
                </label>
                <input
                  type="file"
                  @change="onFileChange"
                  style="display: none; width: "
                  id="file"
                  class="raw-image"
                />
              </div>
            </div>
          </div>
          <div class="col-8 right-wrapper">
            <!-- Name -->
            <div class="row" style="text-align: left">
              <div class="col-12">
                <p style="margin-bottom: 0px">
                  Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: {{item.name}}
                </p>
              </div>
            </div>
            <!-- Category -->
            <div class="row" style="margin-top: 15px; text-align: left">
              <div
                class="col-12"
                style="width: 100%; margin-top: 10px; margin-bottom: 0px"
              >
                <!-- Input Datalist -->
                <label>Category : </label>
                <input
                  list="categories"
                  type="text"
                  :value="category_item.name"
                  class="select-input"
                />
                <datalist id="categories">
                  <option v-for="(cate, idx) in categories" :key="idx">
                    {{ cate.name }}
                  </option>
                </datalist>
              </div>
            </div>
            <!-- Status -->
            <div
              class="row"
              style="margin-top: 15px; text-align: left; margin-bottom: 0px"
            >
              <div class="col-12">
                <p>Status&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: 
                <img style="margin-right: 0px;" :src="$store.state.raw_material.status_image[item.status]" alt="img" />
                </p>
              </div>
            </div>
            <!-- Frigde -->
            <div class="row" style="margin-top: 10px; text-align: left">
              <div class="col-12" style="display: inline-block;">
                Frigde&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:
              <div class="switch"><Switch @switch="fridge" /></div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="mini-content-wrapper">
        <div class="row">
          <!-- First Row -->
          <div class="col-6" style="width: 100%; margin-top: 15px">
            <!-- Input Datalist -->
            <label style="margin-left: 20px"
              >Qty&nbsp;&nbsp;&nbsp;&nbsp;: {{item.remain}}&nbsp;</label
            >
            <input
              list="categories"
              type="text"
              :value="item.unit_set.unit"
              class="select-input"
              style="width: 96px; height: 40px"
            />
            <datalist id="categories">
              <option v-for="(cate, idx) in categories" :key="idx">
                {{ cate.name }}
              </option>
            </datalist>
          </div>
          <!-- Second Row -->
          <div class="col-6" style="width: 100%; margin-top: 15px">
            Min Price : 1,000
          </div>
        </div>

        <div class="row" style="margin-top: 15px">
          <!-- First Row -->
          <div class="col-6" style="width: 100%; margin-left: -25px">
            Price : 1,000
          </div>
          <!-- Second Row -->
          <div class="col-6" style="width: 100%">Max Price : 1,000</div>
        </div>
      </div>
      <!-- Footer Button -->
      <div>
        <button class="btn-edit" @click="edit">
          <span class="icon-edit"></span>Edit
        </button>
      </div>
    </div>
    <!-- Card Popup -->
    <div class="card" :class="{ 'card-active': alert }">
      <div class="icon">
        <img src="../../assets/icon/btn-pass.png" alt="" />
      </div>
      <div class="main-text">Pickup successfully</div>
    </div>
  </div>
</template>


<script>
import Switch from "../../components/main_component/Switch.vue";
export default {
  name: "RMDetailPopup",
  props: ["item", "categories", "category_item"],
  components: {Switch},
  data() {
    return {
      show_status: false,
      alert: false,
      show_img: require(`../../../../backend${this.item.img}`),
      category: this.category_item.name,
    };
  },
  mounted() {
  },
  methods: {
    onFileChange(e) {
      this.show_img = e.target.files[0];
      if (this.show_img) {
        const reader = new FileReader();
        reader.onload = (e) => (this.show_img = e.target.result);
        reader.readAsDataURL(this.show_img);
      }
    },
    edit() {
      this.alert = true;
      setTimeout(() => {
        this.alert = false;
        this.$emit("show_status");
      }, 2000);
    },
  },
};
</script>

<style scoped>
.switch {
    display: inline-block;
    top: 10px;
    left: 10px;
}
.mini-content-wrapper {
  width: 590px;
  height: 134px;
  background: #303344;
  border-radius: 30px;
  margin: 40px 0px 0px 11px;
  font-size: 30px;
  color: white;
}
.card {
  width: 542px;
  height: 319px;
}
.btn-edit {
  width: 192px;
  height: 45px;
  border: 1px solid #ffbf86;
  box-sizing: border-box;
  border-radius: 10px;
  font-size: 24px;
  margin-top: 20px;
  color: #ffbf86;
  background: transparent;
}
span.icon-edit {
  background: url("../../assets/icon/edit_yellow.png") no-repeat transparent;
  background-size: 30px;
  float: left;
  margin-left: 30px;
  width: 30px;
  height: 35px;
}
.pickup-input {
  width: 121px;
  height: 50px;
  background: #717171;
  border-radius: 10px;
}
.right-wrapper {
  text-align: left;
  width: 340px;
  height: 230px;
  font-size: 30px;
  color: white;
  margin: 0px 20px 0px 40px;
}
.content-wrapper {
  width: 575px;
  height: 260px;
  margin: 15px 20px 0px 20px;
  background: #303344;
  border-radius: 30px;
}
.show-pickup-popup {
  width: 616.86px;
  height: 600px;
  top: 30%;
  left: 7%;
  position: absolute;
  background-color: #252836;
  border: 2px solid #ea7c69;
  border-radius: 20px;
}
.image {
  width: 220px;
  height: 220px;
  border-radius: 25px;
}
#select_img {
  width: 220px;
  height: 220px;
  border-radius: 25px;
  margin: 20px 0px 0px 25px;
  background-color: #717171;
}
.txt-for-add {
  font-weight: bold;
  font-size: 48px;
  line-height: 56px;
  text-align: center;
  width: 100%;
  color: white;
}
.edit-block {
  position: absolute;
  width: 74px;
  height: 28.23px;
  left: 45px;
  top: 270px;
  background-color: #c4c4c4;
  border-radius: 5px;
  background-image: url("../../assets/icon/el_camera.png");
  background-position: 10% 50%;
  background-size: contain;
  background-repeat: no-repeat;
  font-size: 18px;
  color: #000000;
  font-weight: bold;
  text-indent: 30px;
  background-size: 25px;
}
.select-input {
  width: 180px;
  height: 35px;
  background-color: #2f414e;
  color: white;
  margin: 0px -10px 0px 5px;
  background-image: url("../../assets/icon/down-arrow.png");
  background-position: center right;
  background-size: 24px;
  background-repeat: no-repeat;
}
</style>