<template>
  <div
    class="modal fade"
    id="selectTable"
    tabindex="-1"
    aria-labelledby="selectTableLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="selectTableLabel">Select Table</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <select
              v-model="select_table"
              class="form-select form-select-lg mb-3"
              aria-label=".form-select-lg example"
            >
              <option selected>Select Table</option>
              <option value='โต๊ะนอกบ้าน'>โต๊ะนอกบ้าน</option>
              <option value='โต๊ะติดกระจก'>โต๊ะติดกระจก</option>
              <option value='โต๊ะ1'>โต๊ะ1</option>
              <option value='โต๊ะ2'>โต๊ะ2</option>
              <option value='โต๊ะ3'>โต๊ะ3</option>
              <option value='โต๊ะ4'>โต๊ะ4</option>
              <option value='โต๊ะ5'>โต๊ะ5</option>
              <option value='โซฟา'>โซฟา</option>
              <option value='โต๊ะหน้ากระดาน1'>โต๊ะหน้ากระดาน1</option>
              <option value='โต๊ะหน้ากระดาน2'>โต๊ะหน้ากระดาน2</option>
              <option value="">none</option>
            </select>
          </div>
          <!-- <div class="row">
            <img scr="../../assets/tablePOS/free-out-door.png" v-if="select_table == 'โต๊ะนอกบ้าน'" alt="">
            <img scr="../../assets/tablePOS/free-mirror.png" v-else-if="select_table === '2'||select_table === '9'||select_table === '10'" alt="">
            <img scr="../../assets/tablePOS/free-table.png" v-else-if="select_table >= '3' && select_table <= '7'" alt="">
            <img scr="../../assets/tablePOS/free-sofa.png" v-else-if="select_table === '8'" alt="">
          </div> -->
        </div>
        <div class="modal-footer">
          <button type="button" data-bs-dismiss="modal" @click="SelectTable" class="btn btn-primary">Save changes</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SelectTable",
  props:['table'],
  data(){
    return{
      select_table:0
    }
  },
  methods:{
    SelectTable(){
      this.$emit('select_table',this.select_table)
    }
  },
  watch:{
    table(newData){
      this.select_table = newData
    }
  }
};
</script>

<style>
</style>