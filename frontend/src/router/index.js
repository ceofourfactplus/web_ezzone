import { createRouter, createWebHashHistory } from "vue-router";
import Login from "../views/User/Login.vue";
import Register from "../views/User/Register.vue";
import Test from '../views/Test.vue'
import UserStatus from '../views/User/UserStatus.vue'
import store from "../store";
// import Product from "../views/Product/Product.vue"
// import Topping from "../views/Product/Topping.vue"
// import TypeTopping from "../views/Product/TypeTopping.vue"
// import SaleChannel from "../views/Product/SaleChannel.vue"
// import SelectApp from "../views/Product/SelectApp.vue"
import RawMaterials from "../views/RawMaterials/RawMaterials.vue"
import AddRawMaterials from "../views/RawMaterials/AddRawMaterials.vue"
import Suppliers from "../views/RawMaterials/Suppliers.vue"
import POForSuppliers from "../views/RawMaterials/POForSuppliers.vue"
import PickupRawMaterial from "../views/RawMaterials/PickupRawMaterial.vue"
import Minimum from "../views/RawMaterials/Minimum.vue"
import ManageRawMaterial from "../views/RawMaterials/ManageRawMaterial.vue"
import EditUser from '../views/User/EditUser.vue'

const routes = [
  // {
  //   path: "/",
  //   name: "Home",
  //   component: Windows,
  //   meta: {
  //     requiresLogin: true,
  //   },
  // },
  {
    path: "/suppliers",
    name: "Suppliers",
    component: Suppliers,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/po-for-suppliers",
    name: "POForSuppliers",
    component: POForSuppliers,
  },
  {
    path: "/pickup-raw-material",
    name: "PickupRawMaterial",
    component: PickupRawMaterial, 
  },
  {
    path: "/minimum",
    name: "Minimum",
    component: Minimum,
  },
  {
    path: "/manage-raw-material",
    name: "ManageRawMaterial",
    component: ManageRawMaterial,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/raw-materials",
    name: "RawMaterials",
    component: RawMaterials,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/add-raw-materials",
    name: "AddRawMaterials",
    component: AddRawMaterials,
    meta: {
      requiresLogin: false,
    },
  },
  // {
  //   path: "/product",
  //   name: "MainCreate",
  //   component: MainCreate,
  //   meta: {
  //     requiresLogin: true,
  //   },
    // children: [
    //   {
    //     name: "Category",
    //     path: "/category",
    //     component: Category,
    //     params: {text:'category'}
    //   },{
    //     name: "Topping",
    //     path: "/topping",
    //     component: Topping,
    //     params: {text:'topping'}
    //   },{
    //     name: "Product",
    //     path: "/product",
    //     component: Product,
    //     params: {text:'product'}
    //   },{
    //     name: "SaleChannel",
    //     path: "/sale-channel",
    //     component: SaleChannel,
    //     params: {text:'sale-channel'}
    //   },{
    //     name: "TypeTopping",
    //     path: "/type-topping",
    //     component: TypeTopping,
    //     params: {text:'type-topping'}
    //   },
    //   { 
    //     name:"SelectApp",
    //     path:'/',
    //     component: SelectApp,
    //   }
    // ],
  // },
  // {
  //   path: "/stock",
  //   name: "MainStock",
  //   component: MainStock,
  //   meta: {
  //     requiresLogin: true,
  //   },
  //   children: [
  //     {
  //       name: "ToBuy",
  //       path: "/to-buy",
  //       component: ToBuy,
  //     },
  //     {
  //       name: "AllStock",
  //       path: "/all-stock",
  //       component: AllStock,
  //     },
  //   ],
  // },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
  {
    path: "/test",
    name: "Test",
    component: Test,
  },
  {
    path:'/user-status',
    name:'UserStatus',
    component: UserStatus,
  },
  {
    path:'/edit-user/:id',
    props: true,
    component: EditUser,
    name:'EditUser'
  }
  
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

router.beforeEach((to, form, next) => {
  if (to.matched.some((record) => record.meta.requiresLogin)) {
    if (!store.getters["auth/loggedIn"]) {
      next({ name: "Login" });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
