<template>
  <div>
    <nav-app save="true" @save="create_sup()">Create&#160;Supplier</nav-app>
    <div class="container">
      <div style="height: 250px">
        <label for="file">
          <img
            v-if="show_img == null"
            width="190"
            height="190"
            src="../../assets/icon/User.png"
            class="register-user"
          />
          <img
            v-else
            :src="show_img"
            width="190"
            height="190"
            class="register-user"
          />
        </label>
        <input
          type="file"
          @change="onFileChange"
          style="display: none"
          id="file"
          class="register-user"
        />
        <!-- <check-box-white/> -->
      </div>
      <input type="text" v-model="supplier_name" placeholder="Supplier Name"/>
      <input type="text" v-model="contact" placeholder="Contact Person"/>
      <input type="number" v-model="phone" placeholder="Phone"/>
      <input type="email" v-model="email" placeholder="E-mail"/>
      <textarea name="text" v-model="address" id="" placeholder="Address"></textarea>
      <input type="url" v-model="google_map" placeholder="Google Map"/>
    </div>
  </div>
</template>

<script>
import { api_raw_material } from '../../api/api_raw_material';
import NavApp from "../../components/main_component/NavApp.vue";
export default {
  components: { NavApp },
  data() {
    return {
      img: "",
      show_img: null,
      supplier_name:'',
      google_map:'',
      contact:'',
      phone:0,
      email:'',
      address:'',
    };
  },
  methods: {
    onFileChange(e) {
      this.img = e.target.files[0];
      if (this.img) {
        const reader = new FileReader();
        reader.onload = (e) => (this.show_img = e.target.result);
        reader.readAsDataURL(this.img);
      }
    },
    create_sup(){
      const user = new FormData();
        user.append("company_name", this.supplier_name);
        user.append("contact", this.contact);
        user.append("email", this.email);
        user.append("address", this.address);
        user.append("google_map", this.google_map);
        user.append("phone", this.phone);
        user.append("img", this.img,this.img.name);
        user.append('create_by',1)
      api_raw_material.post('supplier',user).then(()=>{
        this.$router.push({name:'Supplier'})
      })
    }
  },
};
</script>

<style scoped>
.register-user {
  top: 120px;
  left: 37%;
  position: fixed;
  border-radius: 50%;
}
input {
  width: 100%;
  margin-bottom: 20px;
  height: 60px;
}
textarea {
  width: 100%;
  margin-bottom: 20px;
  height: 140px;
}
</style>