<template>
  <div>
    <nav-app save="true">Product&#160;Detail</nav-app>
    <div class="container-f">
      <div class="frame f-1">
        <div class="row h-100">
          <div class="col-5 w-100">
            <div class="row" style="margin-top: 10px">
              <label for="code">Code&#160;:</label>
              <input type="text" v-model="code" style="margin-left: 0px" />
            </div>
            <div class="row">
              <div class="col-12" style="padding: 0px">
                <label id="select_img" for="file" style="margin-top: 30px">
                  <img :src="show_img" class="image" v-if="show_img != null" />
                  <div class="edit-block">Edit</div>
                </label>
                <input
                  type="file"
                  @change="onFileChange"
                  style="display: none"
                  id="file"
                  class="raw-image"
                />
              </div>
            </div>
          </div>
          <div class="col-7 w-100">
            <div class="col-12 h-20">
              <input
                type="text"
                style="width: 300px; margin: auto; margin-top: 10px"
              />
            </div>
            <div class="col-12 h-20">
              <label for="">Category :</label><input type="text" />
            </div>
            <div class="col-12 h-20">
              <label for="">Status :</label><input type="text" />
            </div>
            <div class="col-12 h-20">
              <label for="">Active :</label><input type="text" />
            </div>
            <div class="col-12 h-20">
              <label for="">Active :</label><input type="text" />
            </div>
          </div>
        </div>
      </div>
      <div class="frame f-2">
        <div class="row">
          <div class="col-6">
            <div class="row">
              <label for="">Qty</label><input type="text" />
            </div>
            <div class="row">
              <label for="">Qty</label><input type="text" />
            </div>
          </div>
          <div class="col-6">
            <div class="row">
              <label for="">Qty</label><input type="text" />
            </div>
            <div class="row">
              <label for="">Qty</label><input type="text" />
            </div>
          </div>
        </div>
      </div>
      <div class="frame f-2">
        <div class="row">
          <div class="col-6">
            <div class="row">
              <label for="">Qty</label><input type="text" />
            </div>
            <div class="row">
              <label for="">Qty</label><input type="text" />
            </div>
          </div>
          <div class="col-6">
            <div class="row">
              <label for="">Qty</label><input type="text" />
            </div>
            <div class="row">
              <label for="">Qty</label><input type="text" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavApp from "../../components/main_component/NavApp.vue";

export default {
  components: { NavApp },
  mounted() {
    this.fetchRawMaterials();
  },
  data() {
    return {
      show_img: null,
    };
  },
  methods: {
    fetchRawMaterials() {
      console.log("fetch raw materials");
    },
    onFileChange(e) {
      this.show_img = e.target.files[0];
      if (this.show_img) {
        const reader = new FileReader();
        reader.onload = (e) => (this.show_img = e.target.result);
        reader.readAsDataURL(this.show_img);
      }
    },
  },
};
</script>

<style scoped>
.frame {
  margin-top: 15px;
  margin-bottom: 20px;
  background-color: #303344;
  border-radius: 20px;
  padding-top: 20px;
  padding-bottom: 20px;
  padding-left: 20px;
}
.f-1 {
  width: 680px;
  height: 398px;
}
.f-2 {
  width: 680px;
  height: 199px;
}
.container-f {
  padding-left: 22px;
  margin-right: auto;
  margin-left: auto;
}
input {
  background-color: #717171;
  width: 150px;
  height: 50px;
  margin-left: 10px;
}
raw-img {
  width: 236px;
  height: 235px;
}

label {
  color: #fff;
  font-size: 30px;
}

::placeholder {
  text-indent: 5px;
}
.h-20 {
  height: 20%;
  text-align: left;
}

.h-100 {
  height: 100%;
}

.edit-block {
  position: absolute;
  width: 74px;
  height: 28.23px;
  top: 415px;
  left: 80px;
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
#select_img {
  width: 236px;
  height: 235px;
  border-radius: 25px;
  margin-right: 12px;
  background-color: #717171;
}
.image {
  width: 236px;
  height: 235px;
  border-radius: 25px;
}
</style>