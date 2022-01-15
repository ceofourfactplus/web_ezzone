<template>
    <div>
        <nav-app :reward_menu="true">All Reward</nav-app>

        <!-- Search Bar -->
        <div class="row" style="max-width:672px;margin:0px;">
            <div class="col-7 w-100 BlockSearch">
                <SearchBar @search="search"/> 
            </div>
            <div class="col-5 w-100 BlockUserPoints">
                <div class="row" style="padding: 0px;width: 266px;margin-right: 0px;margin-left: 0px;line-height:35px;">
                    <div class="col-2 w-100" style="margin-left:-15px;margin-top:-2px;"><img src="../../assets/icon/user-icon.png" alt=""></div>
                    <div class="col-5 w-100 ItmeUserPoints">คุณแอปเปิ้ลgs</div>
                    <div class="col-1 w-100" style="max-width:2px;">:</div>
                    <div class="col-2 w-100 ItmeUserPoints" style="left:-20px;">9999</div>
                    <div class="col-2 w-100 ItmeUserPoints">Point</div>

                </div>

            </div>
        </div>

        <!-- AreaBlockItem -->
        <div class="col-12"
        style="margin-left: 24px;
        margin-right: 24px;
        margin-top: 20px;
        margin-bottom: 20px;
        border-radius:20px;
        height: 100%px;
        width: 672px;">
        <!-- BlockItme -->

            <div class="row" style="position:relative;margin-top:15px;">
                
                <div class="BlockItem">
                    <div class="PictureItem">
                        <img src="../../assets/img/BG.png" alt="" style="height: 120px;width: 120px;">
                    </div>
                    <div class="FontItem">Special Set1</div>
                    <div class="FontItem">200 Points</div>
                    <div class="SeeDetail">See Details</div>
                </div>
                <div></div>
                <div class="BlockItem">
                    <div class="PictureItem">
                        <img src="../../assets/img/BG.png" alt="" style="height: 120px;width: 120px;">
                    </div>
                    <div class="FontItem">Special Set1</div>
                    <div class="FontItem">200 Points</div>
                    <div class="SeeDetail">See Details</div>
                </div>
                <div></div>
                <div class="BlockItem">
                    <div class="PictureItem">
                        <img src="../../assets/img/BG.png" alt="" style="height: 120px;width: 120px;">
                    </div>
                    <div class="FontItem">Special Set1</div>
                    <div class="FontItem">200 Points</div>
                    <div class="SeeDetail">See Details</div>
                </div>
                <div></div>
                <div class="BlockItem">
                    <div class="PictureItem">
                        <img src="../../assets/img/BG.png" alt="" style="height: 120px;width: 120px;">
                    </div>
                    <div class="FontItem">Special Set1</div>
                    <div class="FontItem">200 Points</div>
                    <div class="SeeDetail">See Details</div>
                </div>   
            </div>   

            <div class="row" style="position:relative;margin-top:15px;">
                
                <div class="BlockItem">
                    <div class="PictureItem">
                        <img src="../../assets/img/BG.png" alt="" style="height: 120px;width: 120px;">
                    </div>
                    <div class="FontItem">Special Set1</div>
                    <div class="FontItem">200 Points</div>
                    <div class="SeeDetail">See Details</div>
                </div>
                <div></div>
                <div class="BlockItem">
                    <div class="PictureItem">
                        <img src="../../assets/img/BG.png" alt="" style="height: 120px;width: 120px;">
                    </div>
                    <div class="FontItem">Special Set1</div>
                    <div class="FontItem">200 Points</div>
                    <div class="SeeDetail">See Details</div>
                </div>
                <div></div>
                <div class="BlockItem">
                    <div class="PictureItem">
                        <img src="../../assets/img/BG.png" alt="" style="height: 120px;width: 120px;">
                    </div>
                    <div class="FontItem">Special Set1</div>
                    <div class="FontItem">200 Points</div>
                    <div class="SeeDetail">See Details</div>
                </div>
                <div></div>
                <div class="BlockItem">
                    <div class="PictureItem">
                        <img src="../../assets/img/BG.png" alt="" style="height: 120px;width: 120px;">
                    </div>
                    <div class="FontItem">Special Set1</div>
                    <div class="FontItem">200 Points</div>
                    <div class="SeeDetail">See Details</div>
                </div>   
            </div>

            <div class="row" style="position:relative;margin-top:15px;">
                
                <div class="BlockItem">
                    <div class="PictureItem">
                        <img src="../../assets/img/BG.png" alt="" style="height: 120px;width: 120px;">
                    </div>
                    <div class="FontItem">Special Set1</div>
                    <div class="FontItem">200 Points</div>
                    <div class="SeeDetail">See Details</div>
                </div>
                <div></div>
                <div class="BlockItem">
                    <div class="PictureItem">
                        <img src="../../assets/img/BG.png" alt="" style="height: 120px;width: 120px;">
                    </div>
                    <div class="FontItem">Special Set1</div>
                    <div class="FontItem">200 Points</div>
                    <div class="SeeDetail">See Details</div>
                </div>
                <div></div>
                <div class="BlockItem">
                    <div class="PictureItem">
                        <img src="../../assets/img/BG.png" alt="" style="height: 120px;width: 120px;">
                    </div>
                    <div class="FontItem">Special Set1</div>
                    <div class="FontItem">200 Points</div>
                    <div class="SeeDetail">See Details</div>
                </div>
                <div></div>
                <div class="BlockItem">
                    <div class="PictureItem">
                        <img src="../../assets/img/BG.png" alt="" style="height: 120px;width: 120px;">
                    </div>
                    <div class="FontItem">Special Set1</div>
                    <div class="FontItem">200 Points</div>
                    <div class="SeeDetail">See Details</div>
                </div>   
            </div>
          
        </div>
    </div>
</template>

<script>
export default {  
  name: "AllReward",
  components : {
      NavApp,
      SearchBar
      
  },
  data() {
      return{
        
      }
  },
  methods: {
      search(val) {
          console.log(val)
      }
  },

};

import NavApp from "../../components/main_component/NavApp.vue"
import SearchBar from "../../components/materials/SearchBar.vue"

</script>

<style scoped>

.BlockSearch {

    height: 45px;
    margin-left: 20px;
    margin-right: 20px;
    margin-top: 10px;
    margin-bottom: 20px;

}

.BlockUserPoints {
    color:#fff;
    font-size: 18px;
    background-color: #303344;
    height: 45px;
    margin-left: 20px;
    margin-right: 20px;
    margin-top: 10px;
    margin-bottom: 20px;
    padding: 0px;
    border: 4px solid #EA7C69;
    border-radius: 20px;


}

.ItmeUserPoints {

    padding: 0px;
    text-align: left;

}

.BlockItem {
    position: relative;
    display: inline-block;
    height: 240px;
    width: 150px;
    border-radius: 10px;
    padding-left: 8px;
    padding-right: 8px;
    padding-top: 6px;
    margin: 0px;
    left: 14px;
    background-color: #303344;
}

.PictureItem {

    position: relative;
    height: 120px;
    width: 135px;

}

.FontItem {

    color:#fff;
    font-size: 20px;

}

.SeeDetail {

    color: #EA7C69;
    border: 2px solid #EA7C69;
    border-radius: 20px;
    height: 30px;
    width: 110px;
    margin-left: 12px; 
    margin-right: 12px; 
    margin-top: 10px; 


}

</style>