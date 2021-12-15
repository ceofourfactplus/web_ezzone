<template>
  <div>
    <nav-app>User Status</nav-app>
    <search-bar />
    <div class="table mt-4">
      <div class="table-header">
        <div class="row" style="width: 100%">
          <div class="col-4" style="margin: auto;padding-bottom:9px;padding-top:3px;">Name</div>
          <div class="col-4" style="margin: auto;padding-bottom:9px;padding-top:3px;">Role</div>
          <div class="col-2" style="margin: auto;margin-left: 30px;padding-bottom:9px;padding-top:3px;">Status</div>
          <div class="col-2" style="margin: auto;padding-bottom:9px;padding-top:3px;">Edit</div>
        </div>
      </div>
      <div style="overflow-x: auto; height: 650px">
        <div v-for="n in 10" :key="n" class="table-item">
          <div class="row" style="width: 100%">
            <div
              class="col-4"
              style="margin-left: 15px; width: 100%; display: flex"
            >
              <div>
                <img
                  class="img-user-status me-1"
                  src="../../assets/icon/download.jpeg"
                  alt=""
                /><span>Trin tin tin</span>
              </div>
            </div>
            <div class="col-4" style="margin-left: 10px; width: 100%">
              B/C/M/R/P
            </div>
            <div
              class="col-2"
              style="margin: auto; margin-left: 60px; width: 100%"
            >
              <div class="status-circle"></div>
            </div>
            <div
              class="col-2"
              style="margin: auto; margin-left: 30px; width: 100%"
            >
              <img src="../../assets/icon/edit-user.png" alt="" />
            </div>
          </div>
        </div>
      </div>
      <div class="table-bottom">
        <div class="row">
          <div class="col-3" style="width: 100%; line-height:25px">
            <div class="row">
              <div class="col-2 me-1">
                <div class="status-circle ms-1 me-1" style="background-color:#FFF500"></div>
              </div>
              <div class="col-9 ms-2">Waiting</div>
            </div>
          </div>
          <div class="col-3" style="width: 100%; line-height:25px">
            <div class="row">
              <div class="col-2 me-1">
                <div class="status-circle ms-1 me-1" style="background-color:#50D1AA"></div>
              </div>
              <div class="col-9 ms-2">Active</div>
            </div>
          </div>
          <div class="col-3" style="width: 100%; line-height:25px">
            <div class="row">
              <div class="col-2 me-1">
                <div class="status-circle ms-1 me-1" style="background-color:#FF7CA3"></div>
              </div>
              <div class="col-9 ms-2">Inactive</div>
            </div>
          </div>
          <div class="col-3" style="width: 120%; line-height:25px">
            <div class="row">
              <div class="col-2 me-1">
                <div class="status-circle ms-1 me-1" style="background-color:#65B0F6"></div>
              </div>
              <div class="col-9 ms-2">Banned</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavApp from "../../components/main_component/NavApp.vue";
import SearchBar from "../../components/materials/SearchBar.vue";
export default {
  components: { NavApp, SearchBar },
  data(){
    return{
      
    }
  }
};
</script>

<style>
</style>