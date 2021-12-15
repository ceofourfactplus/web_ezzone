<template>
  <div>
    <img class="back" src="../../assets/icon/btn-back.png" />
    <h2 class="header">{{ header }}</h2>
    <input 
        type="checkbox" 
        name="checkbox" 
        id="checkbox" 
        v-model="ham_val" 
        @click="tick"
        />
    <label for="checkbox"></label>
    <div class="float-menu" v-if="ham_val">
        <p
            v-for="(item, idx) in ham_menus" 
            :key="idx" 
            class="float-menu-item"
            @click="select_ham(item)"
            :class="{'clicked': ham == item.name}"
            >
            {{ item.name }}
            </p>
            <!-- <router-link :to="{{ item.url }}">{{ item.name }}</router-link> -->
    </div>
  </div>
</template>


<script>
export default {
  name: "NavRM",
  props: ["header"],
  data() {
    return {
      ham_val: false,
      ham_menus: [
          {name: 'Raw Materials'},
          {name: 'Manage Raw Material'},
          {name: 'Suppliers'},
          {name: 'PO for Suppliers'},
          {name: 'Add Raw Material'},
          {name: 'Pickup Raw Material'},
          {name: 'Minimum'},
      ],
        ham: '',
    };
  },
  methods: {
    tick() {
      console.log(this.ham_val);
    },
    select_ham(ham) {
        this.ham = ham.name
    }
  },
};
</script>

<style>
input[type="checkbox"] {
  -webkit-appearance: none;
  appearance: none;
  width: 50px;
  height: 50px;
  cursor: pointer;
  content: url("../../assets/icon/btn-navbar.png");
  position: fixed;
  right: 7%;
  top: 5%;
}

label{
    cursor: pointer;
}

.float-menu{
    width: 290px;
    height: 360px;
    background-color: #363c55;
    margin-right: 7px;
    right: 0;
    top: 10%;
    position: absolute;
    padding-left: 12px;
}

.float-menu-item{
    color: grey;
    font-size: 25px;
    text-align: left;
}

.clicked{
    color: #ea7c69;
}
</style>