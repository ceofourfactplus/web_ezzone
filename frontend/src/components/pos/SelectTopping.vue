<template>
  <div
    class="modal fade"
    id="selectOptions"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-xl">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <!-- size -->
            <div class="col">
              <div
                class="btn-group-vertical"
                role="group"
                style="width: 100%; height: 100%"
              >
                <button
                  type="button"
                  class="btn btn-warning fs-1 border border-dark"
                  @click="$emit('update_size', 'L')"
                >
                  Large
                </button>
                <button
                  type="button"
                  class="btn btn-warning fs-1 border border-dark"
                  @click="$emit('update_size', 'M')"
                >
                  Medium
                </button>
              </div>
            </div>

            <!-- flavour -->
            <div class="col" style="width: 100%">
              <div class="row">
                <button class="btn btn-warning fs-1 m-1" style="width: 100%">
                  very
                </button>
              </div>
              <div class="row">
                <button class="btn btn-warning fs-1 m-1" style="width: 100%">
                  very
                </button>
              </div>
              <div class="row">
                <button class="btn btn-warning fs-1 m-1" style="width: 100%">
                  very
                </button>
              </div>
              <div class="row">
                <button class="btn btn-warning fs-1 m-1" style="width: 100%">
                  very
                </button>
              </div>
            </div>

            <!-- topping -->
            <div class="col">
              <div class="row">
                <div class="col-6" v-for="topping in toppings" :key="topping">
                  <button class="btn btn-danger fs-4 fw-bold" style="width: 100%;height:100px;" @click="$emit('add_topping',topping)" v-if="product_select.topping.find(item=>item.id==topping.id)==undefined">
                    {{topping.name}} <div class="row"></div>
                    <div class="row">+{{topping.price}}</div>
                  </button>
                  <button class="btn btn-success" @click="$emit('delete_topping',product_select.topping.findIndex(item=>item.id==topping.id))" v-else>
                    {{topping.name}}
                  </button>
                </div>
              </div>
            </div>

            <!-- amount -->
            <div class="col">
              <div class="row">
                <div class="text-center" style="font-size: 120px">

                {{product_select.amount}}
                </div>
              </div>
              <div class="row">
                <div class="btn-group">
                  <button class="btn btn-warning fs-3">+</button>
                  <button class="btn btn-warning fs-3">-</button>
                </div>
              </div>
              <div class="row">
                <h5>total price: {{product_select.total_price}}</h5>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-secondary"
            data-bs-dismiss="modal"
          >
            Close
          </button>
          <button type="button" class="btn btn-primary">Save changes</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  props: ["product_select"],
  data(){
    return{
      toppings:[]
    }
  },
  mounted(){
    axios.get("http://127.0.0.1:8000/product/topping-pos/").then((response) => {
      this.toppings = response.data
    })
  }
};
</script>

<style>
</style>