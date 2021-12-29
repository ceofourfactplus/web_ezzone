import { createRouter, createWebHashHistory } from "vue-router";
import store from "../store";

// user
import Login from "../views/User/Login.vue";
import Register from "../views/User/Register.vue";
import UserStatus from "../views/User/UserStatus.vue";
import EditUser from "../views/User/EditUser.vue";
import ForgotPassword from "../views/User/ForgotPassword.vue";

// raw material
import RawMaterials from "../views/RawMaterials/RM.vue";
import CreateRM from "../views/RawMaterials/CreateRM.vue";
import EditRM from "../views/RawMaterials/EditRM.vue";
import PickupList from "../views/RawMaterials/PickupList.vue";
import RMUnit from "../views/RawMaterials/UnitRM.vue";
import PickupRawMaterial from "../views/RawMaterials/PickupRawMaterial.vue";
import RawMaterialCategory from "../views/RawMaterials/RMCategory.vue";

// supplier
import Supplier from "../views/RawMaterials/Supplier.vue";
import CreateSupplier from "../views/RawMaterials/CreateSup.vue";
import EditSupplier from "../views/RawMaterials/EditSup.vue";

// po
import PONotice from "../views/RawMaterials/PONotice.vue";
import PO from "../views/RawMaterials/PO.vue";
import ConfirmPO from "../views/RawMaterials/ConfirmPO.vue";

// customer
import Customer from "../views/Customer/Customer.vue";
import CreateCustomer from "../views/Customer/CreateCustomer.vue";
import EditCustomer from "../views/Customer/EditCustomer.vue";

// product
import Product from "../views/Product/Products.vue";
import CreateProduct from "../views/Product/CreateProduct.vue";
import ProductCategory from "../views/Product/ProductCategory.vue";

// dash board
import DashBoard from "../views/DashBoard.vue";

// sale channel
import SaleChannel from "../views/SaleChannel/SaleChannel.vue"
import EditSaleChannel from "../views/SaleChannel/EditSaleChannel.vue"
import CreateSaleChannel from "../views/SaleChannel/CreateSaleChannel.vue"

const routes = [
  // product
  {
    path: "/product/category",
    name: "ProductCategory",
    component: ProductCategory,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/product/create-product",
    name: "CreateProduct",
    component: CreateProduct,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/product",
    name: "Product",
    component: Product,
    meta: {
      requiresLogin: false,
    },
  },

  // dash board
  {
    path: "/dash-board",
    name: "DashBoard",
    component: DashBoard,
    meta: {
      requiresLogin: false,
    },
  },

  // user
  {
    path: "/user/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/user/forgot-password",
    name: "ForgotPassword",
    component: ForgotPassword,
  },
  {
    path: "/user/register",
    name: "Register",
    component: Register,
  },
  {
    path: "/user/status",
    name: "UserStatus",
    component: UserStatus,
  },
  {
    path: "/user/edit/:id",
    props: true,
    component: EditUser,
    name: "EditUser",
  },

  // customer
  {
    path: "/customer",
    props: true,
    component: Customer,
    name: "Customer",
  },
  {
    path: "/customer/create",
    props: true,
    component: CreateCustomer,
    name: "CreateCustomer",
  },
  {
    path: "/customer/edit/:id",
    props: true,
    component: EditCustomer,
    name: "EditCustomer",
  },

  // raw material
  {
    path: "/rm/unit",
    component: RMUnit,
    name: "RMUnit",
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
    path: "/rm/edit/:id",
    name: "EditRM",
    component: EditRM,
    props: true,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/rm/category",
    name: "RawMaterialCategory",
    component: RawMaterialCategory,
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
    path: "/rm//pick-up",
    name: "PickupRawMaterial",
    component: PickupRawMaterial,
  },
  {
    path: "/rm/raw-materials",
    name: "RawMaterials",
    component: RawMaterials,
  },

  // supplier
  {
    path: "/rm/supplier",
    name: "Supplier",
    component: Supplier,
  },
  {
    path: "/rm/supplier/create",
    name: "CreateSupplier",
    component: CreateSupplier,
  },
  {
    path: "/rm/supplier/edit/:id",
    props: true,
    name: "EditSupplier",
    component: EditSupplier,
  },

  // po
  {
    path: "/rm/po-notice",
    name: "PONotice",
    component: PONotice,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/rm/po",
    name: "PO",
    component: PO,
  },
  {
    path: "/rm/confirm-po",
    name: "ConfirmPO",
    component: ConfirmPO,
  },

  // sale channel
  {
    path: "/sale-channel",
    name: "SaleChannel",
    component:  SaleChannel,
  },
  {
    path: "/sale-channel/create",
    name: "CreateSaleChannel",
    component: CreateSaleChannel,
  },
  {
    path: "/sale-channel/edit",
    name: "EditSaleChannel",
    component: EditSaleChannel,
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
