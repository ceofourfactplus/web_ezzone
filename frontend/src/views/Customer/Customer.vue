<template>
  <div>
    <nav-app>Customer&#160;Management</nav-app>
    <div class="row">
      <div class="col-8 ms-4 pe-2">
        <search-bar @search="search" style="width: 500px" />
      </div>
      <div class="col-4">
        <button
          class="btn-ghost-b ms-2"
          style="width: 170px; height: 45px"
          @click="$router.push({ name: 'CreateCustomer' })"
        >
          +&#160;Customer
        </button>
      </div>
    </div>

    <div class="table mt-3">
      <div class="table-header" style="line-height: 40px; font-size: 24px">
        <div class="row">
          <div class="col-3 w-100" style="margin: auto">Nick&#160;N.</div>
          <div class="col-3 w-100" style="margin-left: 10px; text-align: left">
            Birth&#160;Date
          </div>
          <div class="col-2 w-100" style="margin: auto; margin-left: -10px">
            Phone&#160;No.
          </div>
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
              class="col-3 w-100"
              style="margin: auto; margin-left: 0px; text-align: left"
              @click="SeeData(customer.id)"
            >
              <span>
                <img
                  v-if="customer.img != null"
                  :src="customer.img"
                  class="img-user-status me-1"
                /><img
                  v-else
                  src="../../assets/icon/blank-user.png"
                  class="img-user-status me-1"
                />
                {{ customer.nick_name }}
              </span>
            </div>
            <div class="col-3 w-100" style="margin: auto; text-align: left">
              {{ BirthDate(customer.birth_date) }}
            </div>
            <div
              class="col-3 w-100"
              style="margin: auto; width: 175px; text-align: left"
            >
              {{ PhoneNumber(customer.phone_number) }}
            </div>
            <div
              class="col-3 w-100"
              style="margin: auto; text-align: left; padding: 0px"
            >
              {{ BirthDate(customer.birth_date) }}
              <img
                @click="select(customer)"
                src="../../assets/icon/home.png"
                style="float: right;"
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
              <textarea v-model="select_customer.address" placeholder="Address"></textarea>
            </div>
            <div class="col-12">
              <button class="btn-ghost" @click="save_address()">
                <img src="../../assets/icon/save.png" width="35" class="me-4" />
                Save
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
      const day = new Date(date);
      const result = day.toLocaleDateString("th-TH", {
        year: "numeric",
        month: "short",
        day: "numeric",
      });
      return result;
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
    },
    PhoneNumber(number) {
      var phone = String(number);
      return (
        phone.substr(0, 3) + "-" + phone.substr(3, 3) + "-" + phone.substr(6, 4)
      );
    },
    SeeData(id) {
      this.$router.push({ name: "EditCustomer", params: { id: id } });
    },
    save_address() {
      api_customer.put("save-address/" + this.select_customer.id, {
        address: this.select_customer.address,
      }).then(()=>{
        api_customer.get('customer').then((response)=>{
          this.all_customer = response.data
          this.blur = false
        })
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
  top: 20%;
  left: 23%;
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
  font-size: 24px;
  font-weight: bold;
  line-height: 30px;
  margin: auto;
}

.btn-ghost {
  width: 200px;
  margin-top: 30px;
  height: 50px;
  line-height: 30px;
}
.exit {
  top: 23%;
  right: 180px;
  position: fixed;
}
</style>