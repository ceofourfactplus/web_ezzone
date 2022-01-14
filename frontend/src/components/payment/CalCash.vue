<template>
  <div v-if="show_cal">
    <div class="dark" @click="$emit('hide_cal')"></div>
    <div class="calculator">
      <div class="result">
        <div style="position: absolute; top: 8px; right: 30px">
          {{ parseInt(result).toLocaleString(undifined) }}
        </div>

        <div
          style="
            position: absolute;
            top: 80px;
            right: 30px;
            font-size: 20px;
            color: #ea7c69;
          "
        >
          total : {{ parseInt(total_price).toLocaleString(undifined) }}
        </div>

        <img
          src="../../assets/icon/clear.png"
          class="clear"
          @click="result = '0'"
        />
      </div>
      <div class="key mt-2">
        <div class="row">
          <div
            v-for="i in 3"
            :key="i"
            class="col-4 w-100"
            :class="{ 'border-l': i != 1 }"
            @click="add_number(i)"
          >
            {{ i }}
          </div>
          <div class="col-12 line"></div>
          <div
            v-for="i in [4, 5, 6]"
            :key="i"
            class="col-4 w-100"
            :class="{ 'border-l': i != 4 }"
            @click="add_number(i)"
          >
            {{ i }}
          </div>
          <div class="col-12 line"></div>
          <div
            v-for="i in [7, 8, 9]"
            :key="i"
            class="col-4 w-100"
            :class="{ 'border-l': i != 7 }"
            @click="add_number(i)"
          >
            {{ i }}
          </div>
          <div class="col-12 line"></div>
          <div
            v-if="false"
            class="col-4 w-100"
            @click="add_number('%')"
            style="font-size: 55px; line-height: 114px"
          >
            %
          </div>
          <div
            v-else
            class="col-4 w-100"
            style="font-size: 55px; line-height: 114px"
          ></div>
          <div class="col-4 w-100 border-l" @click="add_number('0')">0</div>
          <div
            class="col-4 w-100 border-l"
            style="font-size: 55px; line-height: 114px"
            @click="submit()"
          >
            OK
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["show_cal", "total_price"],
  data() {
    return {
      result: "0",
    };
  },
  methods: {
    add_number(i) {
      this.result = this.result + i;
    },
    submit() {
      this.$emit("submit_c", this.result);
    },
  },
};
</script>

<style scoped>
.calculator {
  width: 400px;
  height: 637px;
  top: 43%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: #303344;
  position: absolute;
  opacity: 1;
  border-radius: 10px;
  padding: 20px;
}
.dark {
  background-color: #00000099;
  width: 100%;
  height: 100%;
  top: 0px;
  left: 0px;
  position: fixed;
  display: block;
}
.result {
  background: #474747;
  border-radius: 5px;
  width: 360px;
  color: #fff;
  padding-right: 10px;
  text-align: right;
  font-weight: bold;
  font-size: 48px;
  height: 93px;
}
.key {
  width: 355px;
  height: 510px;
}
.line {
  height: 1px;
  width: 340px;
  background-color: #fff;
  margin: 10px auto;
}
.col-4 {
  color: #fff;
  font-weight: bold;
  font-size: 72px;
}
.border-l {
  border-left: 1px solid #fff;
}
.clear {
  position: absolute;
  left: 30px;
  top: 51px;
  width: 28px;
}
</style>