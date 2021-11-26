<template>
  <table class="table table-dark fw-bold fs-5">
    <thead style="position: sticky">
      <tr>
        <th>#</th>
        <th>SaleChannel</th>
        <th>able</th>
        <th>edit/delete</th>
      </tr>
    </thead>
    <tbody class="scroll">
      <tr
        v-for="(channel, index) in sales_channels"
        v-show="!load"
        :key="channel.id"
      >
        <td>{{ index + 1 }}</td>
        <td>{{ channel.sale_channel }}</td>
        <td>
          <Switch :value="channel.status" :id="channel.id" @input="Switch" />
        </td>
        <td>
          <div class="btn-group">
            <button
              class="btn btn-warning"
              @click="$emit('select_channel',channel)"
              data-bs-toggle="modal"
              data-bs-target="#UpdateSaleChannel"
            >
              <i class="fas fa-arrow-alt-circle-up"></i>update
            </button>
            <button class="btn btn-danger" @click="DeleteSaleChannel(channel.id)">
              <i class="fas fa-trash-alt"></i>delete
            </button>
          </div>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import axios from "axios";
import Switch from "../../switch.vue";

export default {
  components: { Switch, },
  props:['sales_channels'],  
  name: "SaleChannelTable",
  data() {
    return {
      load: false,
      select_SaleChannel: "",
    };
  },
  methods: {
    Switch(value, id) {
      axios
        .put("http://127.0.0.1:8000/product/sale-channel/status/" + id + "/", {
          status: value,
          update_by: this.$store.state.auth.userInfo.id,
        })
        .then(() => {
          this.$emit("reload")
        });
    },
    DeleteSaleChannel(id) {
      axios
        .delete("http://127.0.0.1:8000/product/sale-channel/" + id + "/")
        .then(() => {
          this.$emit("reload")
        });
    },
  },
};
</script>

<style>
</style>