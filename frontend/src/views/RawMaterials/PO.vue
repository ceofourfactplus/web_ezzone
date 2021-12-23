<template>
  <div>
    <!-- Head -->
    <nav-app>PO&#160;Notice</nav-app>
    <div class="row" style="width: 100%; margin-left: 25px" v-if="permisstion">
      <div class="col-9 wrap-search w-100">
        <SearchBar @search="serchByTyping" style="width: 98%" />
      </div>
      <div class="col-3 w-100" style="padding-left: 0px; text-align: left">
        <button class="btn-ghost-b" style="width: 120px">+&#160;PO</button>
      </div>
    </div>
    <div class="table mt-3">
      <div class="table-header" style="line-height: 40px; font-size: 24px">
        <div class="row">
          <div class="col-5 w-100">Item</div>
          <div class="col-1 w-100">Qty.</div>
          <div class="col-2 w-100">Unit</div>
          <div class="col-2 w-100">Min&#160;Sup</div>
          <div class="col-2 w-100">Status</div>
        </div>
      </div>
      <div style="overflow-x: auto; height: 650px">
        <div v-for="item in rm" :key="item.id" class="table-item">
          <div class="row" style="width: 100%">
            <div
              class="col-5 w-100"
              style="margin: auto; margin-left: 0px; text-align: left"
            ></div>
            <div class="col-1 w-100" style="margin: auto; text-align: left">

              {{ item.remain }}
            </div>
            <div
              class="col-2 w-100"
              style="margin: auto; width: 175px; text-align: left"
            >
              {{ item.unit_set.unit }}
            </div>
          </div>
          <div
            class="col-2 w-100"
            style="margin: auto; width: 175px; text-align: left"
          >
            {{ get_sup(item) }}
          </div>
          <div
            class="col-2 w-100"
            style="margin: auto; text-align: left; padding: 0px"
          >
            <img :src="get_status(item.status)" alt="" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { api_raw_material } from "../../api/api_raw_material";
import Tabs from "../../components/materials/Tabs.vue";
import SearchBar from "../../components/materials/SearchBar.vue";
import NavApp from "../../components/main_component/NavApp.vue";
import Table from "../../components/main_component/Table.vue";
import PickupPopup from "../../components/materials/PickupPopup.vue";
import RMDetailPopup from "../../components/materials/RMDetailPopup.vue";
import { resolveTransitionHooks } from '@vue/runtime-core';

export default {
  components: {
    SearchBar,
    NavApp,
    Table,
  },
  mounted() {
    this.get_raw();
  },

  data() {
    return {
    };
  },
  methods: {
    get_raw() {
      api_raw_material.get("rm-po/notice").then((response) => {
        console.log(response.data, "data");
        this.raw_materials = response.data;
        this.temp_rm = response.data;
      });
    },
    get_sup(item){
      api_raw_material.get('rm/get-sup',item.id).then((response)=>{
        return response.data.supplier
      })
    },
    get_status(status){
      if(status == 2){return require('../../assets/icon/warning.png')}
      if(status == 3){return require('../../assets/icon/incorrect.png')}
    }
  },
};
</script>

<style scoped>
</style>