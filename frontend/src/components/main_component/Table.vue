<template>
  <div>
    <!-- Table -->
    <div class="table" style="margin-top: 10px">
      <div class="table-header">
        <!-- Is Staff -->
        <div v-if="is_staff" class="row" style="padding-right: 80px">
          <div class="col-6" style="margin-left: 90px">{{ head1 }}</div>
          <div class="col-2" style="padding-left: 10px">{{ head2 }}</div>
          <div class="col-2" style="padding-left: 20px">{{ head3 }}</div>
          <div class="col-2">{{ head4 }}</div>
        </div>
        <!-- Is Consignment -->
        <div v-else-if="category == 'Consignment'" class="row" style="padding-right: 0px">
          <div class="col-6" style="margin-left: 90px">{{ head1 }}</div>
          <div class="col-1" style="margin-left: 220px;">{{ head2 }}</div>
          <div class="col-1" style="margin-left: -5px;">{{ head3 }}</div>
          <div class="col-1" style="margin-left: -5px;">{{ head4 }}</div>
          <div class="col-1" style="margin-left: 0px;">{{ head5 }}</div>
        </div>
        <!-- Is User -->
        <div v-else class="row" style="padding-right: 10px">
          <div class="col-6" style="margin-left: 90px">{{ head1 }}</div>
          <div class="col-2">{{ head2 }}</div>
          <div class="col-2">{{ head3 }}</div>
          <div class="col-2">{{ head4 }}</div>
        </div>
      </div>
      <div
        style="
          height: 660px;
          overflow-y: scroll;
          overflow-x: hidden;
          border-radius: 10px;
        "
      >
        <div v-if="is_staff">
          <div
            class="row table-item"
            v-for="(item, idx) in elements"
            :key="idx"
            style="
              padding-right: 0px;
              margin: 5px 0px 0px 0px;
              margin: 0px;
              background-color: #303344;
              border-radius: 10px;
            "
          >
            <div class="col-6" style="text-align: left; width: 100%">
              {{ item.name }}
            </div>
            <div class="col-2">{{ item.qty }}</div>
            <div class="col-2">{{ item.unit }}</div>
            <div class="col-1" v-if="status != 'category'">
              <img :src="$store.state.raw_material.status_image[item.status]" alt="img" />
            </div>
            <div class="col-1">
              <img
                @click="edit(item)"
                src="../../assets/icon/edit.png"
                alt="img"
              />
            </div>
          </div>
        </div>

        <div v-else-if="category == 'Consignment'">
          <div
            class="row table-item"
            v-for="(item, idx) in elements"
            :key="idx"
            style="
              padding-right: 0px;
              background-color: #303344;
              border-radius: 10px;
              margin: 0px;
              margin-top: 5px;
            "
          >
            <div class="col-6" style="text-align: left; width: 100%; font-size: 24px;">
              {{ item.name }}
            </div>
            <div class="col-1" style="margin-right: -140px;">{{ item.qty }}</div>
            <div class="col-1" style="margin-right: -10px;">{{ item.unit }}</div>
            <div class="col-1"><p style="margin-right: -100px;">Someone</p></div>
            <div class="col-1">
              <img style="margin-right: -200px;" :src="$store.state.raw_material.status_image[item.status]" alt="img" />
            </div>
          </div>
        </div>

        <div v-else>
          <div
            class="row table-item"
            v-for="(item, idx) in elements"
            :key="idx"
            style="
              padding-right: 0px;
              background-color: #303344;
              border-radius: 10px;
              margin: 0px;
              margin-top: 5px;
            "
          >
            <div class="col-6" style="text-align: left; width: 100%">
              {{ item.name }}
            </div>
            <div class="col-2">{{ item.qty }}</div>
            <div class="col-2">{{ item.unit }}</div>
            <div class="col-2" style="margin-left: 30px">
              <img :src="$store.state.raw_material.status_image[item.status]" alt="img" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import api_raw_material from "../../api/api_raw_material"

export default {
  components: {},
  props: ["head1", "head2", "head3", "head4", "head5", "elements", "is_staff", "status", "category"],
  mounted() {
  },
  data() {
    return {
        
    };
  },
  methods: {},
};
</script>

<style scoped>
</style>