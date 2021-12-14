<template>
  <table class="table table-dark fw-bold fs-5">
    <thead>
      <tr>
        <th>img</th>
        <th>code</th>
        <th>name</th>
        <th>price</th>
        <th>able</th>
        <th>edit/delete</th>
      </tr>
    </thead>
    <tbody class="scroll">
      <tr v-for="item in all_topping" :key="item">
        <td>
          <img
            id="image"
            :src="item.img"
            style="width:60px;height:60px;border"
            :alt="item"
          />
        </td>
        <td>{{ item.code }}</td>
        <td>{{ item.name }}</td>
        <td>
          <button
            class="btn btn-primary"
            @click="$emit('select_topping', item)"
            type="button"
            data-bs-toggle="offcanvas"
            data-bs-target="#price-detail"
            aria-controls="offcanvasRight"
          >
            see price detail
          </button>
        </td>
        <td>
          <Switch :value="item.status" :id="item.id" @input="Switch" />
        </td>
        <td>
          <div class="btn-group">
            <button
              class="btn btn-warning"
              @click="$emit('select_topping', item)"
              data-bs-toggle="modal"
              data-bs-target="#UpdateTopping"
            >
              <i class="fas fa-arrow-alt-circle-up"></i>update
            </button>
            <button class="btn btn-danger" @click="DeleteTopping(item.id)">
              <i class="fas fa-trash-alt"></i>delete
            </button>
          </div>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import Switch from "../../../components/switch";
import axios from "axios";
export default {
  components: { Switch },
  props: ["all_topping"],
  methods: {
    Switch(value, id) {
      axios
        .put(
          "http://127.0.0.1:8000/product/topping/status/" + id + "/",
          {
            status: value,
            update_by: this.$store.state.auth.userInfo.id,
          }
        )
        .then((data) => {
          this.$emit("reload");
          console.log(data.data);
        });
    },
    DeleteTopping(id) {
      axios
        .delete("http://127.0.0.1:8000/product/topping/" + id + "/")
        .then(() => {
          this.$emit("reload");
        });
    },
  },
};
</script>

<style scoped>
#image {
  width: 40px;
  height: 40px;
  border-radius: 20%;
}
</style>