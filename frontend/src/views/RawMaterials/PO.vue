<template>
  <div>
    <!-- nav bar -->
    <nav-app :url_name="'RawMaterials'" :rm_menu="true">Purchase&#160;Order</nav-app>
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
      <div class="col-2 w-100">
        <button
          @click="confirm"
          class="btn-ghost-b"
          style="width: 120px; height: 50px;padding-left: 16%; text-align: left;"
        >
          Confirm
        </button>
      </div>
    </div>

    <!-- table -->
    <div class="table mt-3" style="height: 100%">
      <div class="table-header" style="height:45px;line-height: 40px; font-size: 24px;padding-left: 8px;padding-right: 8px;">
        <!-- Table Head -->
        <div class="row" style="line-height:100%">
          <div class="col-1 w-100">
            <div class="checkbox-white">
              <input
                type="checkbox"
                :value="true"
                style="left: 15px;"
                @input="selectAllItem"
              />
            </div>
          </div>
          <div class="col-7 w-100">Item</div>
          <div class="col-1 w-100">Qty.</div>
          <div class="col-1 w-100" style="right:-10px;position:relative;">Unit</div>
          <div class="col-2 w-100" style="right:-10px;position:relative;">Price</div>
        </div>
      </div>
      <div style="overflow-x: auto; height: 650px">
        <div v-for="recept in all_recept" :key="recept">
          <!-- Table Item Head -->
          <div class="table-item" style="height:45px;padding-top:0%; padding-bottom:0%;">
            <div
              class="row"
              style="
                width: 100%;
                margin-left: 0px;
                text-align: center;
                font-size: 28px;
                font-weight: bold;
                position: relative;
                line-height: 150%;
              "
            >
              <div class="col-1 w-100">
                <div class="checkbox-orange">
                  <input
                    type="checkbox"
                    style="margin-top: 8px; right: 0px"
                    :id="recept.supplier.company_name"
                    :value="recept.supplier.company_name"
                    @input="selectAllItemInSupplier(recept)"
                  />
                </div>
              </div>
              <div
                class="col-6 w-100"
                style="margin-top: -1px; text-align: left;"
              >
                <label :for="recept.supplier.company_name">
                  {{ recept.supplier.company_name }}</label
                >
              </div>
              <div class="col-1 w-100"></div>
              <div class="col-4 w-100">
                <p
                  style="font-size: 28px; font-weight: 800"
                >
