<template>
  <div>
    
  </div>
</template>

<script>
// import api_raw_material from "../../api/api_raw_material"

export default {
  components: {
      
  },
  mounted() {
      this.is_staff = this.$store.state.auth.userInfo['is_staff']
  },
  data() {
    return {
        is_staff: false,
    };
  },
  methods: {},
};
</script>

<style scoped>

</style>