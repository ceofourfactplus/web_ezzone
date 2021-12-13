<template>
  <div class="c">
    <div class="container">
      <h1 id="login">Login</h1>
      <div class="arrow"><img src="https://www.figma.com/file/it3vEPwSA4GGwyfUFZo4no/EZ-wireframe_3(Dark-tone)?node-id=233%3A2021" alt=""></div>
      <form @submit="login">
        <div class="alert alert-error m" v-if="error.status">
          <div class="row">
            <div class="col-3">
              <img src="../../assets/img/btn-error.png" style="height:100%" alt="" />
            </div>
            <div class="col-9"><div class="text-error">{{ error.data }}</div></div>
          </div>
        </div>
        <div class="col-12 m">
          <input
            type="text"
            v-model="username"
            placeholder="Username"
            aria-label=".form-control-lg example"
          />
        </div>
        <div class="col-12 m">
          <input
            v-model="password"
            type="password"
            placeholder="Password"
            aria-label=".form-control-lg example"
          />
        </div>
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
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      error: {
        status: true,
        data: "",
      },
    };
  },
  methods: {
    login() {
      this.$store
        .dispatch("auth/userLogin", {
          username: this.username,
          password: this.password,
        })
        .then(() => {
          console.log("1");
          this.$router.push({ name: "Home" });
        })
        .catch((err) => {
          this.error.status=true
          this.error.data = err.error.data
        });
    },
  },
  watch:{
    username(){this.error.status = false},
    password(){this.error.status = false},
  },
  beforeCreate() {
    const username = localStorage.getItem("username");
    const password = localStorage.getItem("password");
    this.$store
      .dispatch("auth/userLogin", {
        username: username,
        password: password,
      })
      .then(() => {
        console.log("1");
        this.$router.push({ name: "Home" });
      })
      .catch((err) => {
        console.log(err);
        this.incorrectAuth = true;
      });
    console.log("dispatch");
  },
};
</script>

<style>
.c {
  position: relative;
  margin: auto;
  top: 100px;
}
.m {
  margin: auto;
  margin-bottom: 40px;
}
#login {
  font-family: Sarabun;
  font-style: normal;
  font-weight: bold;
  font-size: 72px;
  line-height: 94px;
  color: #fafafa;
  margin-bottom: 40px;
}
#btn-login {
  width: 300px;
  height: 70px;
}
</style>