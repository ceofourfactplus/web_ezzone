<template>
  <div>
    <div class="container" >
      <div class="position-absolute top-50 start-50 translate-middle row" >
        <div class="col p-3 bg-light rounded-3" style="width:90vw;">
          <h3 class="mb-3 fw-normal">Please Register</h3>
          <p v-if="incorrectAuth">username has already - please try again</p>
          <form v-on:submit.prevent="register">
            <div class="row mb-3">
              <div class="col">
                <div class="form-group ms-3">
                  <label for="first_name" class="form-label">First name</label>
                  <input
                    type="text"
                    name="username"
                    id="first_name"
                    v-model="first_name"
                    class="form-control form-control-lg"
                  />
                  <div v-show="error_first_name" class="text-danger fw-bold">
                    first name is require
                  </div>
                </div>
              </div>
              <div class="col">
                <div class="form-group me-3">
                  <label for="last_name" class="form-label">Last name</label>
                  <input
                    type="text"
                    name="username"
                    id="last_name"
                    v-model="last_name"
                    class="form-control form-control-lg"
                  />
                </div>
              </div>
            </div>
            <div class="row mb-3">
              <div class="col">
                <div class="form-group ms-3">
                  <label for="username" class="form-label">Username</label>
                  <input
                    type="text"
                    name="username"
                    id="username"
                    v-model="username"
                    class="form-control form-control-lg"
                    placeholder="example"
                  />
                </div>
              </div>
              <div class="col">
                <div class="form-group me-3">
                  <label for="password" class="form-label">Email</label>
                  <input
                    type="email"
                    name="email"
                    id="email"
                    v-model="email"
                    class="form-control form-control-lg"
                    placeholder="example@gamil.com"
                    required
                  />
                </div>
              </div>
            </div>
            <div class="row mb-3">
              <div class="col">
                <div class="form-group ms-3">
                  <label for="password" class="form-label">Password</label>
                  <input
                    type="password"
                    name="password"
                    id="password"
                    v-model="password"
                    class="form-control form-control-lg"
                    placeholder="password"
                    required
                  />
                </div>
              </div>
              <div class="col">
                <div class="form-group me-3">
                  <label for="password" class="form-label">Confirm</label>
                  <input
                    type="password"
                    name="confirm"
                    id="confirm"
                    v-model="confirm"
                    class="form-control form-control-lg"
                    placeholder="confirm"
                  />
                </div>
              </div>
            </div>

            <div class="d-grid gap-1">
              <button type="submit" class="btn btn-primary d-grid gap-2" @clcik="register()">
                Register
              </button>
            </div>
            <div class="row m-2">
              <router-link class="link-dark" :to="{ name: 'Login' }"
                >Login</router-link
              >
            </div>
          </form>
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