<template>
  <div>
    <nav-app :url_name="'DataBaseSettings'">Sale&#160;Channel</nav-app>
    <div class="row" style="width: 90%; margin: auto">
      <div class="col-8 w-100" style="padding: 0px">
        <search-bar @search="search" style="width: 100%; height: 45px" />
      </div>
      <div
        class="col-2 w-100"
        style="
          padding-left: 12px;
          margin: auto;
          justify-content: space-between;
          display: flex;
        "
      >
        <button
          class="btn-ghost-b"
          style="width: 100%; height: 45px; white-space: nowrap; padding: 0px"
          @click="$router.push({ name: 'CreateSaleChannel' })"
        >
          +&#160;New
        </button>
      </div>
      <div class="col-2 w-100 pe-0 ps-0">
        <button
          class="btn-ghost-r"
          style="width: 100%; height: 45px; white-space: nowrap; padding: 0px"
          v-if="delete_status"
          @click="delete_list_f()"
        >
          <img
            src="../../assets/icon/delete_icon.png"
            style="width: 19px; height: 26px; object-fit: cover"
          />&#160;Delete
        </button>
        <button
          v-else
          class="btn-ghost-r"
          style="width: 125px; height: 45px; white-space: nowrap; padding: 0px"
          @click="delete_status = true"
        >
          <img
            src="../../assets/icon/r-trash.png"
            style="width: 19px; height: 26px; object-fit: cover"
            alt=""
          />&#160;Delete
        </button>
      </div>
    </div>

    <div class="table mt-3">
      <div class="table-header">
        <div class="row">
          <div class="col-5 w-100">Name</div>
          <div class="col-2 w-100">Create&#160;at</div>
          <div class="col-1 w-100 ms-3">Qty</div>
          <div class="col-2 w-100">Status</div>
          <div class="col-1 w-100"></div>
          <div class="col-1 w-100"></div>
        </div>
      </div>
      <div style="overflow-x: auto; height: 650px">
        <div
          v-for="channel in show_channel"
          :key="channel.id"
          class="table-item"
        >
          <div class="row" style="width: 100%; padding: 0px">
            <div class="col-1" 
              v-if="delete_status">
              
              <div class="checkbox-orange" v-if="!channel.can_delete">
                <input
                  type="checkbox"
                  :value="channel.id"
                  v-model="delete_list"
                />
              </div>
              </div>
            <div
              class="col-1 w-100"
              style="margin: auto; margin-left: 0px; text-align: right"
            >
              <span>
                <img :src="channel.img" class="img-user-status me-1" />
              </span>
            </div>
            <div
              class="col-4 w-100"
              v-if="!delete_status"
              style="margin: auto; text-align: left; height: 100%"
            >
              {{ channel.sale_channel }}
            </div>
            <div
              class="col-3 w-100"
              v-else
              style="margin: auto; text-align: left; height: 100%"
            >
              {{ channel.sale_channel }}
            </div>
            <div
              class="col-2 w-100"
              style="margin: auto; text-align: center; height: 100%"
            >
              {{ get_date(channel.create_at) }}
            </div>
            <div
              class="col-1 w-100"
              style="padding: 0px; text-align: right; margin: auto"
            >
              {{ channel.qty }}
            </div>
            <div class="col-2 w-100" style="margin: auto">
              
              <button
                v-if="channel.status"
                class="btn-g"
                style="
                  width: 90px;
                  height: 30px;
                  margin-top: 5px;
                  line-height: 25px;
                  font-weight: bold;
                  font-size: 18px;
                "
              >
                Active
              </button>
              <button
                v-else
                class="btn-r"
                style="
                  width: 90px;
                  height: 30px;
                  margin-top: 5px;
                  line-height: 25px;
                  font-weight: bold;
                  font-size: 18px;
                "
              >
                Inactive
              </button>
            </div>
            <div
              class="col-1 w-100"
              style="margin: auto; text-align: left; padding: 0px; height: 100%"
              @click="
                $router.push({
                  name: 'EditSaleChannel',
                  params: { id: channel.id },
                })
              "
            >
              <img src="../../assets/icon/edit-orange.png" alt="" />
            </div>
            <div
              class="col-1 w-100"
              style="margin: auto; text-align: left; padding: 0px; height: 100%"
              @click="duplicate(channel.id)"
            >
              <img src="../../assets/icon/duplicate.png" alt="" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { api_product } from "../../api/api_product";
import NavApp from "../../components/main_component/NavApp.vue";
import SearchBar from "../../components/materials/SearchBar.vue";
export default {
  components: { NavApp, SearchBar },
  mounted() {
    this.get_sale_channel();
  },
  data() {
    return {
      sale_channels: [],
      show_channel: [],
      delete_list: [],
      delete_status: false,
    };
  },
  methods: {
    get_sale_channel() {
      api_product.get("sale-channel/").then((response) => {
        this.sale_channels = response.data;
        this.show_channel = response.data;
      });
    },
    count_product(id) {
      return id;
    },
    get_date(date) {
      return new Date(date).toLocaleString("th-TH", {
        dateStyle: "short",
      });
    },
    delete_list_f() {
      if (this.delete_list.length != 0) {
        api_product
          .put("delete-sale-channel-by-list/", {
            list: this.delete_list,
          })
          .then((response) => {
            this.get_sale_channel();
          });
      }
      this.delete_status = false;
    },
    get_img(id) {
      api_product
        .get("sale-channel-update-img/" + id + "/")
        .then((response) => {
          return response.data.img;
        });
    },
    search(val) {
      var temp = [];
      if (val == "") {
        this.show_channel = this.sale_channels;
      } else {
        this.sale_channels.forEach((element) => {
          if (element.sale_channel.toLowerCase().indexOf(val.toLowerCase()) + 1 != 0) {
            temp.push(element);
          }
        });
        this.show_channel = temp;
      }
    },
    duplicate(id) {
      this.$store.state.sale_channel.duplicate = true;
      this.$store.state.sale_channel.sale_channel_id = id;
      this.$router.push({ name: "CreateSaleChannel" });
    },
  },
};
</script>

<style scoped>
.row {
  margin: auto;
}
.img-user-status {
  border-radius: 3px;
}
pre {
  margin-bottom: 0px;
}
img {
  height: 30px;
  margin-bottom: 4px;
}
input[type='checkbox'] {
  top:10px;
}
input:checked::after {
  top: -8px !important;
}
</style>