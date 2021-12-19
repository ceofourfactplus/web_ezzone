<template>
  <div>
    <nav-app style="margin-bottom: 0px">Customer Data</nav-app>
    <div class="container-fluid">
      <!-- detail  -->
      <div
        class="row"
        style="margin-top: 0px; margin-left: 20px; height: 230px"
      >
        <!-- img -->
        <div class="col-3 w-100">
          <div class="row">
            <div class="col-12">
              <label for="file">
                <img
                  v-if="show_img == null"
                  width="160"
                  height="160"
                  src="../../assets/icon/User.png"
                  style="border-radius: 50%;left:0px"
                />
                <img
                  v-else
                  :src="show_img"
                  width="160"
                  style="border-radius: 50%;left:0px"
                  height="160"
                />
              </label>
              <input
                type="file"
                @change="onFileChange"
                style="display: none"
                id="file"
                class="register-user"
              />
            </div>
          </div>
          <div class="row">
            <div class="col-12" style="width: 200px">
              <div class="row">
                <div class="checkbox-white">
                  <div class="row">
                    <div class="col-4">
                      <input
                        type="radio"
                        class="me-3 mt-2"
                        v-model="user.gender"
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
                        v-model="user.gender"
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

          <!-- <check-box-white/> -->
        </div>
        <div class="col-9 w-100">
          <div class="row" style="height: 160px">
            <div class="col-4">
              <h>Point</h>
            </div>
            <div class="col-4"></div>
            <div class="col-4"></div>
          </div>
          <div class="row"></div>
        </div>
      </div>

      <!-- form -->
      <div class="row" style="margin-top: 30px">
        <div class="col-12">
          <div class="row mb-3">
            <div class="col-3 w-100">
              <label for="first_name">First Name</label>
            </div>
            <div class="col-9 w-100">
              <input type="text" v-model="user.first_name" id="first_name" />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-3 w-100">
              <label for="last_name">Last Name</label>
            </div>
            <div class="col-9 w-100">
              <input type="text" v-model="user.last_name" id="last_name" />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-3 w-100">
              <label for="nick_name">Nick Name</label>
            </div>
            <div class="col-9 w-100">
              <input type="text" v-model="user.nick_name" id="nick_name" />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-3 w-100">
              <label for="birth_date">Birth Date</label>
            </div>
            <div class="col-9 w-100">
              <input
                type="text"
                class="textbox-n"
                onfocus="(this.type='date')"
                v-model="user.birth_date"
                id="birth_date"
              />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-3 w-100">
              <label for="phone_number">Phone No.</label>
            </div>
            <div class="col-9 w-100">
              <input
                type="number"
                v-model="user.phone_number"
                id="phone_number"
              />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-3 w-100">
              <label for="email" style="margin-left: -25px">Email</label>
            </div>
            <div class="col-9 w-100">
              <input type="email" v-model="user.email" id="email" />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-3 w-100">
              <label for="id_card">ID Number</label>
            </div>
            <div class="col-9 w-100">
              <input type="number" v-model="user.id_card" id="id_card" />
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- blur -->
    <div class="blur" v-if="blur" @click="blur = false">
      <div class="card-status">
        <div class="row mt-4">
          <div class="col-6 w-100 m-auto">
            <img
              v-if="user.img != null"
              class="img-select me-2"
              :src="user.img"
              alt=""
            />
            <img
              v-else
              src="../../assets/icon/blank-user.png"
              class="img-select me-2"
              alt=""
            />
          </div>
          <div class="col-6" id="test">
            <p style="color: #fff">{{ user.first_name }}</p>
          </div>
        </div>
        <div class="col-12 mt-3 w-100 m-auto">
          <button
            v-if="user.is_working == 1"
            class="mt-4 btn-g"
            style="width: 80%; height: 70px"
          >
            Active
          </button>
          <button
            v-else
            @click="change_status(1)"
            class="mt-4 btn-ghost-g"
            style="width: 80%; height: 70px"
          >
            Active
          </button>
          <button
            v-if="user.is_working == 2"
            class="mt-4 btn-b"
            style="width: 80%; height: 70px"
          >
            Banned
          </button>
          <button
            v-else
            @click="change_status(2)"
            class="mt-4 btn-ghost-b"
            style="width: 80%; height: 70px"
          >
            Banned
          </button>
          <button
            v-if="user.is_working == 0"
            class="mt-4 btn-r"
            style="width: 80%; height: 70px"
          >
            Inactive
          </button>
          <button
            v-else
            @click="change_status(0)"
            class="mt-4 btn-ghost-r"
            style="width: 80%; height: 70px"
          >
            Inactive
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { api_user } from "../../api/api_user";
import NavApp from "../../components/main_component/NavApp.vue";
export default {
  name: "EditUser",
  components: { NavApp },
  data() {
    return {
      user: {},
      blur: false,
      show_img: null,
      new_img: false,
    };
  },
  methods: {
    status_color() {
      if (!this.user.is_active) {
        return "Wait for Activate";
      }
      if (this.user.is_working == 1) {
        return "Actvate";
      }
      if (this.user.is_working == 2) {
        return "Banned";
      }
      if (this.user.is_working == 0) {
        return "Inavtive";
      }
    },
    onFileChange(e) {
      this.user.img = e.target.files[0];
      this.new_img = true;
      if (this.user.img) {
        const reader = new FileReader();
        reader.onload = (e) => (this.show_img = e.target.result);
        reader.readAsDataURL(this.user.img);
      }
    },
    back() {
      this.$router.push({ name: "UserStatus" });
    },
    change_status(status) {
      this.user.is_working = status;
    },
    check_status() {
      if (
        !this.user.is_chef &&
        !this.user.is_barista &&
        !this.user.is_receptionish &&
        !this.user.is_staff &&
        !this.user.is_purchesing
      ) {
        console.log("woo");
        this.user.is_working = 0;
      }
      console.log("new");
    },
    edit_user() {
      const user_data = new FormData();
      user_data.append("is_chef", this.user.is_chef);
      user_data.append("is_barista", this.user.is_barista);
      user_data.append("is_purchesing", this.user.is_purchesing);
      user_data.append("is_receptionist", this.user.is_receptionist);
      user_data.append("is_staff", this.user.is_staff);
      user_data.append("username", this.user.username);
      user_data.append("password", this.user.password);
      user_data.append("email", this.user.email);
      user_data.append("first_name", this.user.first_name);
      user_data.append("last_name", this.user.last_name);
      user_data.append("nick_name", this.user.nick_name);
      user_data.append("id_card", this.user.id_card);
      user_data.append("phone_number", this.user.phone_number);
      user_data.append("is_active", true);
      if (this.new_img) {
        user_data.append("img", this.user.img, this.user.img.name);
      }
      user_data.append("gender", this.user.gender);
      api_user.put("edit-user/" + this.user.id, user_data).then(() => {
        this.$router.go(-1);
      });
    },
  },

  mounted() {
    api_user.get("edit-user/" + this.$route.params.id).then((reponse) => {
      this.user = reponse.data;
      if (this.user.img != null) {
        this.show_img = this.user.img;
      }
    });
  },
  watch: {
    user() {
      this.check_status();
    },
  },
};
</script>

<style scoped>
#alert {
  font-weight: 600;
  height: 45px;
  font-size: 18px;
  width: 630px;
  text-align: center;
  line-height: 40px;
  margin: auto;
}
#text {
  margin-top: 20px;
}
#img {
  margin-right: 10px !important;
  margin-bottom: 0px !important;
}
#header {
  margin-left: 25px;
  color: #ea7c69;
  font-weight: 700;
}
/* 
label img {
  top: 100px;
  left: 20px;
}

.gender {
  position: fixed;
  top: 280px;
  left: 50px;
  color: #ffffff;
} */

.status {
  top: 110px;
  right: 80px;
  position: fixed;
}

.col-3 label {
  font-size: 24px;
  margin: auto;
  font-weight: 700;
  color: #ffb572;
}

input[type="email"],
input[type="date"],
input[type="text"],
input[type="number"] {
  width: 100%;
  height: 45px;
}

.btn-ghost {
  width: 300px;
  height: 70px;
  font-weight: 600;
  font-size: 36px;
  line-height: 10px;
}
</style>