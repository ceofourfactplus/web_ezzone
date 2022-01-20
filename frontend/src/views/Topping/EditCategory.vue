<template>
  <div>
    <nav-app :save="true" @save="save2" :url_name="'ToppingCategory'"
      >Edit Category</nav-app
    >
    <div class="row" style="width: 90%; margin: auto">
      <div class="col-12" style="display: flex">
        <label for="category" style="display: inline; line-height: 55px">
          <pre>Category Name : </pre>
        </label>
        <input
          type="text"
          style="display: inline; width: 100%"
          v-model="category"
        />
      </div>
      <div class="col-6 w-100">
        <button
          :class="{ 'active-btn': type_topping == 3 }"
          @click="type_topping = 3"
          class="btn-gray me-2"
        >
          FOOD
        </button>
        <button
          :class="{ 'active-btn': type_topping == 2 }"
          @click="type_topping = 2"
          class="btn-gray me-2"
        >
          DRINK
        </button>
        <button
          :class="{ 'active-btn': type_topping == 1 }"
          @click="type_topping = 1"
          class="btn-gray"
        >
          DRESSERT
        </button>
      </div>
      <div class="col-6 w-100 mt-1">
        <search-bar />
      </div>
    </div>
    <!-- Table -->
    <div class="table" style="margin-top: 10px">
      <div class="table-header">
        <div class="row w-100">
          <div class="col-1"></div>
          <div class="col-5 w-100" style="margin: auto">Code</div>
          <div class="col-5 w-100" style="margin: auto">Product</div>
          <div class="col-1"></div>
        </div>
      </div>
      <div
        style="
          height: 660px;
          overflow-y: scroll;
          overflow-x: hidden;
          border-radius: 10px;
          margin: auto;
        "
      >
        <div
          class="row table-item"
          v-for="(item, idx) in topping"
          :key="idx"
          style="
            padding-right: 0px;
            margin: 10px 0px 0px 0px;
            background-color: #303344;
            border-radius: 10px;
            line-height: 100%;
          "
        >
          <div
            class="col-1"
            style="margin: auto; width: 100%; margin-left: 10px"
          >
            <div class="checkbox-orange">
              <input
                type="checkbox"
                :value="item.id"
                v-model="select_topping"
              />
            </div>
          </div>
          <div class="col-5" style="margin: auto">{{ item.code }}</div>
          <div class="col-5" style="margin: auto">
            {{ item.name }}
          </div>
        </div>
      </div>
    </div>
    <SavePopup :alert="alert" />
  </div>
</template>

<script>
import SearchBar from "../../components/materials/SearchBar.vue";
import SavePopup from "../../components/main_component/SavePopup.vue"
import NavApp from "../../components/main_component/NavApp.vue";
import { api_product } from "../../api/api_product";

export default {
  components: {
    SearchBar,
    NavApp,
    SavePopup,
  },
  mounted() {
    api_product
      .get("topping/category/" + this.$route.params.id)
      .then((response) => {
        this.data_topping = response.data;
        console.log(this.data_topping.settopping_set);
        this.category = response.data.category;
        this.change_to_list();
      });
    // this.change_to_list()
    this.fetchTopping();
  },
  data() {
    return {
      data_topping: {},
      category: "",
      alert: false,
      type_topping: 1,
      select_topping: [],
      topping: [],
    };
  },
  methods: {
    fetchTopping() {
      api_product
        .get("topping-by-type/" + this.type_topping)
        .then((response) => {
          this.topping = response.data;
        });
    },
    save2() {
      const data = {
        category: this.category,
        create_by: this.data_topping.create_by,
        update_by: 1,
        settopping_set: [],
      };
      for (var id of this.select_topping) {
        data.settopping_set.push({
          topping: parseInt(id),
          category: this.data_topping.id,
        });
      }
      api_product
        .put("topping/category/" + this.$route.params.id, data)
        .then(() => {
          this.alert = true
          setTimeout(() => {
            this.alert = false
            this.$router.push({ name: "ToppingCategory" });
          }, 2000)
        })
        .catch((error) => {
          this.err = error;
        });
    },
    search_by_typing(val) {
      var temp = [];
      if (val == "") {
        this.categories = this.temp_categories;
      } else {
        this.temp_categories.forEach((element) => {
          if (element.category.toLowerCase().indexOf(val.toLowerCase()) + 1 != 0) {
            temp.push(element);
          }
        });
        this.categories = temp;
      }
    },
    check_category() {
      if (this.category != "") {
        api_product
          .get("check-category-topping/" + this.category)
          .then((response) => {
            this.status = response.data.status;
            console.log(response.data.status);
          });
      }
    },
    change_to_list() {
      this.data_topping.settopping_set.forEach((item) => {
        this.select_topping.push(item.topping);
      });
      console.log(this.select_topping);
    },
  },
  watch: {
    type_topping() {
      this.fetchTopping();
    },
  },
};
</script>

<style scoped>
.card {
  width: 542px;
  height: 350px;
  top: 230px;
  left: 90px;
}
.btn-save {
  font-weight: bold;
  font-size: 24px;
  color: #ea7c69;
  border-color: #ea7c69;
  margin-top: 45px;
  border-radius: 10px;
  text-align: center;
  background: transparent;
  line-height: 100%;
  width: 192px;
  height: 45px;
}
.btn-save-gray {
  font-weight: bold;
  font-size: 24px;
  color: #889898;
  border-color: #889898;
  margin-top: 45px;
  border-radius: 10px;
  text-align: center;
  background: transparent;
  line-height: 100%;
  width: 192px;
  height: 45px;
}
.btn-gray {
  background-color: #303344;
  height: 58px;
  font-size: 24px;
  font-weight: bolder;
  border: 0px;
  border-radius: 10px 10px 0px 0px;
  color: #ffffff80;
}
.active-btn {
  color: #ffffff;
}
span.icon-save {
  background: url("../../assets/icon/save.png") no-repeat transparent;
  background-size: 30px;
  float: left;
  margin-left: 37px;
  width: 30px;
  height: 30px;
}
span.icon-save-gray {
  background: url("../../assets/icon/save-gray.png") no-repeat transparent;
  background-size: 30px;
  float: left;
  margin-left: 37px;
  width: 30px;
  height: 30px;
}
.for-category {
  margin: 40px 0px 0px 0px;
  width: 300px;
  height: 50px;
}
h2 {
  width: 100%;
  height: 39px;
  margin-top: 20px;
  margin: auto;
  top: 10px;
  color: #ea7c69;
}

.category-popup {
  position: absolute;
  top: 240px;
  left: 140px;
  font-weight: bold;
  font-size: 30px;
  width: 450px;
  height: 250px;
  background: #252836;
  border: 2px solid #ea7c69;
  box-sizing: border-box;
  border-radius: 10px;
}
.btn-ghost {
  border-color: #65b0f6;
  color: #65b0f6;
  width: 119px;
  height: 45px;
  margin: 0px 30px 0px 0px;
}
.wrap-search {
  min-width: 520px;
  width: fit-content;
  padding: 0px;
  margin-left: 45px;
}
</style>