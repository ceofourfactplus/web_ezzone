<template>
  <div>
    <nav-app @back="back">Add Raw Material</nav-app>
    <div class="row">
      <div style="width: 1%"></div>
      <div class="col-9 wrap-search">
        <input
          type="text"
          class="search-bar"
          placeholder="Search for Raw Material"
          v-model="texts"
        />
        <img class="img-float" src="../../assets/icon/Search-19x18-1.png" />
      </div>
      <div style="padding-left: 0px">
        <button class="btn-ghost" @click="add">Confirm Add</button>
      </div>
    </div>
    <div class="table">
      <div class="table-header" style="width: 648px">
        <div class="row">
          <div class="col-8" style="margin-left: 70px; font-size: 24px">
            Items
          </div>
          <div
            class="item-in-head-table"
            style="width: 100px; font-size: 24px; padding-top: 3px; margin-top: 5px;"
          >
            + Qty
          </div>
          <div
            class="item-in-head-table"
            style="font-size: 24px; width: 87px; height: 41px; padding-top: 3px; margin-top: 5px;"
          >
            Unit
          </div>
          <div class="item-in-head-table pu">Price <br />/Unit</div>
          <div
            class="item-in-head-table"
            style="
              width: 103px;
              height: 41px;
              padding-left: 0px;
              margin-left: 5px;
              margin-right: 15px;
              margin-top: 5px;
            "
          >
            Total Price
          </div>
        </div>
      </div>
      <div style="height: 720px; overflow-y: scroll; overflow-x: hidden;">
        <div class="table-item" v-for="(item, idx) in raw_material_data" :key="idx">
        <div class="checkbox-orange">
          <div class="row">
            <input
              type="checkbox"
              class="me-3 mt-2"
              v-model="list_vals"
              :value="item"
              id="Female"
              style="left: 25px; bottom: 3px"
            />
            <div class="col-4">
              <div class="item-in-table-row">{{ item.item }}</div>
            </div>
            <div class="col-1">
              <div 
                class="qty" 
                style="margin-left: 30px"
              >
              <input type="text" class="inp-qty" v-model="item.qty" @input="calc(item)">
            </div>
            </div>
            <div class="col-1">
              <div class="unit">
                <select style="background-color: #2f3446; color: white; border-radius: 10px;" v-model="item.unit">
                  <option
                    v-for="unit in units"
                    :value="unit.unit"
                    :key="unit.value"
                  >
                    {{ unit.unit }}
                  </option>
                </select>
              </div>
            </div>
            <div class="price-unit"><input type="text" class="inp-qty" v-model="item.price_unit" @input="calc(item)"></div>
            <div class="col-1 total-price"><input type="text" class="inp-qty" v-model="item.total_price" @input="calc_discount(item)"></div>
          </div>
        </div>
      </div>
      </div>
    </div>
  </div>
</template>

<script>
import NavApp from "../../components/main_component/NavApp.vue";
// import api_raw_material from "../../api/api_raw_material"

