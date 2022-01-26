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
                <h2>
                  <span>{{ format_locale_string(point) }}</span>
                </h2>
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
                <h2>
                  <span>{{ format_locale_string(total_promotion) }}</span>
                </h2>
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
                FOD&#160;{{ getDate(customer.date_joined) }}
              </h2>
              <div class="btn w-100">
                <h2>
                  <span>{{ format_locale_string(total_price) }}</span>
                </h2>
              </div>
              <h2>LOD&#160;{{ getDate(customer.last_joined) }}</h2>
            </div>
          </div>
          <div class="row">
            <h2><span>Favorite&#160;Menu</span></h2>
          </div>
          <div class="row">
            <div class="col-4 w-100" style="text-align: left;color: white; font-size: 20px; font-weight: 600;" v-for="(menu, idx) in favorite_menu" :key="menu.id">
              {{ idx+1 }}.&nbsp;{{ menu.name }}
            </div>
          </div>
        </div>
      </div>

      <!-- form -->
      <div class="row" style="margin-top: 40px">
        <div class="col-12">
          <div class="row mb-3">
            <div class="col-3 w-100">
              <label for="first_name" class="i">First Name</label>
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
              <label for="last_name" class="i">Last Name</label>
            </div>
            <div class="col-9 w-100">
              <input type="text" v-model="customer.last_name" id="last_name" />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-3 w-100">
              <label for="nick_name" class="i">Nick Name</label>
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
              <label for="birth_date" class="i">Birth Date</label>
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
              <label for="phone_number" class="i">Phone No.</label>
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
              <label for="email" class="i">Email</label>
            </div>
            <div class="col-9 w-100">
              <input type="email" v-model="customer.email" id="email" />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-3 w-100">
              <label for="address" class="i">Address</label>
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
              <label for="line_id" class="i">Line ID</label>
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
              <label for="invite_by" class="i">Invite By </label>
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
      total_price: 0,
      total_promotion: 0,
      point: 0,
      show_img: null,
      favorite_menu: [],
      new_img: false,
      all_cus: [],
      addresscustomer: {
        address: "",
        customer_id: "",
      },
      error: {
        nick_name: true,
        phone_number: true,
      },
      check_number: false,
    };
  },
  methods: {
    format_locale_string(num) {
      return (parseInt(num)).toLocaleString()
    },
    getDate(date) {
      console.log(date);
      var temp_date = date.slice(0, 10).split('-')
      return `${temp_date[2]}/${temp_date[1]}/${temp_date[0]}`
    },
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
      if (!this.error.phone_number && !this.error.nick_name) {
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
              } else {
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
  },
  beforeMount() {
    api_customer
      .get("get-customer/" + this.$route.params.id)
      .then((response) => {
        console.log(response.data, 'data')
        this.customer = response.data.customer;
        this.favorite_menu = response.data.top_products
        if (this.customer.img != null) {
          this.show_img = this.customer.img;
        }
        this.total_price = response.data.total_price;
        this.point = response.data.point;
        this.total_promotion = response.data.total_promotion;
        this.addresscustomer.customer_id = response.data.customer.id;
      });
    api_customer.get("customer").then((response) => {
      this.all_cus = response.data;
    });
  },
  mounted() {},
  watch: {
    "customer.phone_number"(number) {
      this.error.status = false;
      var phone = ![...number].some((numbers) => {
        return isNaN(parseInt(numbers));
      });
      if ((number.length == 9 || number.length == 10) && phone) {
        api_customer
          .get("check-phone-number/" + number + "/" + this.$route.params.id)
          .then((result) => {
            console.log(result);
            this.error.phone_number = false;
          })
          .catch((err) => {
            console.log(err);
            this.error.phone_number = true;
          });
      } else {
        this.error.phone_number = true;
      }
    },
    "customer.nick_name"(nick) {
      this.error.nick_name = false;
      this.error.status = false;
      if (nick == "") {
        this.error.nick_name = true;
      }
    },
  },
};
</script>

<style scoped>
.i {
  width: 100%;
  padding-left: 30px;
  text-align: left;
}
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