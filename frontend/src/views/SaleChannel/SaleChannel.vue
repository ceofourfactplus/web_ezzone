<template>
  <div>
    <nav-app>Sale&#160;Channel</nav-app>
    <div class="row" style="width: 90%; margin: auto">
      <div class="col-7 w-100" style="padding: 0px">
        <search-bar @search="search" style="width: 100%" />
      </div>
      <div
        class="col-5 w-100"
        style="padding-right:0px;padding-left:12px;margin:auto; justify-content: space-between; display: flex"
      >
        <button
          class="btn-ghost-b"
          style="width: 125px; height: 50px"
          @click="$router.push({ name: 'CreateCustomer' })"
        >
          +&#160;New</button
        ><button
          class="btn-ghost-r"
          style="width: 125px; height: 50px"
          @click="$router.push({ name: 'CreateCustomer' })"
        >
          <img src="../../assets/icon/bin.png" width="20" alt="">&#160;Delete
        </button>
      </div>
    </div>

    <div class="table mt-3">
      <div class="table-header" style="line-height: 40px; font-size: 24px">
        <div class="row">
          <div class="col-3 w-100" style="margin: auto">Name</div>
          <div class="col-3 w-100" style="margin-left: 10px; text-align: left">
            Create&#160;at
          </div>
          <div class="col-2 w-100" style="margin: auto; margin-left: -10px">
            Qty
          </div>
          <div class="col-3 w-100" style="margin: auto">Status</div>
        </div>
      </div>
      <div style="overflow-x: auto; height: 650px">
        <div
          v-for="customer in all_customer"
          :key="customer.id"
          class="table-item"
        >
          <div class="row" style="width: 100%">
            <div
              class="col-3 w-100"
              style="margin: auto; margin-left: 0px; text-align: left"
              @click="SeeData(customer.id)"
            >
              <span>
                <img
                  v-if="customer.img != null"
                  :src="customer.img"
                  class="img-user-status me-1"
                /><img
                  v-else
                  src="../../assets/icon/blank-user.png"
                  class="img-user-status me-1"
                />
                {{ customer.nick_name }}
              </span>
            </div>
            <div class="col-3 w-100" style="margin: auto; text-align: left">
              {{ BirthDate(customer.birth_date) }}
            </div>
            <div
              class="col-3 w-100"
              style="margin: auto; width: 175px; text-align: left"
            >
              {{ PhoneNumber(customer.phone_number) }}
            </div>
            <div
              class="col-3 w-100"
              style="margin: auto; text-align: left; padding: 0px"
            >
              {{ BirthDate(customer.birth_date) }}
              <img
                @click="select(customer)"
                src="../../assets/icon/home.png"
                style="float: right"
              />
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
};
</script>

<style>
</style>