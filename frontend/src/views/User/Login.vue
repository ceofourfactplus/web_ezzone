<template>
  <div class="c">
    <div class="container">
      <h1 id="login">Login</h1>
      <div class="arrow">
        <img
          src="https://www.figma.com/file/it3vEPwSA4GGwyfUFZo4no/EZ-wireframe_3(Dark-tone)?node-id=233%3A2021"
          alt=""
        />
      </div>
      <form @submit="login">
        <!-- <div class="alert alert-error m" v-if="error.status">
          <div class="row">
            <div class="col-3">
              <img src="../../assets/img/btn-error.png" style="height:100%" alt="" />
            </div>
            <div class="col-9"><div class="text-error">{{ error.data }}</div></div>
          </div>
        </div> -->
        <div class="col-12 m">
          <input
            type="text"
            v-model="username"
            placeholder="Username"
            aria-label=".form-control-lg example"
          />
        </div>
        <div class="col-12" style="margin-bottom: 10px">
          <input
            v-model="password"
            type="password"
            placeholder="Password"
            aria-label=".form-control-lg example"
          />
        </div>
        <div class="col-12"></div>
        <div class="m-3" v-if="error.status">
          <div class="text-error">
            <img src="../../assets/icon/btn-warning.png" alt="" />
            password or username is inactive
          </div>
        </div>
        <div class="m" v-else></div>

        <button type="submit" class="btn m mt-2 col-12" id="btn-login">
          Login
        </button>
        <div class="col-12">
          <button
            type="button"
            class="btn-ghost"
            @click="$router.push({ name: 'Register' })"
            id="btn-login"
          >
            Register
          </button>
        </div>
        <div class="col-12 mt-3 w-100">
          <router-link
            :to="{ name: 'ForgotPassword' }"
            style="color: #fff; font-size: 18px; text-decoration: underline"
            >Forget password</router-link
          >
        </div>
      </form>
    </div>
    <div class="card" :class="{ 'card-active': alert }">
      <div class="icon">
        <img src="../../assets/icon/btn-pass.png" alt="" />
      </div>
      <div class="main-text">Login already</div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import { api_user } from "../../api/api_user";
export default {
  name: "Login",
  computed: mapState(["auth"]),
  data() {
    return {
      username: "",
      password: "",
      error: {
        status: false,
        data: "",
      },
      alert: false,
    };
  },
  methods: {
    login() {
      api_user
        .post("login/", {
          username: this.username,
          password: this.password,
        })
        .then((response) => {
          this.auth.accessToken = response.data.token;
          this.auth.userInfo = response.data.user_set;
          this.$router.push({ name: "DashBoard" });
        })
        .catch((err) => {
          console.log(err);
          this.error.status = true;
          this.error.data = err.response.data;
        });
    },
  },
  watch: {
    username() {
      this.error.status = false;
    },
    password() {
      this.error.status = false;
    },
  },
};
</script>

<style scoped>
.m {
  margin: auto;
  margin-bottom: 20px;
}
input {
  height: 80px !important;
}
#btn-login {
  width: 300px;
  height: 70px;
}
</style>