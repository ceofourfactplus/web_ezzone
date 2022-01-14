<template>
    <div>
        <nav-app>Redemption</nav-app>
        <!-- CustommerPhone Block -->
        <div class="row" 
        style="line-height:65px;
        border-radius:10px;
        height: 70px;
        background-color: #303344;
        margin-left: 24px;
        margin-right: 24px;
        margin-top: 20px;
        margin-bottom: 20px;">
            <div 
            class="col-4 w-100" 
            style="font-size:30px;
            padding:0px;
            text-align: right;
            color: #FFFFFF;
            ">Custumer Phone</div>
            <input 
            class="col-8"
            type ="text" 
            v-model="CustommerPhone"
            placeholder="XXX-XXX-XXXX"
            style="font-size:30px;
            color: #FFFFFF;
            line-height:50px;
            margin:10px;
            border-radius: 10px;
            height: 50px;
            width: 408px;
            background-color: #717171;
            text-align: left;
            padding-left:20px;
            "/>
        </div>
        <!-- Data Block -->
        <div class="row"
        style="line-height:65px;
        background-color: #303344;
        margin-left: 24px;
        margin-right: 24px;
        margin-top: 20px;
        margin-bottom: 20px;
        border-radius:10px;
        height: 245px;">
        <!-- Picture Block -->
            <div class="col-4 "
            style="background-color:#717171;
            border-radius: 10px;
            height: 200px;
            width: 200px;
            margin: 10px;
            left: 10px;
            bottom: -13px;
            position:relative;">
            <img src="../../assets/img/PropertyDiamond.png" alt="" style="height: 250px;width: 198px;left:-11px;top:-10px;position:relative;">
            </div>
        <!-- Description Block -->
            <div class="col-8 w-100" style="font-size:30px;color:#ffffff;">
                <!-- Point -->
                <div class="row" style="height:68px;margin-top:20px;line-height:80px;">
                    <div class="col-3 w-100" id="ColPoint">Point</div>
                    <div class="col-1 w-100" id="DotPoint">:</div>
                    <div class="col-5 w-100" style="height:64px;display:inline-block;font-size:42px;line-height:75px;padding-left:10px;text-align:left;">999,999</div>
                    <div class="col-3 w-100" id="LinkHistory"><a href="http://localhost:8080/?#/promotion/redemption/history">History</a></div>
                </div>
                <!-- Name -->
                <div class="row" style="height:53px;margin-top:10px;line-height:50px;">
                    <div class="col-3 w-100 " id="ColName" style="height:50px;display:inline-block;text-align:left;">Name</div>
                    <div class="col-1 w-100"  id="DotName">:</div>
                    <div class="col-8 w-100 " id="DetailName">Kantphich</div>
                </div>
                <!-- Birthdate -->
                <div class="row" style="height:53px;margin-top:10px;line-height:50px;">
                    <div class="col-4 w-100 " id="ColBirthdate">Birthdate :</div>
                    <div class="col-8 w-100 " id="DetailName">11/12/1111</div>
                </div>
            </div>
        </div>
        <!-- Reward -->
        <div class="col-12"
        style="background-color: #303344;
        margin-left: 24px;
        margin-right: 24px;
        margin-top: 20px;
        margin-bottom: 20px;
        border-radius:10px;
        height: 455px;
        width: 672px;">
        <!-- header Reward -->
            <div class="col-12 w-100" id="ColHeaderReward">
                <div class="row" 
                style="font-size:30px;
                height:45px;
                padding-top:5px;
                color: #FFFFFF;">
                    <div class="col-3 w-100" style="margin-left:21px;text-align:left;">Reward</div>
                    <div class="col-6 w-100"></div>
                    <div class="col-3 w-100" style="padding-right:0px;"><a href="http://localhost:8080/?#/promotion/redemption/allreward">See All</a></div>
                </div>
            </div>
            <div class="col-12 w-100" id="ColItemReward">
                <div class="row" style="position:relative;margin-top:15px;height:110;">
                    
                    <div class="BlockItem" id="BlockItem"></div>
                    <div></div>
                    <div class="BlockItem" id="BlockItem"></div>
                    <div></div>
                    <div class="BlockItem" id="BlockItem"></div>
                    <div></div>
                    <div class="BlockItem" id="BlockItem"></div>
                    <div></div>
                    <div class="BlockItem" id="BlockItem"></div>
                    
                </div>
            </div>            
        </div>
    </div>
</template>

<script>
export default {  
  name: "Redemption",
  components : {
      NavApp
  },
  data() {
      return{
        //   CustommerPhone : null,
      }
  },

};
import NavApp from "../../components/main_component/NavApp.vue"
</script>

<style scoped>

#DotPoint {
    height:64px;
    display:inline-block;
    padding:0px;
    text-align:right;
}

#DotName {
    height:50px;
    display:inline-block;
    padding:0px;
    text-align:right;
}

#ColPoint {
    height:64px;
    display:inline-block;
    text-align:left;
}

#ColName {
    height:50px;
    display:inline-block;
    text-align:left;
}

#ColBirthdate {
    height:50px;
    display:inline-block;
    padding:0px;
    text-align:right;
}

#DetailName {
    height:50px;
    display:inline-block;
    padding-left:10px;
    text-align:left;
}

#LinkHistory {
    height:64px;
    display:inline-block;
    line-height:0px;
    right:10px;
    font-size: 30px;
    text-align: left;
    position: relative;
    
}

#ColHeaderReward {
    height: 45px;
    margin-top: 10px;
}

#ColItemReward {
    height: 110px;
    margin-top: 15px;
}

#BlockItem {
    position: relative;
    display: inline-block;
    height: 100px;
    width: 100px;
    border-radius: 10px;
    margin: 5px;
    left: 25px;
    background-color: #717171;
}

</style>