Total  {{ recept.total_price }}</p
                >
              </div>
            </div>
          </div>
          <!-- Table Item -->
          <div
            v-for="item in recept.recept_detail"
            :key="item.id"
            class="table-item" style="height:45px;padding-top:0%; padding-bottom:0%;"
          >
            <div class="row" style="width: 100%; margin-left: 0px;position: relative; bottom: 9px;line-height:320%;">
              <div
                class="col-8 w-100"
              >
                <div class="row">
                  <div class="col-2 w-100"></div>
                  <div class="col-10 w-100" style="text-align: left;white-space:nowrap;overflow-x:auto;text-align: left">
                    <span>
                      <div class="checkbox-orange">
                        <input
                          type="checkbox"
                          :id="item.raw_material_set.name"
                          style="display: inline-block; top: 4px"
                          :value="item"
                          v-model="selected"
                          class="ms-2"
                        />
                        <label
                          :for="item.raw_material_set.name"
                          class="ms-3"
                          @click="showPoPopup(item)"
                        >
                          {{ item.raw_material_set.name }}
                        </label>
                      </div>
                    </span>
                  </div>
                </div>
              </div>
              <div
                class="col-1 w-100"
                style="margin: auto; text-align: center"
                @click="showPoPopup(item)"
              >
                {{ item.raw_material_set.must_buy }}
              </div>
              <div
                class="col-1 w-100"
                style="margin: auto; text-align: center; margin-right: -14px;"
                @click="showPoPopup(item)"
              >
                {{ item.unit_set.unit }}
              </div>
              <div
                class="col-2 w-100"
                style="
                  margin: auto;
                  text-align: center;
                  padding: 0px;
                  margin-left: 20px;
                "
                @click="showPoPopup(item)"
              >
                {{ item.last_price }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Save Popup -->
    <SavePopup :alert="alert" />
    <!-- add PO -->
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
              style="width: 30px;"
            />
          </div>
        </div>

        <div class="frame f-1">
          <div class="row">
            <div style="display: inline;">
                <div class="po-item-label">Name</div>
                <div style="margin-left: 96px;" class="po-item-label">:</div>
            </div>
            <input
              class="g-s"
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
          <div class="row" style="margin-top: 15px;">
            <div style="display: inline;">
                <div class="po-item-label">Supplier</div>
                <div style="margin-left: 69px;" class="po-item-label">:</div>
            </div>
            <input
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
              <div style="display: inline;">
                <div class="po-item-label">Qty</div>
                <div style="margin-left: 125px;" class="po-item-label">:</div>
              </div>
            <input
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
          <div class="row" style="margin-top: 15px;">
            <div style="display: inline;">
                <div class="po-item-label">Price</div>
                <div style="margin-left: 108px;" class="po-item-label">:</div>
            </div>
            <input
              v-model="price"
              type="text"
              style="text-align: right"
            />
            <label for="total_cost">
              <pre>บาท</pre>
            </label>
          </div>
          <div class="row">
            <div style="display: inline;">
                <div class="po-item-label">Discount</div>
                <div style="margin-left: 66px;" class="po-item-label">:</div>
            </div>
            <input
              id="name"
              type="text"
              style="text-align: right"
              v-model="discount"
            /><label for="total_cost">
              <pre><span @click="discount_choice = 0" :class="{'discount-active':discount_choice==0}">บาท</span>/<span @click="discount_choice = 1" :class="{'discount-active':discount_choice==1}">%</span></pre>
            </label>
          </div>
          <div class="row">
            <div style="width: 540px; text-align: left">
                <div class="po-item-label">Total Cost</div>
                <div class="po-item-label" style="margin-left: 52px;">:</div>
                <div class="po-item-label" style="margin-left: 15px;">{{ cal_total_cost }} บาท</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- PO Popup -->
    <div class="po-popup">
      <div class="blur" v-if="po_popup">
        <div
          class="card"
          :class="{ 'card-active': po_popup }"
          style="background-color: #252836; height: 690px"
        >
          <!-- Nav -->
          <div class="row w-100" style="height: 100px;margin:0px;line-height:600%;">
            <div class="col-2 w-100" @click="edit()">
              <img
                src="../../assets/icon/save.png"
                style="margin: 5px 0px 0px 10px"
              />
            </div>
            <div class="col-8 w-100 nav-txt" style="white-space:nowrap;overflow-x:auto;text-align: left">
              {{ po_popup_item.raw_material_set.name }}
            </div>
            <div class="col-2 w-100" @click="po_popup = false">
              <img
                src="../../assets/icon/delete.png"
                style="width: 29px; height: 32px; margin: 5px 0px 0px 0px"
              />
            </div>
          </div>
          <!-- Over Wrapper -->
          <div class="row" style="height:38%;">
            <!-- Image -->
            <div class="col-4 w-100">
              <img
                :src="
                  require(`../../../../backend${po_popup_item.raw_material_set.img}`)
                "
                class="image"
              />
            </div>
            <!-- Item Detail -->
            <div class="col-8 item-detail">
              <!-- Name --> 
              <div class="row">
                <div class="col-12 line-col" style="margin-top: 10px;white-space:nowrap;overflow-x:auto;width:300px;">
                  {{ po_popup_item.raw_material_set.name }}
                </div>
              </div>
              <!-- Category -->
              <div class="row">
                <div class="col-12 line-col">
                  Category&nbsp;:&nbsp;{{ category }}
                </div>
              </div>
              <!-- Status -->
              <div class="row">
                <div class="col-12 line-col">
                  Status&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;
                  <img style="margin-left: 10px;" :src="$store.state.raw_material.status_image[po_popup_item.raw_material_set.status]['img']" />
                </div>
              </div>
              <!-- Supplier -->
              <div class="row">
                <div class="col-12 line-col">
                  Supplier&nbsp;&nbsp;&nbsp;:&nbsp;
                  <select
                    style="height: 40px"
                    v-model="po_popup_item.supplier_id"
                  >
                    <option
                      style="background-color: black;"
                      v-for="supplier in all_supplier"
                      :key="supplier.id"
                      :value="supplier.id"
                    >
                      {{ supplier.company_name }}
                    </option>
                  </select>
                </div>
              </div>
            </div>
          </div>
          <!-- Under Wrapper -->
          <div class="row under-wrapper">
            <!-- Qty -->
            <div class="col-12 w-100 line-col" style="margin-left: 50px">
              Qty&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;
              <input
                type="text"
                class="under-wrapper-input"
                v-model="po_popup_item.raw_material_set.must_buy"
                @input="calc_total_price(po_popup_item)"
              />
              <select
                style="margin-left: 10px;"
                class="under-wrapper-input"
                v-model="po_popup_item.unit_set.id"
                @change="calc_price_unit(po_popup_item.unit_set.id)"
              >
                <option
                  style="background-color: black;"
                  v-for="unit in show_units"
                  :key="unit.id"
                  :value="unit.id"
                >
                  {{ unit.unit }}
                </option>
              </select>
            </div>
            <!-- Price -->
            <div class="col-12 w-100 line-col" style="margin-left: 50px">
              Price&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;
              <input
                type="text"
                class="under-wrapper-input"
                v-model="po_popup_item.last_price"
                @input="calc_total_price(po_popup_item)"
              />
              บาท
            </div>
            <!-- Discount -->
            <div class="col-12 w-100 line-col" style="margin-left: 50px">
              Discount&nbsp;&nbsp;&nbsp;:&nbsp;
              <input
                type="text"
                class="under-wrapper-input"
                v-model="po_popup_item.discount"
              />
              บาท/%
            </div>
            <!-- Total Cost -->
            <div class="col-12 w-100 line-col" style="margin-left: 50px">
              Total Cost&nbsp;:&nbsp;
              <input
                type="text"
                class="under-wrapper-input"
                :value="po_popup_item.raw_material_set.must_buy * po_popup_item.last_price"
              />
              บาท
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { api_raw_material } from "../../api/api_raw_material";
import SavePopup from "../../components/main_component/SavePopup.vue"
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
    SavePopup,
  },
  mounted() {
    api_raw_material.get("category").then((response) => {
      console.log(response.data, "categories");
      this.categories = response.data;
    });
    api_raw_material.get("unit").then((response) => {
      this.all_unit = response.data;
    });
    api_raw_material.get("raw-material/").then((response) => {
      this.all_raw_material = response.data;
    });
  },

  data() {
    return {
      new_img: false,
      filter_by: 1,
      po_popup: false,
      add_po: false,
      selected_status: false,
      select_all_status: false,
      supplier_id: null,
      temp_supplier_id: null,
      supplier: "",
      raw_material: "",
      unit: "",
      unit_id: "",
      category: "",
      total_cost: 0,
      dict_list: {},
      all_raw_material: [],
      all_unit: [],
      show_units: [],
      discount_choice: 0,
      all_supplier: [],
      price: 0,
      amount: 0,
      discount: 0,
      new_po_id: null,
      po_popup_item: {},
      po: [],
      all_recept: [],
      data: [],
      temp_all_recept: [],
      head_selected: [],
      selected: [],
      categories: [],
      all_dressert: false,
    };
  },
  methods: {
    selectAllItem() {
      this.select_all_status = !this.select_all_status;
      this.all_recept.forEach((recept) => {
        recept.recept_detail.forEach((element) => {
          if (this.select_all_status) {
            if (this.selected.indexOf(element) + 1 == 0) {
              this.selected.push(element);
            }
          } else {
            this.selected = [];
          }
        });
      });
    },
    selectAllItemInSupplier(recept) {
      console.log(recept, "recept");
      var not_have = false;
      var have_all = false;
      for (let index = 0; index < recept.recept_detail.length; index++) {
        if (this.selected.indexOf(recept.recept_detail[index]) + 1 == 0) {
          not_have = true;
        } else {
          not_have = false;
          break;
        }
      }
      if (not_have) {
        for (let index = 0; index < recept.recept_detail.length; index++) {
          this.selected.push(recept.recept_detail[index]);
        }
      } else {
        for (let index = 0; index < recept.recept_detail.length; index++) {
          if (this.selected.indexOf(recept.recept_detail[index]) + 1 != 0) {
            have_all = true;
          } else {
            have_all = false;
            break;
          }
        }
      }
      if (have_all) {
        for (let index = 0; index < recept.recept_detail.length; index++) {
          var idx = this.selected.indexOf(recept.recept_detail[index]);
          this.selected.splice(idx, 1);
        }
      } else {
        for (let index = 0; index < recept.recept_detail.length; index++) {
          if (this.selected.indexOf(recept.recept_detail[index]) + 1 == 0) {
            this.selected.push(recept.recept_detail[index]);
          }
        }
      }
    },
    get_raw() {
      api_raw_material.get("raw-material/").then((response) => {
        console.log(response.data, "raw_materials");
        this.raw_materials = response.data;
        this.temp_rm = response.data;
      });
    },
    get_sup() {
      api_raw_material.get("supplier").then((response) => {
        console.log(response.data, "all_supplier");
        this.all_supplier = response.data;
      });
    },
    calc_price_unit(unit_id){
      this.po_popup_item.raw_material_set.pricerawmaterial_set.forEach(prm => {
        if(prm.unit == unit_id) {
          this.po_popup_item.last_price = prm.last_price
        }
      })
    },
    // get_min_sup(item) {
    //   api_raw_material.get("get-min-supplier/"+item.).then((response) => {
    //     return response.data.supplier;
    //   });
    // },
    async get_po() {
      await api_raw_material.get("po/").then((response) => {
        this.po = response.data
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
      var temp = [];
      if (query == "") {
        this.all_recept = this.temp_all_recept;
      } else {
        this.temp_all_recept.forEach((element) => {
          console.log(element, "element");
          element.recept_detail.forEach((el) => {
            console.log(el, "el");
            if (el.raw_material_set.name.indexOf(query) + 1 != 0) {
              temp.push(element);
            }
          });
        });
        this.all_recept = temp;
      }
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
      console.log(this.po, "convert po");
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
            item.raw_material_set.must_buy = item.raw_material_set.maximum - item.raw_material_set.remain
            const data = {
              po_id: item.id,
              supplier_id: item.supplier_id,
              raw_material_id: item.raw_material_id,
              unit_id: item.unit,
              discount: 0,
              is_percent: false,
              amount: item.amount,
              total_price: item.amount * item.last_price,
              last_price: item.last_price,
              create_at: item.create_at,
              supplier_set: item.supplier_set,
              raw_material_set: item.raw_material_set,
              create_by_set: item.create_by_set,
              unit_set: item.unit_set,
            };
            recept.recept_detail.push(JSON.parse(JSON.stringify(data)));
            recept.total_price += item.amount * item.last_price;
          }
        }
        all_recept.push(JSON.parse(JSON.stringify(recept)));
      }
      this.all_recept = all_recept;
      this.temp_all_recept = all_recept;
    },
    showPoPopup(item) {
      this.show_units = []
      var temp_units = [item.raw_material_set.unit_l_id, item.raw_material_set.unit_m_id, item.raw_material_set.unit_s_id,]
      temp_units.forEach(unit_id => {
        this.all_unit.forEach((unit) => {
          if(unit_id == unit.id) {
            this.show_units.push(unit)
          }
        })
      })
      console.log(item, "item");
      this.supplier_id = item.supplier_id;
      this.temp_supplier_id = item.supplier_id;
      this.categories.forEach((el) => {
        if (el["id"] == item.raw_material_set.category_id) {
          this.category = el["name"];
        }
      });
      this.po_popup_item = item;
      this.po_popup = true;
    },
    async edit() {
      this.alert = true;
      setTimeout(() => {
        this.po_popup = false
        this.alert = false;
      }, 2000)
      api_raw_material.put("rm-update/", this.po_popup_item.raw_material_set).then((response) => {
        console.log(response.data)
      })
      // const data = new FormData();
      // data.append("id", this.po_popup_item.raw_material_set.id);
      // data.append("maximum", this.po_popup_item.raw_material_set.maximum);
      // data.append("minimum", this.po_popup_item.raw_material_set.minimum);
      // data.append("remain", this.po_popup_item.raw_material_set.remain);
      // data.append("category_id", this.po_popup_item.raw_material_set.category_id);
      // data.append("name", this.po_popup_item.raw_material_set.name);
      // data.append(
      //   "in_refrigerator",
      //   this.po_popup_item.raw_material_set.in_refrigerator
      // );
      // data.append("supplier_id", this.po_popup_item.supplier_id);
      // data.append("unit_l_id", this.po_popup_item.raw_material_set.unit_l_id);
      // data.append("unit_m_id", this.po_popup_item.raw_material_set.unit_m_id);
      // data.append("unit_s_id", this.po_popup_item.raw_material_set.unit_s_id);
      // data.append("m_to_l", this.po_popup_item.raw_material_set.m_to_l);
      // data.append("s_to_m", this.po_popup_item.raw_material_set.s_to_m);
      // data.append("avg_l", this.po_popup_item.raw_material_set.avg_l);
      // data.append("avg_m", this.po_popup_item.raw_material_set.avg_m);
      // data.append("avg_s", this.po_popup_item.raw_material_set.avg_s);
      // data.append("update_by_id", this.$store.state.auth.userInfo.id);
      // data.append("create_by_id", this.$store.state.auth.userInfo.id);
      // if (this.new_img) {
      //   user_data.append(
      //     "img",
      //     this.po_popup_item.raw_material_set.img,
      //     this.po_popup_item.raw_material_set.img.name
      //   );
      // }
      // await api_raw_material.put("rm-update/", data).then((response) => {
      //   console.log(response.data, "response data");
      // });
      // var po_data = {
      //   id: this.po_popup_item.po_id,
      //   amount: this.po_popup_item.amount,
      //   create_at: this.po_popup_item.create_at,
      //   create_by_id: this.po_popup_item.create_by_set.id,
      //   last_price: this.po_popup_item.last_price,
      //   raw_material_id: this.po_popup_item.raw_material_id,
      //   supplier_id: this.po_popup_item.supplier_id,
      //   unit_id: this.po_popup_item.unit_set.id,
      // }
      // api_raw_material.put("po/update/", po_data).then((response) => {
      //   console.log(response.data, 'po update')
      //   this.po_popup = false
      // })
    },
    change_supplier() {
      console.log(this.po_popup_item, this.temp_supplier_id, "po_popup_item");
      if (this.po_popup_item.supplier_id != this.temp_supplier_id) {
        console.log("come, in");
        for (let out = 0; out < this.all_recept.length; out++) {
          var recept = this.all_recept[out];
          console.log(recept, "recept");
          for (let index = 0; index < recept.recept_detail.length; index++) {
            if (
              recept.recept_detail[index].supplier_id ==
                this.po_popup_item.supplier_id &&
              recept.recept_detail[index].supplier_set.company_name !=
                this.po_popup_item.supplier_set.company_name
            ) {
              console.log("push");
              recept.recept_detail.push(this.po_popup_item);
              break;
            } else {
              console.log("remove");
              if (
                recept.recept_detail[index].raw_material_set.name ==
                this.po_popup_item.raw_material_set.name
              ) {
                var idx = recept.recept_detail.indexOf(this.po_popup_item);
                recept.recept_detail.splice(idx, 1);
              }
            }
          }
        }
      }
      this.po_popup = false

    },
    ConvertSlectedToReceptData() {
      console.log(this.po, "convert po");
      const only_supplier = [
        ...new Map(
          this.selected.map((item) => [item["supplier_id"], item])
        ).values(),
      ];
      const all_recept = [];
      for (const supplier of only_supplier) {
        const recept = {
          recept_detail: [],
          total_price: 0,
          supplier: supplier.supplier_set,
        };
        for (const item of this.selected) {
          if (item.supplier_id == supplier.supplier_id) {
            const data = {
              po_id: item.id,
              supplier_id: item.supplier_id,
              raw_material_id: item.raw_material_id,
              unit_id: item.unit,
              discount: 0,
              is_percent: false,
              amount: item.amount,
              total_price: item.amount * item.last_price,
              last_price: item.last_price,
              create_at: item.create_at,
              supplier_set: item.supplier_set,
              raw_material_set: item.raw_material_set,
              create_by_set: item.create_by_set,
              unit_set: item.unit_set,
            };
            recept.recept_detail.push(JSON.parse(JSON.stringify(data)));
            recept.total_price += item.amount * item.last_price;
          }
        }
        all_recept.push(JSON.parse(JSON.stringify(recept)));
      }
      this.data = all_recept;
      console.log(this.data, "data");
    },
    async confirm() {
      this.$store.state.raw_material.all_receipt = []
      await this.ConvertSlectedToReceptData();
      this.data.forEach((receipt) => {
        const receipt_raw_material = {
          supplier_id: receipt.supplier.id,
          total_price: receipt.total_price,
          total_amount: receipt.recept_detail.length,
          payment: null,
          create_by_id: this.$store.state.auth.userInfo.id,
          update_by_id: this.$store.state.auth.userInfo.id
        }
        this.$store.state.raw_material.all_receipt.push(receipt_raw_material)
        receipt.recept_detail.forEach((el) => {
          const receipt_raw_material_detail = {
            receipt_raw_material_id: null,
            raw_material_id: el.raw_material_set.id,
            supplier_id: el.supplier_id,
            price: el.last_price,
            total_price: el.total_price,
            amount: el.amount,
            remark: '',
            discount: el.discount,
            create_by_id: this.$store.state.auth.userInfo.id,
            update_by_id: this.$store.state.auth.userInfo.id
          }
          this.$store.state.raw_material.all_receipt_detail.push(receipt_raw_material_detail)
        }) });
      this.$store.state.raw_material.all_po_selected = this.data
      this.$router.push({ name: "ConfirmPO"})
    },
    calc_total_price(item) {
      console.log(item, "item in calc")
      this.all_recept.forEach((recept) => {
        if (recept.recept_detail.includes(item)) {
          var idx = recept.recept_detail.indexOf(item)
          recept.recept_detail[idx].raw_material_set.remain = item.raw_material_set.remain
          recept.recept_detail[idx].total_price = parseInt(item.raw_material_set.remain) * parseInt(item.last_price)
          console.log(recept.recept_detail[idx].total_price, 'data')
        }
      })
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
  async beforeMount() {
    await this.get_po();
    await this.ConvertPOToReceptData();
    this.get_raw();
    this.get_sup();
  },
};
</script>

