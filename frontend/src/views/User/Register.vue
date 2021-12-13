<template>
  <div class="c" style="top: 20px">
    <img src="../../assets/icon/btn-back.png" class="back" alt="" />
    <div class="container">
      <h1 id="login">Registration</h1>
      <div class="row">
        <div class="col-3">
          <img class="register-user" src="../../assets/icon/User.png" alt="">
        </div>
        <div class="col-9">
          <div class="row">
            <div class="col-2"></div>
            <div class="col-10">
              <input
              type="text"
              placeholder="Username"
              aria-label=".form-control-lg example"
              style="width:420px;"
            />
            </div>
            
          </div>
          <div class="row">
            <div class="col-2"></div>
            <div class="col-10">
              <input
              type="text"
              placeholder="Username"
              aria-label=".form-control-lg example"
              style="width:420px;"
            />
            </div>
            
          </div>
          <div class="row">
            <div class="col-2"></div>
            <div class="col-10">
              <input
              type="text"
              placeholder="Username"
              aria-label=".form-control-lg example"
              style="width:420px;"
            />
            </div>
            
          </div>
          <div class="row">
            <div class="col-2"></div>
            <div class="col-10">
              <input
              type="text"
              placeholder="Username"
              aria-label=".form-control-lg example"
              style="width:420px;"
            />
            </div>
            
          </div>
          <div class="row">
            <div class="col-2"></div>
            <div class="col-10">
              <input
              type="text"
              placeholder="Username"
              aria-label=".form-control-lg example"
              style="width:420px;"
            />
            </div>
            
          </div>
          <div class="row">
            <div class="col-2"></div>
            <div class="col-10">
              <input
              type="text"
              placeholder="Username"
              aria-label=".form-control-lg example"
              style="width:420px;"
            />
            </div>
            
          </div>
          <div class="row">
            <div class="col-2"></div>
            <div class="col-10">
              <input
              type="text"
              placeholder="Username"
              aria-label=".form-control-lg example"
              style="width:420px;"
            />
            </div>
            
          </div>
          <div class="row">
            <div class="col-2"></div>
            <div class="col-10">
              <input
              type="text"
              placeholder="Username"
              aria-label=".form-control-lg example"
              style="width:420px;"
            />
            </div>
            
          </div>
          <div class="row">
            <div class="col-2"></div>
            <div class="col-10">
              <input
              type="text"
              placeholder="Username"
              aria-label=".form-control-lg example"
              style="width:420px;"
            />
            </div>
            
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Register",
  data() {
    return {
      username: "",
      password: "",
      confirm: "",
      email: "",
      first_name: "",
      last_name: "",
      incorrectAuth: false,
      error_password_length: false,
      error_username_length: false,
      error_password_require: false,
      error_username_require: false,
      error_first_name: false,
      error_last_name: false,
      error_confirm: false,
      error_email: false,
    };
  },
  methods: {
    register() {
      if (this.password != this.confirm) {
        this.error_confirm = true;
      } else if (this.first_name == "") {
        this.error_first_name = true;
      } else if (this.password.length <= 7) {
        this.error_password_length = true;
      } else if (this.username.length <= 4) {
        this.error_username_length = true;
      } else {
        axios
          .post("http://127.0.0.1:8000/auth/register/", {
            username: this.username,
            password: this.password,
            email: this.email,
            first_name: this.first_name,
            last_name: this.last_name,
          })
          .then(() => {
            this.$router.push({ name: "Login" });
          })
          .catch((err) => {
            console.log(err);
            this.incorrectAuth = true;
          });
      }
    },
  },
};
</script>

<style>
</style>