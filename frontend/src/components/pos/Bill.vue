<template>
  <table class="table table-dark table-striped">
    <thead>
      <tr>
        <th>#</th>
        <th>name</th>
        <th>topping</th>
        <th>sweet</th>
        <th>amount</th>
        <th>price</th>
        <th>edit</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(order, index) in bill" :key="order">
        <th>{{ index }}</th>
        <th>name</th>
        <th>topping</th>
        <th>sweet</th>
        <th>amount</th>
        <th>price</th>
        <th>edit</th>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  props:['bill']
};
</script>

<style>
</style>