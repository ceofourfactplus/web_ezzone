<template>
  <div>
    <nav-app :url_name="'Supplier'" save="true" @save="create_sup()"
      >Create&#160;Supplier</nav-app
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
        :class="{ error: error.supplier_name }"
        type="text"
        v-model="supplier_name"
        placeholder="Supplier Name"
      />
      <input
        :class="{ error: error.contact }"
        type="text"
        v-model="contact"
        placeholder="Contact Person"
      />
      <input
        :class="{ error: error.phone_number }"
        type="text"
        v-model="phone_number"
        placeholder="Phone"
      />
      <input type="email" v-model="email" placeholder="E-mail" />
      <textarea
        name="text"
        :class="{ error: error.address }"
        v-model="address"
        id=""
        placeholder="Address"
      ></textarea>
      <input
        type="url"
        v-model="google_map"
        placeholder="Google Map"
        @click="open_map()"
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
  data() {
    return {
      alert: false,
      img: null,
      show_img: null,
      supplier_name: "",
      google_map: "",
      contact: "",
      phone_number: "",
      email: "",
      address: "",
      error: {
        contact: true,
        phone_number: true,
        address: true,
        supplier_name: true,
      },
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
    create_sup() {
      if (
        !this.error.contact &&
        !this.error.phone_number &&
        !this.error.address &&
        !this.error.supplier_name
      ) {
        const user = new FormData();
        user.append("company_name", this.supplier_name);
        user.append("contact", this.contact);
        user.append("email", this.email);
        user.append("address", this.address);
        user.append("google_map", this.google_map);
        user.append("phone", this.phone_number);
        if (this.img != null) {
          user.append("img", this.img, this.img.name);
        }
        user.append("create_by", 1);
        api_raw_material.post("/supplier/", user).then(() => {
          this.alert = true;
          setTimeout(() => {
            this.alert = false;
            this.$router.push({ name: "Supplier" });
          }, 1000);
        });
      }
    },
    open_map() {
      window.open("https://www.google.co.th/maps?hl=en&tab=rl");
    },
  },
  watch: {
    supplier_name(nick) {
      this.error.supplier_name = false;
      this.error.status = false;
      if (nick == "") {
        this.error.supplier_name = true;
      }
    },
    contact(contact) {
      this.error.contact = false;
      this.error.status = false;
      if (contact == "") {
        this.error.contact = true;
      }
    },
    phone_number(number) {
      this.error.status = false;
      var phone = ![...number].some((numbers) => {
        return isNaN(parseInt(numbers));
      });
      if ((number.length == 9 || number.length == 10) && phone) {
        api_raw_material
          .get("check-phone-number/" + number)
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
    address(address) {
      this.error.address = false;
      this.error.status = false;
      if (address == "") {
        this.error.address = true;
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