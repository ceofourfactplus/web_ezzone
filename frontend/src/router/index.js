import { createRouter, createWebHashHistory } from "vue-router";
import Login from "../views/User/Login.vue";
import Register from "../views/User/Register.vue";
import Test from '../views/Test.vue'
import UserStatus from '../views/User/UserStatus.vue'
import store from "../store";
import RawMaterials from "../views/RawMaterials/RawMaterials.vue"
import AddRawMaterials from "../views/RawMaterials/AddRawMaterials.vue"
import Suppliers from "../views/RawMaterials/Suppliers.vue"
import POForSuppliers from "../views/RawMaterials/POForSuppliers.vue"
import PickupRawMaterial from "../views/RawMaterials/PickupRawMaterial.vue"
import Minimum from "../views/RawMaterials/Minimum.vue"
import ManageRawMaterial from "../views/RawMaterials/ManageRawMaterial.vue"
import EditUser from '../views/User/EditUser.vue'

const routes = [
  {
    path: "/suppliers",
    name: "Suppliers",
    component: Suppliers,
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
  },
  {
    path: "/raw-materials",
    name: "RawMaterials",
    component: RawMaterials,
  },
  {
    path: "/add-raw-materials",
    name: "AddRawMaterials",
    component: AddRawMaterials,
  },
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
