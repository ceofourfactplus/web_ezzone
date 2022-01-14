<template>
    <div>
        <nav-app>All Reward</nav-app>
        <!-- Reward -->
        <div class="col-12"
        style="background-color: #303344;
        margin-left: 24px;
        margin-right: 24px;
        margin-top: 20px;
        margin-bottom: 20px;
        border-radius:20px;
        height: 820px;
        width: 672px;">
        <!-- header Reward -->
            <div class="col-12 w-100" id="ColHeaderReward">
                <div class="row" 
                style="font-size:30px;
                height50px;
                padding-top:10px;
                padding-bottom:10px;
                color: #FFFFFF;">
                    <div class="col-3 w-100" style="margin-left:22px;text-align:left;">Reward</div>
                    <div class="col-9 w-100"></div>
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
  name: "History",
  components : {
      NavApp
  },
  data() {
      return{
        
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
    height: 50px;
    margin-top: 10px;
}

#ColItemReward {
    height: 100%;
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