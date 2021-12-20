import { createRouter, createWebHashHistory } from "vue-router";
import Login from "../views/User/Login.vue";
import Register from "../views/User/Register.vue";
import Test from '../views/Test.vue'
import UserStatus from '../views/User/UserStatus.vue'
import store from "../store";
import RawMaterials from "../views/RawMaterials/RawMaterials.vue"
import AddNewRM from "../views/RawMaterials/AddNewRM.vue"
import AddRawMaterials from "../views/RawMaterials/AddRawMaterials.vue"
import Suppliers from "../views/RawMaterials/Suppliers.vue"
import POForSuppliers from "../views/RawMaterials/POForSuppliers.vue"
import PickupRawMaterial from "../views/RawMaterials/PickupRawMaterial.vue"
import Minimum from "../views/RawMaterials/Minimum.vue"
import ManageRawMaterial from "../views/RawMaterials/ManageRawMaterial.vue"
import EditUser from '../views/User/EditUser.vue'
import DashBoard from '../views/DashBoard.vue'
import ForgotPassword from '../views/User/ForgotPassword.vue'
import Customer from '../views/Customer/Customer.vue'
import CreateCustomer from '../views/Customer/CreateCustomer.vue'
import EditCustomer from '../views/Customer/EditCustomer.vue'
import Products from '../views/Product/Products.vue'
import CreateProduct from '../views/Product/CreateProduct.vue'
import ProductCategory from '../views/Product/ProductCategory.vue'



const routes = [
  {
    path: "/product-category",
    name: "ProductCategory",
    component: ProductCategory,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/create-product/",
    name: "CreateProduct",
    component: CreateProduct,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/products",
    name: "Products",
    component: Products,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/dash-board",
    name: "DashBoard",
    component: DashBoard,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/add-new-rm",
    name: "AddNewRM",
    component: AddNewRM,
    meta: {
      requiresLogin: false,
    },
  },
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
    path: "/forgot-password",
    name: "ForgotPassword",
    component: ForgotPassword,
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
  },
  {
    path:'/customer',
    props: true,
    component: Customer,
    name:'Customer'
  },
  {
    path:'/create-customer',
    props: true,
    component: CreateCustomer,
    name:'CreateCustomer'
  },
  {
    path:'/edit-customer/:id',
    props: true,
    component: EditCustomer,
    name:'EditCustomer'
  }, 
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
