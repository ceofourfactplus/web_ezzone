<template>
  <div>
    <!-- nav bar -->
    <nav-app>Purches&#160;Order</nav-app>
    <div class="row" style="width: 90%; margin-left: 25px">
      <div class="col-8 wrap-search w-100">
        <SearchBar @search="search_raw" style="width: 98%" />
      </div>
      <div class="col-2 w-100" style="padding-left: 0px">
        <button
          class="btn-ghost-b"
          style="width: 100%; height: 50px"
          @click="add_po = true"
        >
          +&#160;PO
        </button>
      </div>
      <div class="col-2 w-100" style="padding-left: 0px; text-align: left">
        <button
          class="btn-ghost-b"
          style="width: 120px; height: 50px"
          @click="ConvertPOToReceptData"
        >
          Confirm
        </button>
      </div>
    </div>

    <!-- table -->
    <div class="table mt-3" style="height:100%">
      <div class="table-header" style="line-height: 40px; font-size: 24px">
        <div class="row">
          <div class="col-8 w-100">Item</div>
          <div class="col-1 w-100">Qty.</div>
          <div class="col-1 w-100">Unit</div>
          <div class="col-2 w-100">Price</div>
        </div>
      </div>
      <div style="overflow-x: auto; height: 650px">
        <div v-for="recept in all_recept" :key="recept">
          <div class="table-item">
            <div class="row" style="width: 100%; margin-left: 0px;text-align:center;">
              <div class="col-1 w-100">
                <div class="checkbox-orange">
                  <input type="checkbox" />
                </div>
              </div>
              <div class="col-2 w-100">
                {{ recept.supplier.company_name }}
              </div>
              <div class="col-5 w-100"></div>
              <div class="col-4 w-100">
                <pre>Total  {{ recept.total_price }}</pre>
              </div>
            </div>
          </div>
          <div
            v-for="item in recept.recept_detail"
            :key="item.id"
            class="table-item"
          >
            <div class="row" style="width: 100%; margin-left: 0px">
              <div
                class="col-8 w-100"
                style="margin-left: 75px; text-align: left"
              >
                <span>
                  <div class="checkbox-orange">
                    <input
                      type="checkbox"
                      :id="item.raw_material_set.name"
                      style="display: inline-block"
                      class="ms-2"
                    />
                    <label :for="item.raw_material_set.name" class="ms-3">
                      {{ item.raw_material_set.name }}</label
                    >
                  </div>
                </span>
              </div>
              <div class="col-1 w-100" style="margin: auto; text-align: left">
                {{ item.amount }}
              </div>
              <div class="col-1 w-100" style="margin: auto; text-align: center">
                {{ item.unit_set.unit }}
              </div>
              <div
                class="col-2 w-100"
                style="margin: auto; text-align: center; padding: 0px"
              >
                {{ item.last_price }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- add OP -->
    <div class="blur" v-if="add_po">
      <div
        class="card"
        :class="{ 'card-active': add_po }"
        style="background-color: #252836"
      >
        <!-- nav popup -->
        <div class="row mt-3">
          <div class="col-2 w-100">
            <img src="../../assets/icon/save.png" alt="" @click="create_po()" />
          </div>
          <div class="col-8 w-100">
            <h2 style="color: #fff; font-size: 36px">PO Item</h2>
          </div>
          <div class="col-2 w-100">
            <img
              src="../../assets/icon/delete.png"
              @click="add_po = false"
              alt=""
            />
          </div>
        </div>

        <div class="frame f-1">
          <div class="row">
            <label for="name"><pre>Name       :</pre></label>
            <input
              class="g-s"
              id="name"
              type="text"
              style="width: 270px"
              v-model="raw_material"
            />
            <select v-model="raw_material" class="g-e" style="width: 30px">
              <option
                v-for="item in all_raw_material"
                :key="item.id"
                :value="item.name"
              >
                {{ item.name }}
              </option>
            </select>
          </div>
          <div class="row">
            <label for="name"><pre>supplier   :</pre></label
            ><input
              id="name"
              class="g-s"
              type="text"
              v-model="supplier"
              style="width: 270px"
            /><select v-model="supplier" class="g-e" style="width: 30px">
              <option
                v-for="sup in all_supplier"
                :key="sup.id"
                :value="sup.company_name"
              >
                {{ sup.company_name }}
              </option>
            </select>
          </div>
        </div>
        <div class="frame f-2">
          <div class="row">
            <label for="name">
              <pre>Qty        :</pre>
            </label>
            <input
              id="name"
              v-model="amount"
              type="number"
              style="text-align: right"
            />
            <input
              type="text"
              style="width: 110px; margin-left: 10px"
              class="g-s"
              v-model="unit"
            />
            <select style="width: 30px" v-model="unit" class="g-e">
              <option
                v-for="unit in all_unit"
                :key="unit.id"
                :value="unit.unit"
              >
                {{ unit.unit }}
              </option>
            </select>
          </div>
          <div class="row">
            <label for="name"><pre>Price      :</pre></label
            ><input
              id="name"
              v-model="price"
              type="text"
              style="text-align: right"
            /><label for="total_cost">
              <pre>บาท</pre>
            </label>
          </div>
          <div class="row">
            <label for="name"><pre>Discount   :</pre></label
            ><input
              id="name"
              type="text"
              style="text-align: right"
              v-model="discount"
            /><label for="total_cost">
              <pre><span @click="discount_choice = 0" :class="{'discount-active':discount_choice==0}">บาท</span>/<span @click="discount_choice = 1" :class="{'discount-active':discount_choice==1}">%</span></pre>
            </label>
          </div>
          <div class="row">
            <label for="name">
              <pre>Total Cost :    {{ cal_total_cost }} บาท</pre>
            </label>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { api_raw_material } from "../../api/api_raw_material";
import SearchBar from "../../components/materials/SearchBar.vue";
import NavApp from "../../components/main_component/NavApp.vue";
import Table from "../../components/main_component/Table.vue";
import CheckBoxWhite from "../../components/main_component/CheckBoxWhite.vue";

export default {
  components: {
    SearchBar,
    NavApp,
    Table,
    CheckBoxWhite,
  },
  mounted() {
    this.get_raw();
    this.get_po();
    this.get_sup();
    api_raw_material.get("unit").then((response) => {
      this.all_unit = response.data;
    });
    api_raw_material.get("raw-material/").then((response) => {
      this.all_raw_material = response.data;
    });
  },

  data() {
    return {
      filter_by: 1,
      add_po: false,
      supplier: "",
      raw_material: "",
      unit: "",
      total_cost: 0,
      all_raw_material: [],
      all_unit: [],
      discount_choice: 0,
      all_supplier: [],
      price: 0,
      amount: 0,
      discount: 0,
      new_po_id: null,
      po: [],
      all_recept: [],
    };
  },
  methods: {
    get_raw() {
      api_raw_material.get("raw-material/").then((response) => {
        this.raw_materials = response.data;
        this.temp_rm = response.data;
      });
    },
    get_sup() {
      api_raw_material.get("supplier").then((response) => {
        this.all_supplier = response.data;
      });
    },
    // get_min_sup(item) {
    //   api_raw_material.get("get-min-supplier/"+item.).then((response) => {
    //     return response.data.supplier;
    //   });
    // },
    get_po() {
      api_raw_material.get("po/").then((response) => {
        this.po = response.data;
      });
    },
    get_status(status) {
      if (status == 2) {
        return require("../../assets/icon/warning.png");
      }
      if (status == 3) {
        return require("../../assets/icon/incorrect.png");
      }
    },
    search_raw(query) {
      console.log(query);
    },
    create_po() {
      const data = {
        raw_material: this.raw_material,
        supplier: this.supplier,
        amount: this.amount,
        unit: this.unit,
        last_price: this.price,
        create_by_id: 1,
      };
      api_raw_material.post("po/cal-add", data).then((response) => {
        console.log(response.data);
        this.new_po_id = response.data.id;
        this.get_po;
      });
    },
    ConvertPOToReceptData() {
      console.log(this.po);
      const only_supplier = [
        ...new Map(this.po.map((item) => [item["supplier_id"], item])).values(),
      ];
      const all_recept = [];
      for (const supplier of only_supplier) {
        const recept = {
          recept_detail: [],
          total_price: 0,
          supplier: supplier.supplier_set,
        };
        for (const item of this.po) {
          if (item.supplier_id == supplier.supplier_id) {
            const data = {
              po_id: item.id,
              supplier_id: item.supplier_id,
              price: item.price,
              raw_material_id: item.raw_material_id,
              unit_id: item.unit,
              dicount: 0,
              is_percent: false,
              amount: item.amount,
              total_price: item.amount * item.last_price,
              price: item.last_price,
              supplier_set: item.supplier_set,
              raw_material_set: item.raw_material_set,
              unit_set: item.unit_set,
            };
            recept.recept_detail.push(JSON.parse(JSON.stringify(data)));
            recept.total_price += item.amount * item.last_price;
          }
        }
        all_recept.push(JSON.parse(JSON.stringify(recept)));
      }
      this.all_recept = all_recept;
    },
  },
  computed: {
    cal_total_cost() {
      if (this.discount_choice == 0) {
        this.total_cost = this.amount * this.price - this.discount;
      }
      if (this.discount_choice == 1) {
        if (this.discount >= 100) {
          this.discount = 100;
        }
        this.total_cost =
          (this.amount * this.price * (100 - this.discount)) / 100;
      }
      return this.total_cost;
    },
  },
};
</script>

<style scoped>
.card {
  width: 600px;
  height: 498px;
  top: 200px;
  border-radius: 24px;
  left: 10%;
}
.frame {
  border-radius: 24px;
}
.discount-active {
  background-color: #fff;
  color: black;
  border-radius: 5px;
}

input,
select {
  text-indent: 0px;
  background-color: #e0eeee88;
  width: 150px;
  height: 40px;
}

.g-s {
  border-radius: 10px 0px 0px 10px;
}
.g-e {
  border-radius: 0px 10px 10px 0px;
}

.f-1 {
  height: 134px;
  width: 90%;
  margin-left: auto;
  margin-right: auto;
}
.f-2 {
  height: 242px;
  width: 90%;
  margin-left: auto;
  margin-right: auto;
}
.a{
  justify-content: center;
}
</style>