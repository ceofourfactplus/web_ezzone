<template>
  <div
    class="modal fade"
    id="CustomerForm"
    tabindex="-1"
    aria-labelledby="TableLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="TableLabel">Customer Form</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <form class="row g-3" @submit="save_customer">
            <div class="col-md-6">
              <div class="row">
                <label for="firstname" class="form-label col-4"
                  >First Name</label
                >
                <div class="col-8">
                  <input
                    type="text"
                    v-model="first_name"
                    class="form-control"
                    id="firstname"
                    required
                  />
                </div>
              </div>
            </div>
            <div class="col-md-6">
              <div class="row">
                <label for="lastname" class="form-label col-4">Last Name</label>
                <div class="col-8">
                  <input
                    type="text"
                    v-model="last_name"
                    class="form-control"
                    id="lastname"
                  />
                </div>
              </div>
            </div>
            <div class="col-md-6">
              <div class="row">
                <label for="phonenumber" class="form-label col-4"
                  >Phone Number</label
                >

                <div class="col-8">
                  <input
                    type="tel"
                    v-model="phone_number"
                    pattern="[0]{1}[0-9]{2}-[0-9]{3}-[0-9]{4}"
                    class="form-control"
                    id="phonenumber"
                    required
                  />
                </div>
              </div>
            </div>
            <div class="col-md-6">
              <div class="row">
                <label for="gender" class="col-4">Gender</label>
                <div class="col-8">
                  <select
                    id="gender"
                    v-model="gender"
                    class="form-select"
                    aria-label="Default select example"
                  >
                    <option selected>Open this to select gender</option>
                    <option value="male">male</option>
                    <option value="female">Female</option>
                  </select>
                </div>
              </div>
            </div>
            <div class="col-md-6">
              <div class="row">
                <label for="inputAddress" class="form-label col-4"
                  >Address</label
                >
                <div class="col-8">
                  <input
                    v-model="address"
                    type="text"
                    class="form-control"
                    id="inputAddress"
                    placeholder="1234 Main St"
                  />
                </div>
              </div>
            </div>
            <div class="col-md-3">
              <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1">ซ.</span>
                <input
                  type="text"
                  v-model="alley"
                  class="form-control"
                  aria-label="Username"
                  aria-describedby="basic-addon1"
                  required
                />
              </div>
            </div>
            <div class="col-md-3">
              <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1">#</span>
                <input
                  type="text"
                  v-model="house_number"
                  class="form-control"
                  aria-label="Username"
                  aria-describedby="basic-addon1"
                  required
                />
              </div>
            </div>
            <div class="col-12">
              <button type="submit" class="btn btn-primary">Sign in</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CustomerForm",
  data() {
    return {
      first_name: "",
      last_name: "",
      phone_number: "",
      gender: "",
      address: "",
      alley: "",
      house_number: "",
    };
  },
  methods: {
    save_customer() {
      this.$emit("save_customer", {
        first_name: this.first_name,
        last_name: this.last_name,
        phone_number: this.phone_number,
        gender: this.gender,
        address: this.address,
        alley: this.alley,
        house_number: this.house_number,
      });
    },
  },
};
</script>

<style>
</style>