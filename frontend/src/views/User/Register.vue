<template>
  <div class="" style="top: 0px">
    <!-- back to login path -->
    <nav-app  :url_name="'Login'">Registration</nav-app>
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
            <div class="row ms-4 mb-2" style="color: #fff; font-size:24px; font-weight:bold;">Gender</div>
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
          <!-- id card -->
          <div class="row">
            <input
              type="number"
              v-model="id_card"
              placeholder="ID Card"
              aria-label=".form-control-lg example"
              style="width: 400px"
            />
          </div>
          <!-- birth date -->
          <div class="row" style="text-align:left">
            <input
              type="text"
              v-model="birth_date"
              placeholder="Birth Date"
              onfocus="(this.type='date')"
              aria-label=".form-control-lg example"
              style="width: 400px;text-align:left;padding-left:2%;"
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
          <!-- Username -->
          <div class="row">
            <input
              type="text"
              v-model="username"
              placeholder="Username"
              aria-label=".form-control-lg example"
              style="width: 400px"
            />
          </div>
          <!-- password -->
          <div class="row">
            <input
              type="password"
              v-model="password"
              placeholder="Password"
              aria-label=".form-control-lg example"
              style="width: 400px"
            />
          </div>
          <!-- conf password -->
          <div class="row">
            <input
              type="password"
              v-model="confirm_password"
              placeholder="Confirm Password"
              aria-label=".form-control-lg example"
              style="width: 400px"
            />
          </div>
          <div class="row">
            <div class="col-1"></div>
            <div class="col-11 ms-3">
              <div class="m-1" v-if="error.status">
                <div
                  class="text-error"
                  style="text-align: center; width: 400px"
                >
                  <img src="../../assets/icon/btn-warning.png" alt="" />
                  {{ error.data }}
                </div>
              </div>
              <div class="m-1" v-else></div>
            </div>
          </div>

          <!-- btn restgister -->
          <div class="row">
              <button
                class="btn-ghost"
                @click="register"
                style="width: 400px; height: 70px"
              >
                Register
              </button>
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
      nick_name:"",
      first_name: "",
      last_name: "",
      id_card: "",
      birth_date: "",
      phone_number: "",
      email: "",
      username: "",
      password: "",
      confirm_password: "",
      img: "",
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
    register() {
      console.log(this.id_card.toString().length);
      console.log(this.nick_name != "");
      console.log(this.first_name != "");
      console.log(this.last_name != "");
      console.log(this.birth_date != "");
      console.log(this.username.length > 6);
      console.log(this.password.length > 6);
      console.log(this.img != "");
      console.log(this.gender != "");
      if (
        this.id_card.toString().length == 13 &&
        this.first_name != "" &&
        this.last_name != "" &&
        this.birth_date != "" &&
        this.username.length > 6 &&
        this.password.length > 6 &&
        this.password == this.confirm_password &&
        this.img != "" &&
        this.gender != ""
      ) {
        const user = new FormData();
        user.append("username", this.username);
        user.append("password", this.password);
        user.append("email", this.email);
        user.append("nick_name", this.nick_name);
        user.append("first_name", this.first_name);
        user.append("last_name", this.last_name);
        user.append("id_card", this.id_card);
        user.append("phone_number", this.phone_number);
        user.append("birth_date", this.birth_date);
        user.append("img", this.img);
        user.append("gender", this.gender);
        axios
          .post("http://192.168.1.118:8000/user/register/", user)
          .then(() => {
            this.alert = true;
            setTimeout(() => {
              this.alert = false;
              this.$router.push({ name: "Login" });
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
    back() {
      this.$router.push({ name: "Login" });
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
</style>
