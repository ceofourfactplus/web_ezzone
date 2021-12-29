<template>
  <div>
    <nav-app>Sale&#160;Channel</nav-app>
    <div class="row" style="width: 90%; margin: auto">
      <div class="col-7 w-100" style="padding: 0px">
        <search-bar @search="search" style="width: 100%" />
      </div>
      <div
        class="col-5 w-100"
        style="
          padding-right: 0px;
          padding-left: 12px;
          margin: auto;
          justify-content: space-between;
          display: flex;
        "
      >
        <button
          class="btn-ghost-b"
          style="width: 125px; height: 50px"
          @click="$router.push({ name: 'CreateChannel' })"
        >
          +&#160;New</button
        ><button
          class="btn-ghost-r"
          style="width: 125px; height: 50px"
          @click="$router.push({ name: 'CreateChannel' })"
        >
          <img src="../../assets/icon/bin.png" width="20" alt="" />&#160;Delete
        </button>
      </div>
    </div>

    <div class="table mt-3">
      <div class="table-header" style="line-height: 40px; font-size: 24px">
        <div class="row">
          <div class="col-4 w-100" style="">Name</div>
          <div class="col-1"></div>
          <div class="col-2 w-100" style="">
            Create&#160;at
          </div>
          <div class="col-1 w-100" style="padding:0px;text-align:right;margin:auto;">
            Qty
          </div>
          <div class="col-2 w-100">Status</div>
          <div class="col-1 w-100"></div>
          <div class="col-1 w-100"></div>
        </div>
      </div>
      <div style="overflow-x: auto; height: 650px">
        <div
          v-for="channel in sale_channels"
          :key="channel.id"
          class="table-item"
        >
          <div class="row" style="width: 100%">
            <div
              class="col-1 w-100"
              style="margin: auto; margin-left: 0px; text-align: right"
            >
              <span>
                <img
                  v-if="channel.img != null"
                  :src="channel.img"
                  class="img-user-status me-1"
                /><img
                  v-else
                  src="../../assets/icon/blank-user.png"
                  class="img-user-status me-1"
                />
              </span>
            </div>
            <div
              class="col-3 w-100"
              style="margin: auto; text-align: left"
            >
              {{ channel.sale_channel }}
            </div>
            <div class="col-1"></div>
            <div
              class="col-2 w-100"
              style="margin: auto; text-align: left"
            >
              {{ channel.create_at }}
            </div>
            <div
              class="col-1 w-100"
               style="padding:0px;text-align:right;margin:auto;"
            >
              {{ count_product(channel.id)}}
            </div>
            <div
              class="col-2 w-100"
              style="margin: auto;"
            >
              {{ channel.status }}
            </div>
            <div
              class="col-1 w-100"
              style="margin: auto; text-align: left; padding: 0px"
            >
              <img src="../../assets/icon/edit-orange.png" style="width:55%" alt="">
            </div>
            <div
              class="col-1 w-100"
              style="margin: auto; text-align: left; padding: 0px"
            >
              <img src="../../assets/icon/duplicate.png" style="width:70%" alt="">
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
    this.get_sale_channel()
  },
  data() {
    return {
      sale_channels: [],
    };
  },
  methods: {
    get_sale_channel() {
      api_product.get("sale-channel/").then((response) => {
        this.sale_channels = response.data;
      });
    },
    count_product(id){
      return id
    }
  },
};
</script>

<style scoped>
.row{
  margin:auto
}
.img-user-status{
  border-radius: 3px;
}
</style>