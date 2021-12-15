import { createRouter, createWebHashHistory } from "vue-router";
import Login from "../views/User/Login.vue";
import Register from "../views/User/Register.vue";
<<<<<<< HEAD
import Test from '../views/Test.vue'
import UserStatus from '../views/User/UserStatus.vue'
=======
// import Test from '../views/Test.vue'
>>>>>>> 80b99c295871cdb70bc5cfa42e66f4a73521245d
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
    path: "/po_for_suppliers",
    name: "POForSuppliers",
    component: POForSuppliers,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/pickup_raw_material",
    name: "PickupRawMaterial",
    component: PickupRawMaterial,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/minimum",
    name: "Minimum",
    component: Minimum,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/manage_raw_material",
    name: "ManageRawMaterial",
    component: ManageRawMaterial,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/raw_materials",
    name: "RawMaterials",
    component: RawMaterials,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/add_raw_materials",
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
<<<<<<< HEAD
  {
    path: "/test",
    name: "Test",
    component: Test,
  },
  {
    path:'/user-status',
    name:'UserStatus',
    component: UserStatus,
  }
  
=======
  // {
  //   path: "/test",
  //   name: "Test",
  //   component: Test,
  // },
>>>>>>> 80b99c295871cdb70bc5cfa42e66f4a73521245d
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
