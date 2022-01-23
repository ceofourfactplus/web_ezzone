<template>
  <div>
    <nav-app :url_name="'DashBoard'">Customer</nav-app>
    <div class="row" style="margin: auto; width: 91%">
      <div class="col-9 w-100" style="padding: 0px">
        <search-bar @search="search" />
      </div>
      <div class="col-3 w-100 pe-0">
        <button
          class="btn-ghost-b"
          style="width: 100%; height: 45px"
          @click="$router.push({ name: 'CreateCustomer' })"
        >
          +&#160;Customer
        </button>
      </div>
    </div>

    <div class="table mt-3">
      <div class="table-header" style="line-height: 100%; font-size: 24px">
        <div class="row" style="width: 99%; margin: auto">
          <div class="col-3 w-100">Nick&#160;N.</div>
          <div class="col-3 w-100" style="margin-left: 10px; text-align: left">
            Birth&#160;Date
          </div>
          <div class="col-3 w-100" style="margin-left: -10px">
            Phone&#160;No.
          </div>
          <div class="col-3 w-100" style="text-align: left">
            Last&#160;Order
          </div>
        </div>
      </div>
      <div style="overflow-x: auto; height: 750px">
        <div
          v-for="customer in all_customer"
          :key="customer.id"
          class="table-item"
        >
          <div class="row" style="width: 100%; padding: 0px">
            <div
              class="col-3 w-100 ps-4"
              style="
                margin: auto;
                margin-left: 0px;
                text-align: left;
                line-height: 30px;
              "
              @click="SeeData(customer.id)"
            >
              <div style="display: flex">
                <img
                  v-if="customer.img != null"
                  :src="customer.img"
                  class="img-user-status me-1"
                /><img
                  v-else
                  src="../../assets/icon/blank-user.png"
                  class="img-user-status me-1"
                />
                <div style="width: 100%; text-align: left; overflow-x: auto">
                  {{ customer.nick_name }}
                </div>
              </div>
            </div>
            <div class="col-3 w-100" style="margin: auto; text-align: center">
              {{ BirthDate(customer.birth_date) }}
            </div>
            <div
              class="col-3 w-100"
              style="margin: auto; width: 175px; text-align: center"
            >
              {{ PhoneNumber(customer.phone_number) }}
            </div>
            <div class="col-3 w-100" style="padding: 0px">
              {{ BirthDate(customer.birth_date) }}
              <img
                @click="select(customer)"
                src="../../assets/icon/home.png"
                style="
                  float: right;
                  padding-top: 6px;
                  height: 28px;
                  margin-top: 2px;
                "
              />
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="blur" v-if="blur">
      <div class="card-address">
        <img
          src="../../assets/icon/delete.png"
          class="exit"
          alt=""
          @click="blur = false"
        />
        <div class="row mt-4">
          <div class="col-6 w-100 m-auto">
            <img
              v-if="select_customer.img != null"
              class="img-select me-2"
              style="vertical-align: text-top"
              :src="select_customer.img"
              alt=""
            />
            <img
              v-else
              src="../../assets/icon/user_white.png"
              class="img-select me-2"
              alt=""
            />
          </div>
          <div class="col-6" id="test">
            <p style="color: #fff">{{ select_customer.nick_name }}</p>
          </div>
        </div>
        <div class="container">
          <div class="row mt-4 m-1">
            <div class="col-12 input-label" style="text-align: left">
              <img src="../../assets/icon/home.png" /> Address
            </div>
            <div class="col-12">
              <textarea
                v-if="select_customer.addresscustomer_set != []"
                v-model="select_customer.addresscustomer_set[0].address"
                placeholder="Address"
              ></textarea>
              <textarea
                v-else
                v-model="address"
                placeholder="Address"
              ></textarea>
            </div>
            <div class="col-12">
              <button
                v-if="select_customer.addresscustomer_set.legnth != 0"
                class="btn-ghost"
                @click="save_address()"
              >
                <img src="../../assets/icon/save.png" width="35" class="me-4" />
                Save
              </button>
              <button v-else class="btn-ghost" @click="create_address()">
                <img src="../../assets/icon/save.png" width="35" class="me-4" />
                Create
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { api_customer } from "../../api/api_customer";
import NavApp from "../../components/main_component/NavApp.vue";
import SearchBar from "../../components/materials/SearchBar.vue";
export default {
  components: { NavApp, SearchBar },
  data() {
    return {
      all_customer: [],
      blur: false,
      select_customer: {},
      address: "",
    };
  },
  mounted() {
    api_customer.get("customer").then((response) => {
      this.all_customer = response.data;
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
    BirthDate(date) {
      if (date != null) {
        const day = new Date(date);
        const result = day.toLocaleDateString("th-TH", {
          year: "numeric",
          month: "short",
          day: "numeric",
        });
        return result;
      }
      return "-";
    },
    search(val) {
      if (val != "") {
        api_customer.get("search-name/" + val).then((response) => {
          this.all_customer = response.data;
        });
      } else {
        api_customer.get("customer").then((response) => {
          this.all_customer = response.data;
        });
      }
    },
    select(customer) {
      this.blur = true;
      this.select_customer = customer;
      this.address = "";
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
    SeeData(id) {
      this.$router.push({ name: "EditCustomer", params: { id: id } });
    },
    save_address() {
      api_customer
        .put("save-address/" + this.select_customer.id, {
          address: this.select_customer.addresscustomer_set[0].address,
        })
        .then(() => {
          api_customer.get("customer").then((response) => {
            this.all_customer = response.data;
            this.blur = false;
          });
        });
    },
    create_address() {
      api_customer
        .post("create-address/" + this.select_customer.id, {
          address: this.select_customer.addresscustomer_set[0].address,
        })
        .then(() => {
          api_customer.get("customer").then((response) => {
            this.all_customer = response.data;
            this.blur = false;
          });
        });
    },
  },
};
</script>

<style scoped>
.table-item {
  font-size: 20px;
}

textarea {
  height: 200px;
  width: 100%;
  background-color: #303344;
  padding: 12px 20px;
  box-sizing: border-box;
  border-radius: 10px;
  resize: none;
  text-indent: 0px;
}
.card-address {
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  justify-self: center;
  align-self: center;
  width: 400px;
  height: 500px;
  position: fixed;
  background: #252836;
  border: 2px solid #ea7c69;
  box-sizing: border-box;
  border-radius: 25px;
}
.input-label {
  color: #fff;
  margin-bottom: 10px;
  font-size: 24px;
  font-weight: bold;
  line-height: 30px;
}

.btn-ghost {
  width: 200px;
  margin-top: 30px;
  height: 50px;
  line-height: 30px;
}
.exit {
  top: 3%;
  right: 4%;
  position: absolute;
  width: 30px;
}
</style>