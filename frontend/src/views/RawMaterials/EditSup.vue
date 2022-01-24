<template>
  <div>
    <nav-app save="true" :url_name="'Supplier'" @save="create_sup()"
      >Edit&#160;Supplier</nav-app
    >
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
      <input
        :class="{ error: error.company_name }"
        type="text"
        v-model="supplier.company_name"
        placeholder="Supplier Name"
      />
      <input
        :class="{ error: error.contact }"
        type="text"
        v-model="supplier.contact"
        placeholder="Contact Person"
      />
      <input
        :class="{ error: error.phone_number }"
        type="text"
        v-model="supplier.phone"
        placeholder="Phone"
      />
      <input type="email" v-model="supplier.email" placeholder="E-mail" />
      <textarea
        :class="{ error: error.address }"
        name="text"
        v-model="supplier.address"
        id=""
        placeholder="Address"
      ></textarea>
      <input
        type="url"
        v-model="supplier.google_map"
        placeholder="Google Map"
      />
    </div>
    <SavePopup :alert="alert" />
  </div>
</template>

<script>
import SavePopup from "../../components/main_component/SavePopup.vue";
import { api_raw_material } from "../../api/api_raw_material";
import NavApp from "../../components/main_component/NavApp.vue";
export default {
  components: { NavApp, SavePopup },
  mounted() {
    api_raw_material
      .get("supplier/" + this.$route.params.id)
      .then((response) => {
        this.supplier = response.data;
        this.show_img = response.data.img;
      });
  },
  data() {
    return {
      supplier: {},
      show_img: null,
      change_img: false,
      error: {
        address: false,
        contact: false,
        company_name: false,
        phone_number: false,
      },
    };
  },
  methods: {
    onFileChange(e) {
      this.supplier.img = e.target.files[0];
      if (this.supplier.img) {
        this.change_img = true;
        const reader = new FileReader();
        reader.onload = (e) => (this.show_img = e.target.result);
        reader.readAsDataURL(this.supplier.img);
      }
    },
    create_sup() {
      if (
        !this.error.contact &&
        !this.error.phone_number &&
        !this.error.address &&
        !this.error.supplier_name
      ) {
        const user = new FormData();
        user.append("company_name", this.supplier.company_name);
        user.append("contact", this.supplier.contact);
        user.append("email", this.supplier.email);
        user.append("address", this.supplier.address);
        user.append("google_map", this.supplier.google_map);
        user.append("phone", this.supplier.phone);
        if (this.change_img) {
          user.append("img", this.supplier.img, this.supplier.img.name);
        }
        user.append("create_by", 1);
        api_raw_material
          .put("supplier/" + this.$route.params.id, user)
          .then(() => {
            this.$router.push({ name: "Supplier" });
          });
      }
    },
  },
  watch: {
    "supplier.phone"(number) {
      this.error.status = false;
      var phone = ![...number].some((numbers) => {
        return isNaN(parseInt(numbers));
      });
      if ((number.length == 9 || number.length == 10) && phone) {
        api_raw_material
          .get("check-phone-number/" + number + "/" + this.$route.params.id)
          .then((result) => {
            console.log(result);
            this.error.phone_number = false;
          })
          .catch((err) => {
            console.log(err);
            this.error.phone_number = true;
          });
      } else {
        this.error.phone_number = true;
      }
    },
    "supplier.nick_name"(nick) {
      this.error.nick_name = false;
      this.error.status = false;
      if (nick == "") {
        this.error.nick_name = true;
      }
    },
    "supplier.nick_name"(nick) {
      this.error.nick_name = false;
      this.error.status = false;
      if (nick == "") {
        this.error.nick_name = true;
      }
    },
    "supplier.nick_name"(nick) {
      this.error.nick_name = false;
      this.error.status = false;
      if (nick == "") {
        this.error.nick_name = true;
      }
    },
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