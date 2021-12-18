<template>
  <div>
    <!-- Head -->
    <nav-app @back="back">Raw Material</nav-app>
    <div class="row" v-if="is_staff">
      <div style="width: 1%"></div>
      <div class="col-9 wrap-search">
        <SearchBar @search="serch_by_typing" />
      </div>
      <div style="padding-left: 0px">
        <button class="btn-ghost">+ New</button>
      </div>
    </div>
    <SearchBar v-else @search="serch_by_typing" />
    <div>
      <Tabs @select_cate="query_category" />
    </div>
    <!-- Table -->
    <div class="table" style="margin-top: 10px">
      <div class="table-header">
        <!-- Is Staff -->
        <div v-if="is_staff" class="row" style="padding-right: 80px">
          <div class="col-6" style="margin-left: 90px">Items</div>
          <div class="col-2" style="padding-left: 10px">Qty</div>
          <div class="col-2" style="padding-left: 20px">Unit</div>
          <div class="col-2">Status</div>
        </div>
        <!-- Is User -->
        <div v-else class="row" style="padding-right: 10px">
          <div class="col-6" style="margin-left: 90px">Items</div>
          <div class="col-2">Qty</div>
          <div class="col-2">Unit</div>
          <div class="col-2">Status</div>
        </div>
      </div>
      <div
        style="
          height: 660px;
          overflow-y: scroll;
          overflow-x: hidden;
          border-radius: 10px;
        "
      >
        <div v-if="is_staff">
          <div
            class="row table-item"
            v-for="(item, idx) in raw_materials"
            :key="idx"
            style="
              padding-right: 0px;
              background-color: #303344;
              border-radius: 10px;
            "
          >
            <div class="col-6" style="text-align: left">{{ item.item }}</div>
            <div class="col-2">{{ item.qty }}</div>
            <div class="col-2">{{ item.unit }}</div>
            <div class="col-1">
              <img src="../../assets/icon/Group95.png" alt="img" />
            </div>
            <div class="col-1">
              <img
                @click="edit(item)"
                src="../../assets/icon/edit.png"
                alt="img"
              />
            </div>
          </div>
        </div>
        <div v-else>
          <div
            class="row table-item"
            v-for="(item, idx) in raw_materials"
            :key="idx"
            style="
              padding-right: 0px;
              background-color: #303344;
              border-radius: 10px;
            "
          >
            <div class="col-6" style="text-align: left">{{ item.item }}</div>
            <div class="col-2">{{ item.qty }}</div>
            <div class="col-2">{{ item.unit }}</div>
            <div class="col-2" style="margin-left: 30px">
              <img src="../../assets/icon/Group95.png" alt="img" />
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="popup-add-rm" v-if="add_rm">
      <div class="row">
        <div class="col-4">
          <div class="image-for-add"></div>
        </div>
        <div class="col-8">
          <div class="row" style="margin: 20px 0px 20px 22px; width: 296px; height: 57px; padding: 0px;">
            <div class="col-11 txt-for-add">
              Raw Material Detail
            </div>
            <div class="col-1"></div>
          </div>
          <div class="row">
            <div class="col-12">
              <div class="first-form-wrap">
                <input type="text" placeholder="Name" class="input-for-add">
                <div class="row">
                  <div class="col-6 category-select-for-add">Category: </div>
                  <div class="col-6">
                    <input list="categories" style="width: 133px; height: 35px; background-color: #889898; color: white; margin-top: 17px;">
                    <data-list id="categories">
                      <option v-for="cate in categories" :key="cate" :value="cate"></option>
                    </data-list>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script> 
// import RawMaterial from '../../components/materials/RawMaterial.vue'
// import api_raw_material from "../../api/api_raw_material";
import Tabs from "../../components/materials/Tabs.vue";
import SearchBar from "../../components/materials/SearchBar.vue";
import NavApp from "../../components/main_component/NavApp.vue";

export default {
  components: {
    // RawMaterial,
    Tabs,
    SearchBar,
    NavApp,
  },
  mounted() {
    this.is_staff = this.$store.state.auth.userInfo["is_staff"];
  },
  data() {
    return {
      category: "",
      is_staff: false,
      add_rm: true,
      texts: "",
      materials: [],
       categories: [
        "All",
        "Fresh Food",
        "Dried Food",
        "Garnish",
        "Package",
        "ETC.",
      ],
      img: require('../../assets/icon/frame.png'),
      raw_materials: [
        {
          item: "นมข้นหวาน",
          qty: 2,
          unit: "pack",
          status: "../../assets/icon/Group95.png",
        },
        {
          item: "นมข้นจืด",
          qty: 2,
          unit: "pack",
          status: "../../assets/icon/Group95.png",
        },
        {
          item: "โซดา",
          qty: 20,
          unit: "bag",
          status: "../../assets/icon/Group95.png",
        },
        {
          item: "สไปรท์",
          qty: 10,
          unit: "bag",
          status: "../../assets/icon/Group95.png",
        },
      ],
    };
  },
  methods: {
    edit(item) {
      console.log(item, "item");
    },
    query_category(cate) {
      console.log(cate);
      // api_raw_material.get(`query_category/${cate}`).then((response) => {
      //   this.materials = response.data;
      // });
    },
    select_category(cate) {
      this.category = cate;
      console.log(this.category);
    },
    serch_by_typing(val) {
      this.texts = val;
      console.log(val, "views");
      // api_raw_material.get(`serch_by_typing/${val}`).then((response) => {
      //   this.materials = response.data
      //   console.log(response.data);
      // });
    },
  },
};
</script>

<style scoped>
.category-select-for-add {
  font-size: 30px; 
  line-height: 56px; 
  color: white; 
  margin: 4px 0px 0px 30px; 
  /* width: 317px;  */
  height: 57px; 
  text-align: left;
}
.input-for-add {
  background-color: #C4C4C4; 
  color: black; 
  width: 317px; 
  height: 46px; 
  margin: 24px 0px 0px 0px;
}
.first-form-wrap {
  position: absolute;
  width: 60%;
  height: 220px;
  border-radius: 20px;
  margin: 0px 0px 0px 25px;
  background-color: #252836;
}
.txt-for-add {
  font-weight: bold;
  font-size: 28px;
  line-height: 56px;
  width: 100%;
  color: white;
}
.image-for-add {
  position: absolute;
  width: 167px;
  height: 196px;
  margin: 42px 0px 0px 34px;
  border-radius: 20px;
  background-image: url('../../assets/icon/frame.png');
  background-repeat: no-repeat;
  background-size: contain;
}
::placeholder {
  color: #889898;
}
.popup-add-rm {
  width: 625px;
  height: 756px;
  top: 7%;
  left: 7%;
  position: absolute;
  background-color: aqua;
}
.row {
  padding-right: 50px;
}
.btn-ghost {
  border-color: #65b0f6;
  color: #65b0f6;
  width: 242px;
  height: 45px;
  margin-left: 0px;
}

.wrap-search {
  min-width: 424px;
  width: fit-content;
  padding: 0px;
  margin-left: 0px;
}

.search-bar {
  background-size: contain;
  background-repeat: no-repeat;
  background-color: #3a3d49;
  text-indent: 65px;
  padding-left: 10px;
  margin-left: 3px;
  border-radius: 20px;
  width: 90%;
  height: 45px;
  background-image: url("../../assets/icon/Search-19x18-1.png");
  background-repeat: no-repeat;
  background-position: 2% 50%;
  /* Extra Styling */
}
</style>