export default {
  components: {
    NavApp,
  },
  // mounted() {

  // },
  data() {
    return {
      category_name: "",
      cb_in_table: "",
      discount: 0,
      list_vals: [],
      units: [
        { unit: "ชิ้น", value: "a" },
        { unit: "กล่อง", value: "b" },
        { unit: "แพ็ค", value: "c" },
        { unit: "ถุง", value: "d" },
        { unit: "ลัง", value: "e" },
      ],
      raw_material_data: [
        { item: "item1", qty: 9999, unit: 'ชิ้น', price_unit: 999, total_price: 0, discount: 0,},
        { item: "item2", qty: 9999, unit: 'กล่อง', price_unit: 999, total_price: 0, discount: 0,},
        { item: "item3", qty: 9999, unit: 'แพ็ค', price_unit: 999, total_price: 0, discount: 0,},
        { item: "item4", qty: 9999, unit: 'ถุง', price_unit: 999, total_price: 0, discount: 0,},
        { item: "item5", qty: 9999, unit: 'ลัง', price_unit: 999, total_price: 0, discount: 0,},
      ],
      test_count: 5,
    };
  },
  methods: {
    add() {
      console.log('add')
      this.test_count += 1
      this.raw_material_data.push({ item: `item${this.test_count}`, qty: 9999, unit: 'ลัง', price_unit: 999, total_price: 9999 },)
    },
    calc(item) {
      var idx = this.raw_material_data.indexOf(item)
      var sum = parseInt(item.qty) * parseInt(item.price_unit)
      this.raw_material_data[idx].total_price = sum
      this.raw_material_data[idx].discount = sum - this.raw_material_data[idx].total_price
    },
    calc_discount(item) {
      var idx = this.raw_material_data.indexOf(item)
      var sum = parseInt(item.qty) * parseInt(item.price_unit)
      this.raw_material_data[idx].discount = sum - this.raw_material_data[idx].total_price
      console.log(this.raw_material_data[idx].discount)
    },
<<<<<<< HEAD
    create_raw_material() {
      // data = [
      //       'id',
      //       'name',
      //       'balance',
      //       'category_id',
      //       'unit_id',
      //       'create_by_id',
      // ]
      // api_raw_material.post('create-raw-material/', data).then(response => {
      //   console.log('created')
      // })
    }
=======
    // create_raw_material() {
    //   data = [
    //         'id',
    //         'name',
    //         'balance',
    //         'category_id',
    //         'unit_id',
    //         'create_by_id',
    //   ]
    //   api_raw_material.post('create-raw-material/', data).then(response => {
    //     console.log('created')
    //   })
    // },
>>>>>>> 0d45cc076cd38aaef05830e54fcab531634d56c5
    // createCategory() {
    //   const data = {'name': this.category_name}
    //   api_raw_material.post('create_category/', data).then(response => {
    //     console.log(response.data)
    //   })
    // },
  },
};
</script>

<style scoped>
input.inp-qty {
  width: 100%;
  height: 45px;
  background-color: #bd523f;
}
.total-price,
.price-unit,
.qty {
  font-size: 24px;
  /* background-color: #889898; */
}
.qty {
  width: 75px;
  height: 35px;
  left: 0px;
  top: 5px;
}
.unit {
  width: 94px;
  height: 45px;
  left: 385px;
}
.price-unit {
  width: 75px;
  height: 35px;
  left: -1px;
  top: 5px;
}
.total-price {
  width: 83px;
  height: 35px;
  text-align: center;
  margin-right: 0px;
  right: 2px;
  padding-left: 0px;
  padding-right: 0px;
}
.item-in-table-row {
  width: 10px;
}
.pu {
  padding-right: 0px;
  margin-top: 0px;
  margin: 0px;
  padding-top: 0px;
  position: relative;
  width: 70px;
  height: 41px;
}
.img-float {
  width: 43px;
  left: 48px;
  top: 9.5%;
  position: fixed;
}
.table {
  margin-top: 10px;
}
.item-in-head-table {
  font-size: 18px;
  margin-top: 0px;
}
.head-item {
  display: inline;
  width: 100px;
  padding-left: 30px;
}
.table-add-rm {
  color: white;
  width: 676px;
  height: 45px;
  font-size: 24px;
  border-radius: 200px;
  border: none;
  margin-left: 20px;
  border-collapse: separate;
  border-spacing: 0 10px;
}
.parent-tr {
  background-color: #bd523f;
  border: none;
}
.child-tr {
  margin-top: 10px;
  border: none;
}
th {
  border: none;
}
.table-item {
  height: 60px;
  margin-top: 20px;
  background-color: #2f3446;
  border: none;
  font-weight: 500;
}
.table-header {
  font-weight: 500;
}

.btn-ghost {
  border-color: #65b0f6;
  color: #65b0f6;
  width: 242px;
  height: 45px;
  margin-left: 0px;
}
.wrap-search {
  min-width: 424px;
  width: fit-content;
  padding: 0px;
  margin-left: 0px;
}
.search-bar {
  text-indent: 65px;
  border-radius: 20px;
  height: 45px;
  background-color: #3E4444;
}
</style>