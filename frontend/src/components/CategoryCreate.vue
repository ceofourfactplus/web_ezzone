<template>
  <!-- Create Category Modal -->
  <div
    class="modal fade"
    id="createModal"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Create Category</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <form @submit="save_category()">
            <div class="mb-3">
              <label for="Category" class="form-label">Category</label>
              <input
                type="text"
                class="form-control"
                v-model="category"
                id="Category"
                placeholder="Drink"
              />
            </div>
            <button type="submit" class="btn btn-promary">save</button>
          </form>
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
import axios from 'axios'
import { mapState} from "vuex"
export default {
  name: "CategoryCreate",
  computed: mapState(['auth','product']),
  data() {
    return {
      category: "",
    };
  },
  methods:{
    save_category(){
      axios.post('http://127.0.0.1:8000/product/category/',{category:this.category,create_by:this.$store.state.auth.userInfo.id,update_by:this.$store.state.auth.userInfo.id}).then(response=>{
        this.$store.state.product.category = response.data
      })
    }
  }
};
</script>

<style>
</style>