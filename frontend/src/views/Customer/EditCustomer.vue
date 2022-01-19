<template>
  <div>
    <nav-app :url_name="'Customer'" save=true @save="edit_customer">Customer&#160;Data</nav-app>
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
                  style="border-radius: 50%;"
                />
                <img
                  v-else
                  :src="show_img"
                  width="160"
                  style="border-radius: 50%;object-fit: cover;"
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
              <input type="text" v-model="customer.nick_name" id="nick_name" />
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
                type="number"
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
            <div class="col-9 w-100" style="margin-left:12px">
              <div class="row">
                <textarea
                  v-model="customer.address"
                  id="address"
                  style="width: 516px; height: 80px"
                ></textarea>
              </div>
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-3 w-100">
              <label for="line_id">Line ID</label>
            </div>
            <div class="col-9 w-100">
              <input type="text" v-model="customer.line_customer_id" id="line_id" />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-3 w-100">
              <label for="invite_by">Invite By
              </label>
            </div>
            <div class="col-9 w-100">
              <input type="number" v-model="customer.invite_by" id="invite_by" />
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
import SavePopup from "../../components/main_component/SavePopup.vue"

export default {
  name: "EditUser",
  components: { NavApp, SavePopup },
  data() {
    return {
      customer: {},
      alert: false,
      show_img: null,
      favorite_menu: [],
      new_img: false,
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
      const customer_data = new FormData();
      customer_data.append("email", this.customer.email);
      customer_data.append("first_name", this.customer.first_name);
      customer_data.append("last_name", this.customer.last_name);
      customer_data.append("nick_name", this.customer.nick_name);
      customer_data.append("line_customer_id", this.customer.line_id);
      customer_data.append("phone_number", this.customer.phone_number);
      customer_data.append("address", this.customer.address);
      customer_data.append("birth_date", this.customer.birth_date);
      customer_data.append("invite", this.customer.invite);
      if (this.new_img) {
        customer_data.append("img", this.customer.img, this.customer.img.name);
      }
      customer_data.append("gender", this.customer.gender);
      api_customer
        .put("customer/" + this.$route.params.id, customer_data)
        .then(() => {
          this.alert = true
          setTimeout(() => {
            this.alert = false
            this.$router.go(-1);
          }, 2000)
        });
    },
    Menu(menu) {
      return menu.id;
    },
    update(){

    }
  },

  mounted() {
    api_customer
      .get("customer/" + this.$route.params.id)
      .then((reponse) => {
        this.customer = reponse.data;
        if (this.customer.img != null) {
          this.show_img = this.customer.img;
        }
      });
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
input[type="email"],
input[type="date"],
input[type="text"],
input[type="number"] {
  width: 100%;
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