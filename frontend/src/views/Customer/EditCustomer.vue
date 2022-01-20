<template>
  <div>
    <nav-app :url_name="'Customer'" save="true" @save="edit_customer"
      >Customer&#160;Data</nav-app
    >
    <div class="container-fluid">
      <!-- detail  -->
      <div
        class="row"
        style="margin-top: 0px; margin-left: 20px; height: 230px"
      >
        <!-- img -->
        <div class="col-3 w-100" style="margin-right: 20px">
          <div class="row">
            <div class="col-12">
              <label for="file">
                <img
                  v-if="show_img == null"
                  width="160"
                  height="160"
                  src="../../assets/icon/User.png"
                  style="border-radius: 50%"
                />
                <img
                  v-else
                  :src="show_img"
                  width="160"
                  style="border-radius: 50%; object-fit: cover"
                  height="160"
                />
              </label>
              <input
                type="file"
                @change="onFileChange"
                style="display: none"
                id="file"
                class="register-customer"
              />
            </div>
          </div>
          <div class="row" style="margin-top: 20px">
            <div class="col-12">
              <div class="row">
                <div class="checkbox-white">
                  <div class="row">
                    <div class="col-4">
                      <input
                        type="radio"
                        class="me-3 mt-2"
                        v-model="customer.gender"
                        value="Male"
                        id="Male"
                      />
                    </div>
                    <div class="col-8">
                      <label class="ms-3" for="Male">Male</label>
                    </div>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="checkbox-white">
                  <div class="row">
                    <div class="col-4">
                      <input
                        type="radio"
                        class="me-3 mt-2"
                        v-model="customer.gender"
                        value="Female"
                        id="Female"
                      />
                    </div>
                    <div class="col-8">
                      <label class="ms-3" for="Female">Female</label>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- <check-box-white/> -->
        </div>
        <div class="col-9 w-100">
          <div class="row" style="height: 160px">
            <div class="col-4 w-100">
              <h2>
                <span
                  >Point
                  <img
                    class="mb-1"
                    src="../../assets/icon/star.png"
                    style="display: inline"
                    alt="" /></span
                >(Promotion)
              </h2>
              <div class="btn w-100">
                <h2><span>123,456</span></h2>
              </div>
            </div>
            <div class="col-4 w-100">
              <h2>
                <span> Total</span
                ><img
                  class="ms-2 mb-2"
                  style="display: inline"
                  src="../../assets/icon/Bath.png"
                  alt=""
                />
                (Promotion)
              </h2>
              <div class="btn w-100">
                <h2><span>123,456</span></h2>
              </div>
            </div>
            <div class="col-4 w-100">
              <h2>
                <span> Total</span
                ><img
                  class="ms-2 mb-2"
                  style="display: inline"
                  src="../../assets/icon/Bath.png"
                  alt=""
                />
                FOD&#160;12/12/64
              </h2>
              <div class="btn w-100">
                <h2><span>123,456</span></h2>
              </div>
              <h2>LOD&#160;12/12/64</h2>
            </div>
          </div>
          <div class="row">
            <h2><span>Favorite&#160;Menu</span></h2>
            <div class="row">
              <div
                v-for="(menu, index) in favorite_menu"
                :key="menu.id"
                class="col-4"
              >
                <h2 style="color: #fff">
                  {{ index + 1 }}.&#160;{{ Menu(menu) }}
                </h2>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- form -->
      <div class="row" style="margin-top: 40px">
        <div class="col-12">
          <div class="row mb-3">
            <div class="col-3 w-100">
              <label for="first_name">First Name</label>
            </div>
            <div class="col-9 w-100">
              <input
                type="text"
                v-model="customer.first_name"
                id="first_name"
              />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-3 w-100">
              <label for="last_name">Last Name</label>
            </div>
            <div class="col-9 w-100">
              <input type="text" v-model="customer.last_name" id="last_name" />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-3 w-100">
              <label for="nick_name">Nick Name</label>
            </div>
            <div class="col-9 w-100">
              <input
                type="text"
                v-model="customer.nick_name"
                :class="{ error: error.nick_name }"
                id="nick_name"
              />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-3 w-100">
              <label for="birth_date">Birth Date</label>
            </div>
            <div class="col-9 w-100">
              <input
                type="text"
                class="textbox-n"
                onfocus="(this.type='date')"
                v-model="customer.birth_date"
                id="birth_date"
              />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-3 w-100">
              <label for="phone_number">Phone No.</label>
            </div>
            <div class="col-9 w-100">
              <input
                type="text"
                :class="{ error: error.phone_number }"
                v-model="customer.phone_number"
                id="phone_number"
              />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-3 w-100">
              <label for="email" style="margin-left: -25px">Email</label>
            </div>
            <div class="col-9 w-100">
              <input type="email" v-model="customer.email" id="email" />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-3 w-100">
              <label for="address">Address</label>
            </div>
            <div class="col-9 w-100">
              <textarea
                v-if="customer.addresscustomer_set.length != 0"
                v-model="customer.addresscustomer_set[0]['address']"
                id="address"
              ></textarea>
              <textarea
                v-else
                v-model="addresscustomer.address"
                id="address"
              ></textarea>
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-3 w-100">
              <label for="line_id">Line ID</label>
            </div>
            <div class="col-9 w-100">
              <input
                type="text"
                v-model="customer.line_customer_id"
                id="line_id"
              />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-3 w-100">
              <label for="invite_by">Invite By </label>
            </div>
            <div class="col-9 w-100">
              <select v-model="customer['invited_by']">
                <option v-for="user in all_cus" :key="user.id" :value="user.id">
                  {{ user.nick_name }} {{ user.first_name }}
                </option>
                <option value="null">None</option>
              </select>
            </div>
          </div>
        </div>
      </div>
    </div>
    <SavePopup :alert="alert" />
  </div>
