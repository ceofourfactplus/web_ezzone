<template>
    <div class="table">
        <div class="table-header">
            <div class="row" >
                <div class="checkbox-white">
                <input
                    type="checkbox"
                    :value="true"
                    style="margin-top: 12px; right: 0px; left: 23px;background-color: #ffffff00"
                    @input="selectAllItem"
                />
                </div>
                <div class="col-5 w-100">Product</div>
                <div class="col-3 w-100">Topping</div>
                <div class="col-1 w-100">Qty</div>
                <div class="col-2 w-100">Price</div>

            </div>
        </div>
        <div class="table-item">
            <div class="row" style="line-height:25px;" >
                <div class="checkbox-white">
                <input
                    type="checkbox"
                    :value="true"
                    style="margin-top: 12px; right: 0px; left: 23px;background-color: #ffffff00"
                    @input="selectAllItem"
                />
                </div>
                <div class="col-5 w-100">ข้าวผัดผงกะหรี่กุ้ง</div>
                <div class="col-3 w-100">ไข่ข้น</div>
                <div class="col-1 w-100">1</div>
                <div class="col-2 w-100">59</div>

            </div>
        </div>
        <div class="table-item">
            <div class="row" style="line-height:25px;" >
                <div class="checkbox-white">
                <input
                    type="checkbox"
                    :value="true"
                    style="margin-top: 12px; right: 0px; left: 23px;background-color: #ffffff00"
                    @input="selectAllItem"
                />
                </div>
                <div class="col-5 w-100">ข้าวผัดผงกะหรี่กุ้ง</div>
                <div class="col-3 w-100">ไข่ข้น</div>
                <div class="col-1 w-100">1</div>
                <div class="col-2 w-100">59</div>

            </div>
        </div>
        <div class="table-item">
            <div class="row" style="line-height:25px;" >
                <div class="checkbox-white">
                <input
                    type="checkbox"
                    :value="true"
                    style="margin-top: 12px; right: 0px; left: 23px;background-color: #ffffff00"
                    @input="selectAllItem"
                />
                </div>
                <div class="col-5 w-100">ข้าวผัดผงกะหรี่กุ้ง</div>
                <div class="col-3 w-100">ไข่ข้น</div>
                <div class="col-1 w-100">1</div>
                <div class="col-2 w-100">59</div>

            </div>
        </div>
        <div class="table-item">
            <div class="row" style="line-height:25px;" >
                <div class="col-9 w-100"></div>
                <div class="col-1 w-100" >Total</div>
                <div class="col-2 w-100" >59</div>
            </div>        
        </div>
        <div class="table-item">
            <div class="row" style="line-height:25px;" >
                <div class="col-5 w-100"></div>
                <div class="col-5 w-100" style="text-align: right;" >Discount Price</div>
                <div class="col-2 w-100" >59</div>
            </div>        
        </div>
        <div></div>
        
    </div>
</template>

<script>
export default {  
  name: "starttestvue"
};
</script>

<style scoped>
.table {
    width: 672px;
    height: 290px;
    background-color: rgb(206, 221, 221);
}
.row {
    width: 672px;
    height: 45px;
    margin: 0px;
}
.checkbox-white {
    display: inline-block;
    position: relative;
    left: -15px;
    top: -8px;
    
}
.checkbox-white input::before {
    position: absolute;
    content: "";
    height: 20px;
    width: 20px;
    background-color: #252836;
    border: 2px solid #ffffff80;
    border-radius: 3px;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    cursor: pointer;
    transition: 0.3s all ease;
}
.checkbox-white input:checked::before {
    background-color: #252836;
    border: 2px solid #ffffff80; 
}
.checkbox-white input:checked::after {
    position: absolute;
    content: "\f00c";
    font-family: "FontAwesome";
    color: #c2c2c5ea;
    font-size: 13px;
    top: -2px;
    left: 0.5px;
    display: flex;
}
.table-item {
    margin-top: 5px;
}
</style>

<div class="row table-itme" id="BlockSaleChannel">
        <!-- Sale Channel Setting -->
        <div class="row" style="margin-top: 45px">
          <div class="col-6 w-100 dbs-font" style="margin-left: -5px">
            Sale Channel Setting
          </div>
          <div class="col-1 w-100">
            <img
              src="../../assets/icon/edit-orange.png"
              style="width: 25px; height: 30px; margin-top: 5px"
              @click="$router.push({ name: 'SaleChannel' })"
            />
          </div>
        </div>
        <!-- Sale Channel -->
        <div class="row" style="width: 540px; margin-left: 39px">
          <div class="col-6 w-100" style="margin-top: 10px">
            <img
              src="../../assets/icon/lineman-35x35.png"
              style="display: inline"
            />
            <p
              style="
                display: inline;
                font-size: 20px;
                color: white;
                margin-left: 10px;
              "
            >
              Line Man
            </p>
            <div class="sc-status">ACTIVE</div>
          </div>
          <div class="col-6 w-100" style="margin-top: 10px">
            <img
              src="../../assets/icon/robin-35x35.png"
              style="display: inline"
            />
            <p
              style="
                display: inline;
                font-size: 20px;
                color: white;
                margin-left: 10px;
              "
            >
              Line Man
            </p>
            <div class="sc-status">ACTIVE</div>
          </div>
        </div>
        
        <div class="row" style="width: 540px; margin: 20px 0px 0px 39px">
            <div class="col-6 w-100" style="margin-top: 10px">
              <img
                src="../../assets/icon/foodpanda-35x35.png"
                style="display: inline"
              />
              <p
                style="
                  display: inline;
                  font-size: 20px;
                  color: white;
                  margin-left: 10px;
                "
              >
                Line Man
              </p>
              <div class="sc-status">ACTIVE</div>
            </div>
            <div class="col-6 w-100" style="margin-top: 10px">
              <img src="../../assets/icon/grab-35x35.png" style="display: inline" />
              <p
                style="
                  display: inline;
                  font-size: 20px;
                  color: white;
                  margin-left: 10px;
                "
              >
                Line Man
              </p>
              <div class="sc-status">ACTIVE</div>
            </div>
          </div>
      </div>

      ../../assets/icon/foodpanda-35x35.png
      ../../assets/icon/grab-35x35.png