<template>
  <div>
    <nav-app :url_name="'DashBoard'">User Status</nav-app>
    <div style="width: 90%; margin: auto"><search-bar @search="search" /></div>

    <div class="table mt-3">
      <div class="table-header">
        <div class="row h-100" style="width: 100%">
          <div
            class="col-4"
            style="margin: auto; padding-bottom: 9px; padding-top: 3px"
          >
            Name
          </div>
          <div
            class="col-4"
            style="margin: auto; padding-bottom: 9px; padding-top: 3px"
          >
            Role
          </div>
          <div
            class="col-2"
            style="
              margin: auto;
              margin-left: 30px;
              padding-bottom: 9px;
              padding-top: 3px;
            "
          >
            Status
          </div>
          <div
            class="col-2"
            style="margin: auto; padding-bottom: 9px; padding-top: 3px"
          >
            Edit
          </div>
        </div>
      </div>
      <div style="overflow-x: auto; height: 650px">
        <div v-for="user in all_user" :key="user.id" class="table-item">
          <div class="row" style="width: 100%">
            <div
              class="col-4"
              style="margin-left: 15px; width: 100%; display: flex"
            >
              <div>
                <img
                  v-if="user.img != null"
                  class="img-user-status me-2"
                  :src="user.img"
                  alt=""
                />
                <img
                  v-else
                  src="../../assets/icon/blank-user.png"
                  class="img-user-status me-2"
                  alt=""
                />
                <span>{{ user.nick_name }}</span>
              </div>
            </div>
            <div class="col-4" style="margin-left: 10px; width: 100%;line-height:35px;">
              {{ role(user) }}
            </div>
            <div
              class="col-2"
              style="margin: auto; margin-left: 60px; width: 100%"
            >
              <div
                class="status-circle"
                @click="SelectUser(user)"
                :style="{ 'background-color': status_color(user) }"
              ></div>
            </div>
            <div
              class="col-2"
              style="margin: auto; margin-left: 30px; width: 80%"
            >
              <img
                src="../../assets/icon/edit-user.png"
                alt=""
                style="height:27px;"
                @click="ToEditUser(user)"
              />
            </div>
          </div>
        </div>
      </div>
      <div class="table-bottom">
        <div class="row">
          <div class="col-3" style="width: 100%; line-height: 25px">
            <div class="row">
              <div class="col-2 me-1">
                <div
                  class="status-circle ms-1 me-1"
                  style="background-color: #fff500"
                ></div>
              </div>
              <div class="col-9 ms-2">Waiting</div>
            </div>
          </div>
          <div class="col-3" style="width: 100%; line-height: 25px">
            <div class="row">
              <div class="col-2 me-1">
                <div
                  class="status-circle ms-1 me-1"
                  style="background-color: #50d1aa"
                ></div>
              </div>
              <div class="col-9 ms-2">Active</div>
            </div>
          </div>
          <div class="col-3" style="width: 100%; line-height: 25px">
            <div class="row">
              <div class="col-2 me-1">
                <div
                  class="status-circle ms-1 me-1"
                  style="background-color: #ff7ca3"
                ></div>
              </div>
              <div class="col-9 ms-2">Inactive</div>
            </div>
          </div>
          <div class="col-3" style="width: 120%; line-height: 25px">
            <div class="row">
              <div class="col-2 me-1">
                <div
                  class="status-circle ms-1 me-1"
                  style="background-color: #65b0f6"
                ></div>
              </div>
              <div class="col-9 ms-2">Banned</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="blur" v-if="blur" @click="blur = false">
      <div class="card-status">
        <div class="row mt-4">
          <div class="col-6 w-100 m-auto">
            <img
              v-if="select_user.img != null"
              class="img-select me-2"
              :src="select_user.img"
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
            <p style="color: #fff">{{ select_user.first_name }}</p>
          </div>
        </div>
        <div class="col-12 mt-3 w-100 m-auto">
          <button
            v-if="select_user.is_working == 1 && select_user.is_active == true"
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
            v-if="select_user.is_working == 2"
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
            v-if="select_user.is_working == 0"
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
import SearchBar from "../../components/materials/SearchBar.vue";
export default {
  components: { NavApp, SearchBar },
  data() {
    return {
      all_user: [],
      blur: false,
      select_user: {},
    };
  },
  mounted() {
    api_user.get("read-all/").then((response) => {
      this.all_user = response.data;
    });
  },
  methods: {
    role(user) {
      var output = "";

      if (user.is_barista) {
        output = output + "B";
      }
      if (user.is_staff) {
        if (output.length != 0) output = output + "/";
        output = output + "M";
      }
      if (user.is_chef) {
        if (output.length != 0) output = output + "/";
        output = output + "C";
      }
      if (user.is_receptionish) {
        if (output.length != 0) output = output + "/";
        output = output + "R";
      }
      if (user.is_purchesing) {
        if (output.length != 0) output = output + "/";
        output = output + "P";
      }
      if (user.is_owner) {
        if (output.length != 0) output = output + "/";
        output = output + "O";
      }
      if (output.length == 0) output = "-";

      return output;
    },
    status_color(user) {
      if (!user.is_active) {
        return "#fff500";
      }
      if (user.is_working == 1) {
        return "#50D1AA";
      }
      if (user.is_working == 2) {
        return "#65b0f6";
      }
      if (user.is_working == 0) {
        return "#ff7ca3";
      }
    },
    search(val) {
      if (val != "") {
        api_user.get("search-name/" + val).then((response) => {
          this.all_user = response.data;
        });
      } else {
        api_user.get("read-all/").then((response) => {
          this.all_user = response.data;
        });
      }
    },
    SelectUser(user) {
      this.blur = true;
      this.select_user = user;
    },
    change_status(status) {
      api_user
        .put("change-status/" + this.select_user.id + "/" + status)
        .then(() => {
          api_user.get("read-all/").then((response) => {
            this.all_user = response.data;
          });
        });
    },
    ToEditUser(user) {
      this.$router.push({ name: "EditUser", params: { id: user.id } });
    },
  },
};
</script>

<style scoped>
.row div {
  line-height: 100%;
}
.row {
  padding: 3px;
  margin: 0px;
}
.img-user-status {
  width: 34px;
  height: 34px;
  object-fit: cover;
}
.img-select{
  object-fit: cover;
}
</style>