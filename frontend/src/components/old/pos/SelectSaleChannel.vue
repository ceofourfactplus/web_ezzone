<template>
  <div class="modal fade" id="selectSaleChannel" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Select Sale Channel</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <div class="row">
          <div class="col-3 m-1" v-for="channel in sale_channels" :key="channel" data-bs-dismiss="modal">
            <button class="btn" :style="{'background-color':channel.color}" :class="{'btn-danger':selected_channel.id == channel.id,'disabled':table !='' }" @click="$emit('select_channel',channel)">
              <img :src="channel.img" width="100" height="100" style="border-radius:5px;" alt="">
              <h5 class="mt-1">{{ channel.sale_channel }}
              </h5>
            </button>
            
          </div>
          <div class="col-3 m-1"><button class="btn btn-warning" @click="$emit('select_channel','');$emit('select_table','')">
              <img src="../../assets/img/tablePOS/free-table.png" width="100" height="100" style="border-radius:5px;" alt="">
              <h5 class="mt-1">cancel
              </h5>
            </button></div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  props:['sale_channels','selected_channel','table']
}
</script>

<style>

</style>