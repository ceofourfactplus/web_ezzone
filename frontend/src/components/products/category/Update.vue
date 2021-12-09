<template>
  <!-- Create Category Modal -->
  <div
    class="modal fade"
    id="UpdateCategory"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Update Category</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <form @submit="save_category()">
            <div class="col-12 mb-3">
              <label for="Category" class="form-label">Category</label>
              <input
                type="text"
                class="form-control"
                v-model="category_name"
                id="Category"
                placeholder="Drink"
              />
            </div> 
            <div class="col-12">
              <div class="row">
                <label for="exampleColorInput" class="col-5 form-label"
                  >Color picker</label
                >
                <div class="col-6 me-2">
                  <input
                    type="color"
                    v-model="color"
                    class="form-control"
                    id="exampleColorInput"
                    title="Choose your color"
                    opacity
                  />
                </div>
              </div>
            </div>
            <button
              type="submit"
              data-bs-dismiss="modal"
              class="btn btn-primary"
              style="width: 100%"
            >
              save
            </button>
          </form>
        </div>
        
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapState } from "vuex";
export default {
  name: "UpdateCategory",
  computed: mapState(["auth", "product"]),
  props: ["category"],
  data() {
    return {
      category_name: "",
      color:''
    };
  },
  methods: {
    save_category() {
      axios
        .put(
          "http://127.0.0.1:8000/product/category/" + this.category.id + "/",
          {
            category: this.category_name,
            color:this.color,
            create_by: this.category.create_by,
            update_by: this.$store.state.auth.userInfo.id,
          }
        )
        .then(() => {
          this.$emit("save");
        });
    },
  },
  watch:{
    category(newCategory) {
     this.category_name = newCategory.category   
     this.color = newCategory.color
    }
  }
};
</script>

<style>
</style>