</template>

<script>
import { api_customer } from "../../api/api_customer";
import NavApp from "../../components/main_component/NavApp.vue";
import SavePopup from "../../components/main_component/SavePopup.vue";

export default {
  name: "EditUser",
  components: { NavApp, SavePopup },
  data() {
    return {
      customer: {
        addresscustomer_set: [],
      },
      show_img: null,
      favorite_menu: [],
      new_img: false,
      all_cus: [],
      addresscustomer: {
        address: "",
        customer_id: "",
      },
      error: {
        nick_name: false,
        phone_number: false,
      },
    };
  },
  methods: {
    onFileChange(e) {
      this.customer.img = e.target.files[0];
      this.new_img = true;
      if (this.customer.img) {
        const reader = new FileReader();
        reader.onload = (e) => (this.show_img = e.target.result);
        reader.readAsDataURL(this.customer.img);
      }
    },
    edit_customer() {
      for (const item of ["email", "last_name", "first_name"]) {
        if (this.customer[item] == null) {
          this.customer[item] = "";
        }
      }
      var err = false;
      if (this.customer.nick_name == "") {
        err = true;
        this.error.nick_name = true;
      }
      var check_number = [...this.customer.phone_number].some((number) => {
        return isNaN(parseInt(number));
      });
      if (this.customer.phone_number.length != 10 || check_number) {
        err = true;
        this.error.phone_number = true;
      }
      if (!err) {
        api_customer
          .put("customer/" + this.$route.params.id, this.customer)
          .then(() => {
            if (
              this.addresscustomer.address != "" ||
              this.customer.addresscustomer_set.length != 0
            ) {
              if (this.customer.addresscustomer_set.length == 0) {
                api_customer
                  .post("create-address", this.addresscustomer)
                  .then(() => {
                    this.$router.push({ name: "Customer" });

                    this.alert = true;
                    setTimeout(() => {
                      this.alert = false;
                      this.$router.go(-1);
                    }, 2000);
                  });
              } 
              else {
                api_customer
                  .put(
                    "save-address/" + this.customer.addresscustomer_set[0].id,
                    this.customer.addresscustomer_set[0]
                  )
                  .then(() => {
                    this.$router.push({ name: "Customer" });
                  });
              }
            } else {
              this.$router.push({ name: "Customer" });
            }
        });
      }
    },
    Menu(menu) {
      return menu.id;
    },
  },

  beforeCreate() {
    api_customer.get("customer").then((response) => {
      this.all_cus = response.data;
    });
    api_customer
      .get("get-customer/" + this.$route.params.id)
      .then((reponse) => {
        this.customer = reponse.data;
        if (this.customer.img != null) {
          this.show_img = this.customer.img;
        }
      });
  },
  watch: {
    "customer.nick_name"() {
      this.error.nick_name = false;
    },
    "customer.phone_number"() {
      this.error.phone_number = false;
    },
  },
};
</script>

<style scoped>
#alert {
  font-weight: 600;
  height: 45px;
  font-size: 18px;
  width: 630px;
  text-align: center;
  line-height: 40px;
  margin: auto;
}
#text {
  margin-top: 20px;
}
#header {
  margin-left: 25px;
  color: #ea7c69;
  font-weight: 700;
}
.status {
  top: 110px;
  right: 80px;
  position: fixed;
}

.col-3 label {
  font-size: 24px;
  margin: auto;
  font-weight: 700;
  color: #ffb572;
}

textarea,
select,
input[type="email"],
input[type="date"],
input[type="text"],
input[type="number"] {
  text-align: left;
  min-width: 100%;
  height: 45px;
}

h2 span {
  font-size: 30px;
  color: #fff;
  font-weight: 700;
}

h2 {
  font-size: 24px;
  color: #ffffff80;
}

.btn {
  background-color: #bd523f;
}
</style>