<style scoped>
.po-item-label {
  display: inline; 
  font-size: 26px; 
  color: white;
}
.under-wrapper-unput {
  width: 150px;
  height: 40px;
  background: #717171;
  border-radius: 10px;
}
.under-wrapper {
  width: 575px;
  height: 292px;
  background: #303344;
  border-radius: 28px;
  font-size: 30px;
  color: white;
  margin: 15px 0px 0px 10px;
}
.line-col {
  text-align: left;
  margin: 10px 0px 0px 10px;
}
.item-detail {
  width: 340px;
  height: 251px;
  background: #303344;
  border-radius: 24px;
  color: white;
  margin-left: 50px;
  font-size: 30px;
}
.image {
  width: 219.62px;
  height: 219.62px;
  border-radius: 30px;
}
.image[data-v-257d4ec0] {
  width: 219px;
  height: 219px;
  border-radius: 25px;
  margin: 10px 0px 0px 15px;
}
.nav-txt {
  font-size: 48px;
  font-weight: 700;
  color: white;
  text-align: center;
}
.po-popup {
  height: 615px;
  width: 625px;
  background: #252836;
  border-radius: 20px;
}
.checkbox-white input {
  position: relative;
  appearance: none;
  height: 30px;
  width: 30px;
  justify-content: center;
  align-content: center;
  display: flex;
  text-indent: 3px;
}
.checkbox-white input::before {
  position: absolute;
  content: "";
  height: 30px;
  width: 30px;
  background-color: white;
  border: 2px solid #ffffff80;
  border-radius: 3px;
  top: 50%;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  cursor: pointer;
  transition: 0.3s all ease;
}
.checkbox-white input:checked::before {
  background-color: #ffffff80;
  border: 0px solid #ffffff80;
}
.checkbox-white input:checked::after {
  position: absolute;
  content: "\f00c";
  font-family: "FontAwesome";
  color: #fff;
  background-color: #ea7c69;
  border-radius: 10%;
  font-size: 20px;
  display: flex;
  height: 30px;
  width: 30px;
  padding-left: 9%;
  line-height: 160%;

}
.checkbox-orange input:checked::after {
  padding-left: 8%;
  line-height: 140%;
  font-size: 20px;
}
.checkbox-orange input::before {
  height: 30px;
  width: 30px;
}
.checkbox-orange input {
  height: 28px;
  width: 28px;
}
.card {
  width: 600px;
  height: 498px;
  top: 150px;
  border-radius: 24px;
  left: 13%;
  
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
.a {
  justify-content: center;
}
#select_img {
  width: 236px;
  height: 235px;
  border-radius: 25px;
  margin-right: 12px;
  background-color: #717171;
}
.image {
  width: 236px;
  height: 235px;
  border-radius: 25px;
}
</style>