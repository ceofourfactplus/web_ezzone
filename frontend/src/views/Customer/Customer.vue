<template>
  <div>
    <nav-app>Customer Management</nav-app>
    <div class="row">
      <div class="col-8">
        <search-bar @search="search" style="width: 500px" />
      </div>
      <div class="col-4">
        <button class="btn-ghost-b" style="width: 170px; height: 45px" @click="$router.push({name:'CreateCustomer'})">
          +&#160;Customer
        </button>
      </div>
    </div>
    <div class="table mt-3 ms-4">
      <div
        class="table-header"
        style="line-height: 40px; font-size: 24px; right: 10px"
      >
        <div class="row">
          <div class="col-2 w-100" style="margin: auto; margin-left: 20px">
            Nick&#160;N.
          </div>
          <div class="col-3 w-100" style="margin: auto">Birth&#160;Date</div>
          <div class="col-3 w-100" style="margin: auto">Phone&#160;Number</div>
          <div class="col-3 w-100" style="margin: auto">Last&#160;Order</div>
        </div>
      </div>
      <div style="overflow-x: auto; height: 650px">
        <div
          v-for="customer in all_customer"
          :key="customer.id"
          class="table-item"
        >
          <div class="row" style="width: 100%">
            <div
              class="col-3"
              style="margin-left: 15px; width: 100%; display: flex"
            >
              <div>
                <img
                  v-if="customer.img != null"
                  class="img-user-status me-2"
                  :src="customer.img"
                  alt=""
                />
                <img
                  v-else
                  src="../../assets/icon/blank-user.png"
                  class="img-user-status me-2"
                  alt=""
                />
                <span>{{ customer.nick_name }}</span>
              </div>
            </div>

            <div class="col-2" style="margin-left: 10px; width: 100%">
              {{ BirthDate(customer.birth_date) }}
            </div>

            <div
              class="col-3"
              style="margin: auto; margin-left: 60px; width: 100%"
            >
              {{ PhoneNumber(customer.phone_number) }}
            </div>

            <div
              class="col-2"
              style="margin: auto; margin-left: 30px; width: 100%"
            >
              {{ customer.last_order }}
            </div>

            <div class="col-2">
              <img src="../../assets/icon/home.png" alt="" />
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="blur" v-if="blur" @click="blur = false">
      <div class="card-status">
        <div class="row mt-4">
          <div class="col-6 w-100 m-auto">
            <img
              v-if="select_user.img != null"
              class="img-select me-2"
              :src="select_user.img"
              alt=""
            />
            <img
              v-else
              src="../../assets/icon/blank-user.png"
              class="img-select me-2"
              alt=""
            />
          </div>
          <div class="col-6" id="test">
            <p style="color: #fff">{{ select_user.first_name }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { api_user } from "../../api/api_user";
import NavApp from "../../components/main_component/NavApp.vue";
import SearchBar from "../../components/materials/SearchBar.vue";
export default {
  components: { NavApp, SearchBar },
  data() {
    return {
      all_user: [],
      blur: false,
      select_user: {},
    };
  },
  mounted() {
    api_user.get("read-all/").then((response) => {
      this.all_user = response.data;
    });
  },
  methods: {
    role(user) {
      var output = "";

      if (user.is_barista) {
        output = output + "B";
      }
      if (user.is_staff) {
        if (output.length != 0) output = output + "/";
        output = output + "M";
      }
      if (user.is_chef) {
        if (output.length != 0) output = output + "/";
        output = output + "C";
      }
      if (user.is_receptionish) {
        if (output.length != 0) output = output + "/";
        output = output + "R";
      }
      if (user.is_purchesing) {
        if (output.length != 0) output = output + "/";
        output = output + "P";
      }
      if (user.is_owner) {
        if (output.length != 0) output = output + "/";
        output = output + "O";
      }
      if (output.length == 0) output = "-";

      return output;
    },
    status_color(user) {
      if (!user.is_active) {
        return "#fff500";
      }
      if (user.is_working == 1) {
        return "#50D1AA";
      }
      if (user.is_working == 2) {
        return "#65b0f6";
      }
      if (user.is_working == 0) {
        return "#ff7ca3";
      }
    },
    search(val) {
      if (val != "") {
        api_user.get("search-name/" + val).then((response) => {
          this.all_user = response.data;
        });
      } else {
        api_user.get("read-all/").then((response) => {
          this.all_user = response.data;
        });
      }
    },
    SelectUser(user) {
      this.blur = true;
      this.select_user = user;
    },
    change_status(status) {
      api_user
        .put("change-status/" + this.select_user.id + "/" + status)
        .then(() => {
          api_user.get("read-all/").then((response) => {
            this.all_user = response.data;
          });
        });
    },
    ToEditUser(user) {
      this.$router.push({ name: "EditUser", params: { id: user.id } });
    },
  },
};
</script>

<style>
</style>