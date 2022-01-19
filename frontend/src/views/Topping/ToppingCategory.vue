<template>
  <div>
    <nav-app :url_name="'DashBoard'" :product_menu="true"
      >Topping Category</nav-app
    >
    <div class="row" style="margin: auto; width: 90%">
      <div class="col-10 w-100" style="padding-left: 0px">
        <SearchBar @search="search_by_typing" />
      </div>
      <div class="col-2 w-100" style="padding-left: 0px">
        <button
          style="margin: 0px;
          white-space: nowrap;"
          class="btn-ghost"
          @click="$router.push({ name: 'CreateCategoryTopping' })"
        >
          + New
        </button>
      </div>
    </div>
    <!-- Table -->
    <div class="table" style="margin-top: 10px">
      <div class="table-header">
        <!-- Is Staff -->
        <div style="margin: auto" class="row">
          <div class="col-1"></div>
          <div class="col-5 w-100" style="margin: auto">Name</div>
          <div class="col-5 w-100" style="margin: auto">Topping&#160;Qty</div>
          <div class="col-1"></div>
        </div>
      </div>
      <div
        style="
          height: 750px;
          overflow-y: scroll;
          overflow-x: hidden;
          border-radius: 10px;
        "
      >
        <div>
          <div
            class="row table-item"
            v-for="(item, idx) in categories"
            :key="idx"
            style="
              padding-right: 0px;
              margin: 10px 0px 0px 0px;
              background-color: #303344;
              border-radius: 10px;
              line-height: 100%;
            "
          >
            <div class="col-1" style="text-align: left; width: 100%">
              <img
                src="../../assets/icon/trash.png"
                @click="delete_category(item.id)"
                style="width: 70%"
                alt=""
              />
            </div>
            <div class="col-5" style="margin: auto; width: 100%">
              {{ item.category }}
            </div>
            <div
              class="col-5 w-100"
              style="margin: auto; font-size: 24px; font-weight: bold"
            >
              {{ item.settopping_set.length }}
            </div>
            <div class="col-1">
              <img
                @click="
                  $router.push({
                    name: 'EditCategoryTopping',
                    params: { id: item.id },
                  })
                "
                src="../../assets/icon/edit.png"
                alt="img"
                style="width: 20px"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SearchBar from "../../components/materials/SearchBar.vue";
import NavApp from "../../components/main_component/NavApp.vue";
import { api_product } from "../../api/api_product";

export default {
  components: {
    SearchBar,
    NavApp,
  },
  mounted() {
    this.is_staff = this.$store.state.auth.userInfo["is_staff"];
    this.fetchToppingCategories();
  },
  data() {
    return {
      alert: false,
      categories: [],
      temp_categories: [],
    };
  },
  methods: {
    fetchToppingCategories() {
      api_product.get("topping/category/").then((response) => {
        this.categories = response.data;
        this.temp_categories = response.data;
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
    delete_category(id) {
      api_product
        .delete("topping/category/" + id)
        .then(() => {
          this.fetchToppingCategories();
        })
        .catch((error) => {
          this.err = error;
        });
    },
    get_topping(category_id) {
      api_product
        .get("category/get-amount-topping/" + category_id)
        .then((response) => {
          console.log(response.data.amount);
          return response.data.amount;
        });
      // return 'html'
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
  line-height: 31px;
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
  line-height: 31px;
  width: 192px;
  height: 45px;
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