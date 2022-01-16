<template>
  <div>
    <nav class="nav">
      <div class="row">
        <div class="col-12">
          <p id="login" class="header-text">Forgot Password</p>
        </div>
      </div>
    </nav>
    <div class="c">
      <div class="container">
        <form @submit="login">
          <div class="col-12 mt-2">
            <input
              type="number"
              id="id_card"
              v-model="id_card"
              placeholder="ID Card"
              aria-label=".form-control-lg example"
            />
          </div>
          <div class="col-12 mt-4">
            <input
              v-model="password"
              type="password"
              placeholder="Password"
              aria-label=".form-control-lg example"
            />
          </div>
          <div class="col-12 mt-4">
            <input
              v-model="confirm_password"
              type="password"
              placeholder="Confirm Password"
              aria-label=".form-control-lg example"
            />
          </div>
          <div class="col-12 mt-4">
            <div class="m-2" v-if="error.status">
              <div class="text-error">
                <img src="../../assets/icon/btn-warning.png" alt="" />
                {{ error.data }}
              </div>
            </div>
            <div class="m-2" v-else></div>
          </div>
          <div class="col-12">
            <button type="submit" class="btn mt-2" id="btn-submit">
              Confirm
            </button>
          </div>
          <div class="col-12 mt-3">
            <router-link
              :to="{name:'Login'}"
              style="color: #fff; font-size: 24px; text-decoration: underline"
              >login</router-link
            >
          </div>
        </form>
      </div>
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
      id_card: "",
      password: "",
      confirm_password: "",
      error: {
        status: false,
        data: "",
      },
      alert: false,
      query: [],
    };
  },
  methods: {
    change_password() {
      if (this.confirm_password == this.password) {
        api_user
          .post("change-password/" + this.query[0].id, {
            new_password: this.password,
          })
          .then(() => {
            this.$router.push({ name: "Login" });
          })
          .catch((err) => {
            this.error.status = true;
            this.error.data = err.response.data;
          });
      }
    },
  },
  watch: {
    id_card(newData) {
      if (newData.length > 9) {
        api_user.get("check-is-card/" + newData).then((response) => {
          this.query = response.data;
        });
      }
    },
  },
};
</script>

<style scoped>
.nav {
  height: 100px;
}
.header-text {
  font-style: normal;
  font-weight: 800;
  font-size: 72px;
  top: 50px;
  color: #fafafa;
  position: fixed;
  width: 100%;
}
#btn-submit {
  width: 270px;
  height: 60px;
}
.img {
  position: fixed;
  z-index: 1;
}
input {
  width: 90%;
  height: 70px;
}
</style>