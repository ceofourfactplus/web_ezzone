<template>
  <div>
    <!-- Table -->
    <div class="table" style="margin-top: 10px">
      <div class="table-header">
        <!-- Is Staff -->
        <div v-if="is_staff" class="row" style="padding-right: 80px">
          <div class="col-4" style="margin-left: 200px">{{ head1 }}</div>
          <div class="col-2" style="padding-left: 10px">{{ head2 }}</div>
          <div class="col-2" style="padding-left: 20px">{{ head3 }}</div>
          <div class="col-2">{{ head4 }}</div>
        </div>
        <!-- Is Raw Material -->
        <div
          v-else-if="category == 'raw_material'"
          class="row"
          style="padding-right: 0px"
        >
          <div class="col-6 w-100" style="white-space: nowrap">
            {{ head1 }}
          </div>
          <div class="col-2 w-100">
            {{ head2 }}
          </div>
          <div class="col-2 w-100">
            {{ head3 }}
          </div>
          <div class="col-1 w-100">
            {{ head4 }}
          </div>
          <div class="col-1 w-100" style="margin-right: 20px">
            {{ head5 }}
          </div>
        </div>

        <!-- Is PO Notice -->
        <div
          v-else-if="category == 'po_notice'"
          class="row"
          style="padding-right: 0px"
        >
          <div
            class="col-4 w-100"
            style="margin-left: ; text-align: right; margin-left: 50px"
          >
            {{ head1 }}
          </div>
          <div class="col-1 w-100" style="margin-left: 100px">
            {{ head2 }}
          </div>
          <div class="col-2 w-100" style="margin-left: 50px">
            {{ head3 }}
          </div>
          <div class="col-4 w-100" style="margin-left: 25px">
            {{ head4 }}
          </div>
          <div class="col-1 w-100" style="margin-right: 30px">
            {{ head5 }}
          </div>
        </div>

        <!-- Is Consignment -->
        <div
          v-else-if="category == 'Consignment'"
          class="row"
          style="padding-right: 0px"
        >
          <div class="col-6" style="margin-left: 90px">{{ head1 }}</div>
          <div class="col-1" style="margin-left: 220px">{{ head2 }}</div>
          <div class="col-1" style="margin-left: -5px">{{ head3 }}</div>
          <div class="col-1" style="margin-left: -5px">{{ head4 }}</div>
          <div class="col-1" style="margin-left: 0px">{{ head5 }}</div>
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
            <div
              class="col-6"
              style="text-align: left; width: 100%; white-space: nowrap"
            >
              {{ item.name }}
            </div>
            <div class="col-2">{{ item.qty }}</div>
            <div class="col-2">{{ item.unit }}</div>
            <div class="col-1" v-if="status != 'category'">
              <img
                :src="$store.state.raw_material.status_image[item.status]"
                alt="img"
              />
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
        <div v-else-if="category == 'po_notice'">
          <div
            class="row table-item ps-0"
            v-for="(item, idx) in elements"
            :key="idx"
            style="
              padding-right: 0px;
              background-color: #303344;
              border-radius: 10px;
              margin: 0px;
              margin-top: 5px;
              line-height: 20px;
            "
          >
            <div class="col-1">
              <div
                class="checkbox-orange"
                style="position: relative; bottom: 6px"
              >
                <input
                  type="checkbox"
                  class="me-3 mt-2"
                  :value="item"
                  @input="$emit('selected_items', item)"
                />
              </div>
            </div>
            <div
              class="col-4 w-100"
              @click="po_detail(item)"
              style="
                text-align: left;
                font-size: 24px;
                overflow-x: auto;
                white-space: nowrap;
              "
            >
              {{ item.raw_material_set.name }}
            </div>
            <div
              class="col-1 w-100"
              @click="po_detail(item)"
              style="text-align: right"
            >
              {{ item.raw_material_set.remain }}
            </div>
            <div class="col-2 w-100" @click="po_detail(item)">
              <p>{{ item.unit_set.unit }}</p>
            </div>
            <div
              class="col-3 w-100"
              style="text-align: left; overflow-x: auto; white-space: nowrap;"
              @click="po_detail(item)"
            >
              {{ item.supplier_set.company_name }}
            </div>
            <div class="col-1" @click="po_detail(item)">
              <img
                style="
                  margin-right: 5px;
                  position: relative;
                  bottom: 3px;
                  height: 30px;
                  width: 30px;
                "
                :src="
                  $store.state.raw_material.status_image[
                    item.raw_material_set.status
                  ]['img']
                "
                alt="img"
              />
            </div>
          </div>
        </div>
        <div v-else-if="category == 'raw_material'">
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
              line-height: 25px;
            "
          >
            <div
              class="col-6 w-100"
              @click="showRmDetial(item)"
              style="text-align: left; white-space: nowrap"
            >
              {{ item.name }}
            </div>
            <div
              class="col-2 w-100"
              @click="showRmDetial(item)"
              style="margin-left: 7px"
            >
              {{ item.remain }}
            </div>
            <div
              class="col-2 w-100"
              @click="showRmDetial(item)"
              style="margin-left: 15px"
            >
              {{ item.unit_set.unit }}
            </div>
            <!-- <div class="col-2 w-100" style="margin-left: 15px;">
              100
            </div> -->
            <div
              class="col-1 w-100"
              @click="showRmDetial(item)"
              style="margin-right: 70px"
            >
              <img
                :src="
                  $store.state.raw_material.status_image[item.status]['img']
                "
                style="
                  position: relative;
                  bottom: 3px;
                  transform: rotate(180deg);
                "
                :style="
                  $store.state.raw_material.status_image[item.status]['style']
                "
                alt="img"
              />
            </div>
            <div
              class="col-1 w-100"
              @click="show_pickup(item)"
              style="margin-right: 20px"
            >
              <img
                style="
                  width: 32px;
                  height: 30px;
                  position: relative;
                  bottom: 3px;
                "
                src="../../assets/icon/pickup.png"
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
            <div
              class="col-6"
              style="
                text-align: left;
                width: 100%;
                font-size: 24px;
                white-space: nowrap;
              "
            >
              {{ item.name }}
            </div>
            <div class="col-1" style="margin-right: -140px">{{ item.qty }}</div>
            <div class="col-1" style="margin-right: -10px">{{ item.unit }}</div>
            <div class="col-1"><p style="margin-right: -100px">Someone</p></div>
            <div class="col-1">
              <img
                style="margin-right: -200px"
                :src="$store.state.raw_material.status_image[item.status]"
                alt="img"
              />
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
              <img
                :src="$store.state.raw_material.status_image[item.status]"
                alt="img"
              />
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
  props: [
    "head1",
    "head2",
    "head3",
    "head4",
    "head5",
    "elements",
    "is_staff",
    "status",
    "category",
  ],
  mounted() {},
  data() {
    return {
      selected_items: [],
    };
  },
  methods: {
    po_detail(item) {
      this.$emit("po_detail", item);
    },
    show_pickup(item) {
      this.$emit("show_pickup", item);
    },
    showRmDetial(item) {
      this.$emit("show_rm_detail", item);
    },
    min_sup() {
      return "true";
    },
    status_img(status) {
      if (status == 2) {
        return require("../../assets/icon/warning.png");
      } else {
      }
    },
  },
};
</script>

<style scoped>
</style>