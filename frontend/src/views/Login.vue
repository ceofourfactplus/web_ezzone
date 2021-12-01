<template>
  <div>
    <div class="container">
      <div
        class="position-absolute top-50 start-50 translate-middle row"
        style="width: 70vw"
      >
        <div class="col-12 p-3 bg-light rounded-3">
          <h3 class="mb-3 fw-normal">Please Login</h3>
          <p v-if="incorrectAuth">
            Incorrect username or password entered - please try again
          </p>
          <form v-on:submit.prevent="login">
            <div class="form-group m-3">
              <label for="username" class="form-label">Username</label>
              <input
                type="text"
                name="username"
                id="user"
                v-model="username"
                class="form-control form-control-lg"
              />
            </div>
            <div class="form-group m-3">
              <label for="password" class="form-label">Password</label>
              <input
                type="password"
                name="password"
                id="pass"
                v-model="password"
                class="form-control form-control-lg"
              />
            </div>
            <div class="d-grid gap-1">
              <button type="submit" class="btn btn-primary d-grid gap-2">
                Login
              </button>
            </div>
          </form>
          <div class="row mt-3">
            <router-link class="link-dark" :to="{ name: 'Register' }"
              >Register</router-link
            >
          </div>
        </div>
      </div>
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
      incorrectAuth: false,
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
          console.log(err);
          this.incorrectAuth = true;
        });
    },
  },
  beforeCreate() {
    const username = localStorage.getItem('username');
    const password = localStorage.getItem('password');
    this.$store.dispatch("auth/userLogin", {
      username: username,
      password: password,
    }).then(() => {
          console.log("1");
          this.$router.push({ name: "Home" });
        })
        .catch((err) => {
          console.log(err);
          this.incorrectAuth = true;
        });
    console.log('dispatch')
  },
};
</script>

<style>
</style>