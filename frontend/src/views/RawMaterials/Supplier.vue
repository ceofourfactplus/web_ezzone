<template>
  <div>
    <nav-app :url_name="'DashBoard'">Supplier</nav-app>
    <div
      class="row"
      style="
        width: 93%;
        margin: auto;
        align-items: center;
        justify-items: center;
      "
    >
      <div class="col-9 w-100">
        <search-bar @search="search_by_typing" />
      </div>
      <div class="col-3 w-100" style="padding-left: 0px">
        <button
          class="btn-ghost-b"
          style="width: 100%; height: 45px"
          @click="$router.push({ name: 'CreateSupplier' })"
        >
          +&#160;Supplier
        </button>
      </div>
    </div>
    <div class="table mt-3">
      <div class="table-header">
        <div class="row w-100" style="width: 100%; margin-left: 0px">
          <div class="col-4 w-100">&#160;&#160;Name</div>
          <div class="col-3 w-100">Contact</div>
          <div class="col-4 w-100">Phone</div>
          <div class="col-1 w-100"></div>
        </div>
      </div>
      <div style="height: 650px">
        <div
          v-for="supplier in show_supplier"
          :key="supplier.id"
          class="table-item"
        >
          <div
            class="row"
            style="width: 100%; margin-left: 0px 0px; padding: 0px"
          >
            <div class="col-4" style="margin-left: 15px; width: 100%">
              <div style="display: flex">
                <img
                  src="../../assets/icon/home_white.png"
                  class="me-4 mb-1"
                  style="
                    width: 25px;
                    height: 25px;
                    object-fit: cover;
                    margin-top: 6px;
                  "
                  alt=""
                />
                <div
                  style="
                    width: 100%;
                    white-space: nowrap;
                    overflow-x: auto;
                    text-align: left;
                  "
                >
                  {{ supplier.company_name }}
                </div>
              </div>
            </div>
            <div class="col-3 w-100">
              {{ supplier.contact }}
            </div>
            <div class="col-4 w-100" style="margin: auto">
              {{ PhoneNumber(supplier.phone) }}
            </div>
            <div class="col-1 w-100">
              <img
                src="../../assets/icon/edit.png"
                style="width: 25px; height: 25px; object-fit: contain"
                alt=""
                @click="EditSupplier(supplier)"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { api_raw_material } from "../../api/api_raw_material";
import NavApp from "../../components/main_component/NavApp.vue";
import SearchBar from "../../components/materials/SearchBar.vue";
export default {
  components: { NavApp, SearchBar },
  data() {
    return {
      all_supplier: [],
      blur: false,
      select_user: {},
      show_supplier: [],
    };
  },
  mounted() {
    api_raw_material.get("/supplier/").then((response) => {
      this.all_supplier = response.data;
      this.show_supplier = response.data;
    });
  },
  methods: {
    search(val) {
      if (val != "") {
        api_raw_material.get("supplier/search-name/" + val).then((response) => {
          this.all_user = response.data;
        });
      } else {
        api_raw_material.get("/supplier/").then((response) => {
          this.all_user = response.data;
        });
      }
    },
    EditSupplier(user) {
      this.$router.push({ name: "EditSupplier", params: { id: user.id } });
    },
    PhoneNumber(number) {
      if (number != "") {
        var phone = String(number);
        if (phone.length == 10) {
          return (
            phone.substr(0, 3) +
            "-" +
            phone.substr(3, 3) +
            "-" +
            phone.substr(6, 4)
          );
        }
        if (phone.length == 9) {
          return (
            phone.substr(0, 2) +
            "-" +
            phone.substr(2, 3) +
            "-" +
            phone.substr(6, 4)
          );
        }
      }
      return "-";
    },
    search_by_typing(val) {
      var temp = [];
      if (val == "") {
        this.show_supplier = this.all_supplier;
      } else {
        this.all_supplier.forEach((element) => {
          if (
            element.company_name.toLowerCase().indexOf(val.toLowerCase()) + 1 !=
            0
          ) {
            temp.push(element);
          }
        });
        this.show_supplier = temp;
      }
    },
  },
};
</script>

<style>
</style>