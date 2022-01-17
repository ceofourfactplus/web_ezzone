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
              v-model="line_id"
              placeholder="Line ID"
              aria-label=".form-control-lg example"
              style="width: 400px"
            />
          </div>
          <!-- Invite by -->
          <div class="row">
            <input
              type="text"
              v-model="invite_by"
              placeholder="Invite by"
              aria-label=".form-control-lg example"
              style="width: 400px"
              list="browsers"
            />
            <datalist id="browsers">
              <option value="Chrome"></option>
            </datalist>
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
    <div class="card" :class="{ 'card-active': alert }">
      <div class="icon">
        <img src="../../assets/icon/btn-pass.png" alt="" />
      </div>
      <div class="main-text">Saved account</div>
      <div class="second">wait for admin tp activate</div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import NavApp from "../../components/main_component/NavApp.vue";
// import CheckBoxWhite from '../../components/main_component/CheckBoxWhite.vue';
export default {
  components: { NavApp },
  // components: { CheckBoxWhite },
  name: "Register",
  data() {
    return {
      nick_name: "",
      first_name: "",
      last_name: "",
      birth_date: "",
      phone_number: "",
      email: "",
      img: "",
      invite_by: "",
      address: "",
      show_img: null,
      gender: "",
      error: {
        data: "",
        status: false,
      },
      alert: false,
    };
  },
  methods: {
    create_customer() {
      if (
        this.nick_name != "" &&
        this.gender != "" &&
        String(this.phone_number).length == 10 &&
        this.birth_date != ""
      ) {
        const user = new FormData();
        user.append("nick_name", this.nick_name);
        user.append("first_name", this.first_name);
        user.append("last_name", this.last_name);
        user.append("birth_date", this.birth_date);
        user.append("phone_number", this.phone_number);
        user.append("email", this.email);
        user.append("line_customer_id", this.line_id);
        user.append("invite_by", this.invite_by);
        user.append("address", this.address);
        if (this.img != null) {
          user.append("img", this.img, this.img.name);
        }else{
          user.append("img", '');
        }
        user.append("gender", this.gender);
        axios
          .post("http://127.0.0.1:8000/customer/customer", user)
          .then(() => {
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
      } else {
        console.log("2");
        this.error.data = "some thing went wrong";
        this.error.status = true;
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
    phone_number() {
      this.error.status = false;
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
input {
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
