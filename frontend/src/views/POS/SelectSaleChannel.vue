<template>
  <div>
    <nav-app :url_name="'OrderDetail'">Sale Channel</nav-app>
    <div class="center">
      <div class="row">
        <div
          v-for="channel in sale_channel"
          :key="channel.id"
          class="col-6 mb-3 w-100"
        >
          <img :src="channel.img" alt=""
          @click="select_channel(channel)" />
          <p>{{ channel.sale_channel }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { api_pos } from '../../api/api_pos';
import { api_product } from "../../api/api_product";
import NavApp from "../../components/main_component/NavApp.vue";
export default {
  components: { NavApp },
  mounted() {
    api_product.get("read-sale-channel/").then((response) => {
      this.sale_channel = response.data;
    });
  },
  data() {
    return {
      sale_channel: [],
      image_new: "",
    };
  },
  methods: {
    select_channel(channel) {
      this.$store.state.pos.order.sale_channel_id = channel.id
      console.log(channel)
      this.$store.state.pos.order.sale_channel_set = channel
      api_pos.get('order-number').then((response) => {
        this.$store.state.pos.order.order_number = response.data.order_number
      })
      this.$router.push({
        name: "KeyOrder",
      });
    },
  },
};
</script>

<style scoped>
.center {
  margin: auto;
  width: 75%;
  margin-top: 40px;
}
.col-6 {
  margin: auto;
}
p {
  white-space: nowrap;
  font-size: 30px;
  color: #fff;
  font-weight: 700;
}
img {
  width: 120px;
  height: 120px;
  border-radius: 10px;
  object-fit: cover;
}
</style>