<template>
  <div style="top: 0px">
    <!-- back to login path -->
    <nav-app :url_name="'Customer'"
      >Customer Registration
      <img
        src="../../assets/icon/save.png"
        @click="create_customer()"
        class="save"
        alt=""
    /></nav-app>
    <!-- input img -->

    <!-- form -->
    <div class="container">
      <div class="row">
        <div class="col-3">
          <!-- select img -->
          <div style="height: 0px">
            <label for="file">
              <img
                v-if="show_img == null"
                width="170"
                height="170"
                src="../../assets/icon/User.png"
                class="register-user"
              />
              <img
                v-else
                :src="show_img"
                width="170"
                height="170"
                class="register-user"
              />
            </label>
            <input
              type="file"
              @change="onFileChange"
              style="display: none"
              id="file"
              class="register-user"
            />
            <!-- <check-box-white/> -->
          </div>

          <!-- gender -->
          <div class="gender" style="width: 200px">
            <div
              class="row ms-4 mb-2"
              style="color: #fff; font-size: 24px; font-weight: bold"
            >
              Gender
            </div>
            <div class="row">
              <div class="checkbox-white">
                <div class="row">
                  <div class="col-4">
                    <input
                      type="radio"
                      class="me-3 mt-2"
                      v-model="gender"
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
                      v-model="gender"
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
        <div class="col-9 mt-4 ms-4">
          <!-- nick name -->
          <div class="row">
            <input
              type="text"
              v-model="nick_name"
              placeholder="Nick Name"
              :class="{ error: error.nick_name }"
              aria-label=".form-control-lg example"
              style="width: 400px"
            />
          </div>
          <!-- first name -->
          <div class="row">
            <input
              type="text"
              v-model="first_name"
              placeholder="First Name"
              aria-label=".form-control-lg example"
              style="width: 400px"
            />
          </div>
          <!-- last name -->
          <div class="row">
            <input
              type="text"
              v-model="last_name"
              placeholder="Last Name"
              aria-label=".form-control-lg example"
              style="width: 400px"
            />
          </div>
          <!-- birth date -->
          <div class="row">
            <input
              type="text"
              v-model="birth_date"
              placeholder="Birth Date"
              onfocus="(this.type='date')"
              aria-label=".form-control-lg example"
              style="width: 400px"
            />
          </div>
          <!-- phone number -->
          <div class="row">
            <input
              type="text"
              v-model="phone_number"
              :class="{ error: error.phone_number }"
              placeholder="Phone Number"
              aria-label=".form-control-lg example"
              style="width: 400px"
            />
          </div>
          <!-- email -->
          <div class="row">
            <input
              type="email"
              v-model="email"
              placeholder="Email"
              aria-label=".form-control-lg example"
              style="width: 400px"
            />
          </div>
          <!-- Line ID -->
          <div class="row">
            <input
              type="text"
              v-model="line_customer_id"
              placeholder="Line ID"
              aria-label=".form-control-lg example"
              style="width: 400px"
            />
          </div>
          <!-- Invite by -->
          <div class="row">
            <select v-model="invited_by" style="width: 400px">
              <option v-for="user in all_cus" :key="user.id" :value="user.id">
                {{ user.nick_name }} {{ user.first_name }}
              </option>
              <option value="null">Invite by</option>
            </select>
          </div>

          <!-- address -->
          <div class="row">
            <textarea
              v-model="address"
              placeholder="Address"
              style="width: 400px; height: 130px"
            ></textarea>
          </div>
          <div class="row">
            <div class="m-1" v-if="error.status">
              <div class="text-error" style="text-align: center; width: 400px">
                <img src="../../assets/icon/btn-warning.png" alt="" />
                {{ error.data }}
              </div>
            </div>
            <div class="m-1" v-else></div>
          </div>
        </div>
      </div>
    </div>

    <!-- card pop up -->
    <SavePopup :alert="alert" />
  </div>
</template>

<script>
import { api_customer } from "../../api/api_customer";
import NavApp from "../../components/main_component/NavApp.vue";
import SavePopup from "../../components/main_component/SavePopup.vue";
// import CheckBoxWhite from '../../components/main_component/CheckBoxWhite.vue';
export default {
  components: { NavApp, SavePopup },
  // components: { CheckBoxWhite },
  mounted() {
    api_customer.get("customer").then((response) => {
      this.all_cus = response.data;
    });
  },
  name: "Register",
  data() {
    return {
      nick_name: "",
      first_name: "",
      last_name: "",
      birth_date: null,
      phone_number: "",
      email: "",
      img: null,
      invited_by: null,
      line_customer_id: "",
      address: "",
      gender: "",
      error: {
        data: "",
        status: false,
        nick_name: true,
        phone_number: true,
      },
      show_img: null,
      alert: false,
      all_cus: [],
    };
  },
  methods: {
    create_customer() {
      if (!this.error.phone_number && !this.error.nick_name) {
        const data = {
          nick_name: this.nick_name,
          first_name: this.first_name,
          last_name: this.last_name,
          phone_number: this.phone_number,
          gender: this.gender,
          email: this.email,
          birth_date: this.birth_date,
          line_customer_id: this.line_customer_id,
          invited_by: this.invited_by,
          addresscustomer_set: {
            address: this.address,
          },
        };
        api_customer
          .post("customer", data)
          .then((response) => {
            if (this.img != null) {
              const img = new FormData();
              img.append("img", this.img, this.img.name);
              api_customer.put("customer-img/" + response.data.id, img);
            }
            this.alert = true;
            setTimeout(() => {
              this.alert = false;
              this.$router.push({ name: "Customer" });
            }, 1500);
          })

          .catch((err) => {
            this.error.data = err.response.data;
            this.error.status = true;
          });
      }
    },
    onFileChange(e) {
      this.img = e.target.files[0];
      if (this.img) {
        const reader = new FileReader();
        reader.onload = (e) => (this.show_img = e.target.result);
        reader.readAsDataURL(this.img);
      }
    },
    wait(ms) {
      var start = new Date().getTime();
      var end = start;
      while (end < start + ms) {
        end = new Date().getTime();
      }
    },
  },
  watch: {
    nick_name(nick) {
      this.error.nick_name = false;
      this.error.status = false;
      if (nick == "") {
        this.error.nick_name = true;
      }
    },
    first_name() {
      this.error.status = false;
    },
    last_name() {
      this.error.status = false;
    },
    id_card() {
      this.error.status = false;
    },
    birth_date() {
      this.error.status = false;
    },
    phone_number(number) {
      this.error.status = false;
      var phone = ![...number].some((numbers) => {
        return isNaN(parseInt(numbers));
      });
      if ((number.length == 9 || number.length == 10) && phone) {
        api_customer
          .get("check-phone-number/" + number)
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
    email() {
      this.error.status = false;
    },
    username() {
      this.error.status = false;
    },
    password() {
      this.error.status = false;
    },
    confirm_password() {
      this.error.status = false;
    },
    img() {
      this.error.status = false;
    },
  },
};
</script>

<style scoped>
input,
select {
  margin-bottom: 15px;
  height: 60px;
}
.gender {
  position: fixed;
  top: 315px;
  left: 50px;
  color: #ffffff80;
}
.checkbox {
  left: 50px;
}

.save {
  position: fixed;
  top: 20px;
  right: 30px;
}
</style>
