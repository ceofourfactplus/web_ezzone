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
            <h5 class="modal-title" id="exampleModalLabel">
              Select Option in {{ product_select.product.name }}
            </h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <div class="row fs-3 mb-1">
              <div class="col">Size</div>
              <div class="col">{{ product_select.product.flavour }} level</div>
              <div class="col">Topping</div>
              <div class="col">Amount</div>
            </div>
            <div class="row">
              <!-- size -->
              <div class="col">
                <div
                  class="btn-group-vertical"
                  role="group"
                  style="width: 100%; height: 100%"
                >
                  <button
                    class="btn btn-warning fs-1"
                    @click="$emit('select_size', 'L')"
                    :class="{
                      'btn-danger': product_select.size == 'L',
                    }"
                  >
                    Large
                  </button>
                  <button
                    @click="$emit('select_size', 'M')"
                    class="btn btn-warning fs-1"
                    :class="{
                      'btn-danger': product_select.size == 'M',
                    }"
                  >
                    Medium
                  </button>
                </div>
              </div>

              <!-- flavour -->
              <div class="col" style="width: 100%">
                <div class="row">
                  <button
                    class="btn btn-warning fs-1"
                    style="width: 100%l; margin: 2px"
                    @click="$emit('select_flavour_level', 'none')"
                    :class="{
                      'btn-danger': product_select.flavour_level == 'none',
                    }"
                  >
                    None
                  </button>
                </div>
                <div class="row">
                  <button
                    class="btn btn-warning fs-1"
                    style="width: 100%; margin: 2px"
                    @click="$emit('select_flavour_level', 'low')"
                    :class="{
                      'btn-danger': product_select.flavour_level == 'low',
                    }"
                  >
                    Low
                  </button>
                </div>
                <div class="row">
                  <button
                    class="btn btn-warning fs-1"
                    style="width: 100%; margin: 2px"
                    @click="$emit('select_flavour_level', 'medium')"
                    :class="{
                      'btn-danger': product_select.flavour_level == 'medium',
                    }"
                  >
                    Medium
                  </button>
                </div>
                <div class="row">
                  <button
                    class="btn btn-warning fs-1"
                    style="width: 100%; margin: 2px"
                    @click="$emit('select_flavour_level', 'very')"
                    :class="{
                      'btn-danger': product_select.flavour_level == 'very',
                    }"
                  >
                    Very
                  </button>
                </div>
              </div>

              <!-- topping -->
              <div class="col">
                <div class="row">
                  <div class="col-6" v-for="topping in toppings" :key="topping">
                    <!-- don`t have topping in select_topping  -->
                    <button
                      class="btn btn-warning fs-4 fw-bold"
                      style="width: 100%; height: 100px"
                      @click="$emit('add_topping', topping.topping)"
                      v-if="
                        product_select.topping.find(
                          (item) => item.id == topping.topping.id
                        ) == undefined
                      "
                    >
                      {{ topping.topping.name }}
                      <div
                        v-for="price in topping.topping.price_topping"
                        :key="price"
                      >
                        <div
                          class="row"
                          v-if="price.sale_channel_id == sale_channel_id"
                        >
                          +{{ price.price }}
                        </div>
                      </div>
                    </button>

                    <!-- have topping in select_topping already -->
                    <button
                      class="btn btn-danger fs-4 fw-bold"
                      style="width: 100%; height: 100px"
                      @click="
                        $emit(
                          'delete_topping',
                          product_select.topping.findIndex(
                            (item) => item.id == topping.topping.id
                          )
                        )
                      "
                      v-else
                    >
                      {{ topping.topping.name }}
                    </button>
                  </div>
                </div>
              </div>

              <!-- amount -->
              <div class="col">
                <div class="row">
                  <div class="text-center" style="font-size: 120px">
                    {{ product_select.amount }}
                  </div>
                </div>
                <div class="row">
                  <div class="btn-group">
                    <button
                      class="btn btn-warning fs-3"
                      @click="$emit('decrease_amount')"
                    >
                      -
                    </button>
                    <button
                      class="btn btn-warning fs-3"
                      @click="$emit('increase_amount')"
                    >
                      +
                    </button>
                  </div>
                </div>
                <div class="row mt-4">
                  <h5>total price: {{ product_select.total_price }}</h5>
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
            <button @click="$emit('add_to_cart')" class="btn btn-primary">Add To Cart</button>
          </div>
        </div>
      </div>
  </div>
</template>

<script>
export default {
  props: ["product_select", "toppings", "sale_channel_id"],
};
</script>

<style>
</style>