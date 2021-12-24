import { createRouter, createWebHashHistory } from "vue-router";
import Login from "../views/User/Login.vue";
import Register from "../views/User/Register.vue";
import new2 from "../views/test/new.vue";
import UserStatus from "../views/User/UserStatus.vue";
import store from "../store";
import RawMaterials from "../views/RawMaterials/RM.vue";
import CreateRM from "../views/RawMaterials/CreateRM.vue";
import EditRM from "../views/RawMaterials/EditRM.vue";
import PickupList from "../views/RawMaterials/PickupList.vue";
import Supplier from "../views/RawMaterials/Supplier.vue"
import CreateSupplier from "../views/RawMaterials/CreateSup.vue"

// import POForSuppliers from "../views/RawMaterials/POForSuppliers.vue"
import PickupRawMaterial from "../views/RawMaterials/PickupRawMaterial.vue";
import PO from "../views/RawMaterials/PO.vue";
import PONotice from "../views/RawMaterials/PONotice.vue";
import EditUser from "../views/User/EditUser.vue";
import DashBoard from "../views/DashBoard.vue";
import ForgotPassword from "../views/User/ForgotPassword.vue";
import Customer from "../views/Customer/Customer.vue";
import CreateCustomer from "../views/Customer/CreateCustomer.vue";
import EditCustomer from "../views/Customer/EditCustomer.vue";
import Products from "../views/Product/Products.vue";
import CreateProduct from "../views/Product/CreateProduct.vue";
import ProductCategory from "../views/Product/ProductCategory.vue";
import RawMaterialCategory from "../views/RawMaterials/RMCategory.vue";
import RMUnit from "../views/RawMaterials/UnitRM.vue";
import EditSupplier from '../views/RawMaterials/EditSup.vue'

const routes = [
  {
    path: "/rm/po-notice",
    name: "PONotice",
    component: PONotice,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/rm/pickup-list",
    name: "PickupList",
    component: PickupList,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/rm/edit-rm",
    name: "EditRM",
    component: EditRM,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/raw-material-category",
    name: "RawMaterialCategory",
    component: RawMaterialCategory,
    meta: {
      requiresLogin: false,
    },
  },
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
    path: "/rm/create-rm",
    name: "CreateRM",
    component: CreateRM,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/pickup-raw-material",
    name: "PickupRawMaterial",
    component: PickupRawMaterial,
  },
  // {
  //   path: "/minimum",
  //   name: "Minimum",
  //   component: Minimum,
  // },
  // {
  //   path: "/manage-raw-material",
  //   name: "ManageRawMaterial",
  //   component: ManageRawMaterial,
  // },
  {
    path: "/rm/raw-materials",
    name: "RawMaterials",
    component: RawMaterials,
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
    component: new2,
  },
  {
    path: "/user-status",
    name: "UserStatus",
    component: UserStatus,
  },
  {
    path: "/edit-user/:id",
    props: true,
    component: EditUser,
    name: "EditUser",
  },
  {
    path: "/customer",
    props: true,
    component: Customer,
    name: "Customer",
  },
  {
    path: "/create-customer",
    props: true,
    component: CreateCustomer,
    name: "CreateCustomer",
  },
  {
    path: "/edit-customer/:id",
    props: true,
    component: EditCustomer,
    name: "EditCustomer",
  },
  {
    path: "/rm/po-notic",
    name: "PO",
    component: PO,
  },
  {
    path: "/rm/unit",
    component: RMUnit,
    name:"RMUnit"
  },
  {
    path:'/rm/supplier',
    name:'Supplier',
    component:Supplier
  },
  {
    path:'/rm/supplier/create',
    name:'CreateSupplier',
    component:CreateSupplier
  },
  {
    path:'/rm/supplier/edit/:id',
    props:true,
    name:'EditSupplier',
    component:EditSupplier
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
