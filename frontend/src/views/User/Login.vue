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
        <div class="m-3" v-if="error.status">
          <div class="text-error">
            <img src="../../assets/icon/btn-warning.png" alt="" /> username or
            password is wrong
          </div>
        </div>
        <div class="m" v-else></div>

        <button type="submit" class="btn m" id="btn-login">Login</button>
        <button
          type="button"
          class="btn-ghost m"
          @click="$router.push({ name: 'Register' })"
          id="btn-login"
        >
          Register
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import { api_user } from "../../api/api_user";
import axios from 'axios'
export default {
  name: "Login",
  computed: mapState(["auth"]),
  data() {
    return {
      username: "",
      password: "",
      error: {
        status: true,
      },
    };
  },
  methods: {
    login() {
      const up = {
        username: this.username,
        password: this.password,
      };
      api_user
        .post("is-active/", up)
        .then(() => {
          axios
            .post("http://127.0.0.1:8000/api-token/", up)
            .then((response) => {
              localStorage.setItem("access", response.data.access);
              localStorage.setItem("refresh", response.data.refresh);
              this.$state.commit("newToken", {
                access: response.data.access,
                refresh: response.data.refresh,
              });
              this.api_user
                .get("user-info/", {
                  Authorization: `Bearer ${response.data.access}`,
                })
                .then((response) => {
                  this.$state.commit("updateUserInfo", {
                    userInfo: response.data,
                  });
                });
            });
        })
        .catch(() => {
          this.error.status = true;
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
  beforeCreate() {
    this.username = localStorage.getItem("username");
    this.password = localStorage.getItem("password");
    this.login;
  },
};
</script>

<style>
.m {
  margin: auto;
  margin-bottom: 40px;
}
#btn-login {
  width: 300px;
  height: 70px;
}
</style>