
<template>
  <input
    type="number"
    @input="handleInput"
    :style="{ 'background-image': url(require(image())) }"
  />
</template>

<script>
export default {
  props:{
  type:{
    type:String
  },
  valid:{
    type:Boolean,
    default:false
  },
  placehoder:{
    type:String,
    default:''
  },
  is_valid:{
    type:Boolean,
    default:false
  },
  first_value:{
    type:String,
    default:''
  },},
  data() {
    return {
      value: '',
    };
  },
  methods: {
    handleInput() {
      this.$emit("input", this.value);
    },
  },
  watch: {
    is_value: function (val) {
      this.texts = val;
      this.$emit("search", val);
    },
  },
  created(){
    this.value = this.first_value 
  },
};
</script>
<style scoped>
input {
  width: 100%;
  background-repeat: no-repeat;
  background-position: 98% 50%;
}
img {
  position: absolute;
  top: 10px;
  right: 20px;
}
</style>