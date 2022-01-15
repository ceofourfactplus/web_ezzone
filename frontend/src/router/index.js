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
import EditProduct from "../views/Product/EditProduct.vue";
import ProductCategory from "../views/Product/ProductCategory.vue";

// topping
import Topping from "../views/Topping/Topping.vue";
import CreateTopping from "../views/Topping/CreateTopping.vue";
import EditTopping from "../views/Topping/EditTopping.vue";
import ToppingCategory from "../views/Topping/ToppingCategory.vue";
import CreateCategoryTopping from "../views/Topping/CreateCategory.vue";
import EditCategoryTopping from "../views/Topping/EditCategory.vue";

// dash board
import DashBoard from "../views/DashBoard.vue";

// sale channel
import SaleChannel from "../views/SaleChannel/SaleChannel.vue";
import EditSaleChannel from "../views/SaleChannel/EditSaleChannel.vue";
import CreateSaleChannel from "../views/SaleChannel/CreateSaleChannel.vue";

// pos
import SelectSaleChannel from "../views/POS/SelectSaleChannel.vue";
import KeyOrder from "../views/POS/KeyOrder.vue";
import KeyProductDetail from "../views/POS/KeyProductDetail.vue";
import KeyToppingDetail from "../views/POS/KeyToppingDetail.vue";
import OrderReceipt from "../views/POS/OrderReceipt.vue";

// database settings
import DataBaseSettings from "../views/DataBaseSettings/DataBaseSettings.vue";

// Order Manage
import OrderDetail from "../views/OrderManage/OrderDetail.vue";
import FoodOrder from "../views/OrderManage/FoodOrder.vue";
import DrinkOrder from "../views/OrderManage/DrinkOrder.vue";

// promotion
import Point from "../views/Promotion/Point.vue"
import NewPoint from "../views/Promotion/NewPoint.vue"
import NewVoucher from "../views/Promotion/NewVoucher.vue"
import NewPackage from "../views/Promotion/NewPackage.vue"
import NewReward from "../views/Promotion/NewReward.vue"
import PackageDetail from "../views/Promotion/PackageDetail.vue"
import RewardDetail from "../views/Promotion/RewardDetail.vue"
import PointDetail from "../views/Promotion/PointDetail.vue"
import VoucherDetail from "../views/Promotion/VoucherDetail.vue"
import Redemption from "../views/Promotion/Redemption.vue"
import History from "../views/Promotion/History.vue"
import AllReward from "../views/Promotion/AllReward.vue"
import DetailReward from "../views/Promotion/DetailReward.vue"
import PreOrderReward from "../views/Promotion/PreOrderReward.vue"

// Report
import MainReport from '../views/Report/MainReport.vue'

import Chart1 from "../views/TestChart/Chart1.vue";
import FaceLogin from "../views/FaceDetector/LoginFace.vue";

const routes = [
  {
    path: "/face-login/",
    name: "FaceLogin",
    component: FaceLogin,
  },
  {
    path: "/chart",
    name: "Chart1",
    component: Chart1,
  },
  // Report
  {
    path: "/report",
    name: "MainReport",
    component: MainReport
  },
  // Order manage

  {
    path: "/order-manage/order-detail",
    name: "OrderDetail",
    component: OrderDetail,
  },
  {
    path: "/order-manage/food-order",
    name: "FoodOrder",
    component: FoodOrder,
  },
  {
    path: "/order-manage/drink-order",
    name: "DrinkOrder",
    component: DrinkOrder,
  },

  // promotion
  {
    path: "/promotion/redemption",
    name: "Redemption",
    component: Redemption,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/promotion/reward-detail/:id",
    name: "RewardDetail",
    component: RewardDetail,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/promotion/package-detail/:id",
    name: "PackageDetail",
    component: PackageDetail,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/promotion/voucher-detail/:id",
    name: "VoucherDetail",
    component: VoucherDetail,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/promotion/point-detail/:id",
    name: "PointDetail",
    component: PointDetail,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/promotion/point",
    name: "Point",
    component: Point,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/promotion/new-promotion",
    name: "NewPoint",
    component: NewPoint,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/promotion/new-voucher",
    name: "NewVoucher",
    component: NewVoucher,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/promotion/new-package",
    name: "NewPackage",
    component: NewPackage,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/promotion/new-reward",
    name: "NewReward",
    component: NewReward,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/promotion/redemption",
    name: "Redemption",
    component: Redemption,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/promotion/redemption/history",
    name: "History",
    component: History,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/promotion/redemption/allreward",
    name: "AllReward",
    component: AllReward,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/promotion/redemption/detailreward",
    name: "DetailReward",
    component: DetailReward,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/promotion/redemption/preorderreward",
    name: "PreOrderReward",
    component: PreOrderReward,
    meta: {
      requiresLogin: false,
    },
  },
  
  // database settings
  {
    path: "/dbs/dbs",
    name: "DataBaseSettings",
    component: DataBaseSettings,
    meta: {
      requiresLogin: false,
    },
  },

  // pos
  {
    path: "/pos/select-sale-channel",
    name: "SelectSaleChannel",
    component: SelectSaleChannel,
  },
  {
    path: "/pos/key-order",
    name: "KeyOrder",
    component: KeyOrder,
  },
  {
    path: "/pos/key-order/:product_id/key-product-detail",
    name: "KeyProductDetail",
    component: KeyProductDetail,
    props: true,
  },
  {
    path: "/pos/key-order/:topping_id/key-topping-detail",
    name: "KeyToppingDetail",
    component: KeyToppingDetail,
    props: true,
  },
  {
    path: "/pos/order-receipt",
    name: "OrderReceipt",
    component: OrderReceipt,
  },

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
    path: "/product/edit-product/:id",
    props: true,
    name: "EditProduct",
    component: EditProduct,
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

  // topping
  {
    path: "/topping/category",
    name: "ToppingCategory",
    component: ToppingCategory,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/topping/category/create",
    name: "CreateCategoryTopping",
    component: CreateCategoryTopping,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/topping/category/edit/:id",
    props: true,
    name: "EditCategoryTopping",
    component: EditCategoryTopping,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/topping/create",
    name: "CreateTopping",
    component: CreateTopping,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/topping/edit/:id",
    props: true,
    name: "EditTopping",
    component: EditTopping,
    meta: {
      requiresLogin: false,
    },
  },
  {
    path: "/topping",
    name: "Topping",
    component: Topping,
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
    component: SaleChannel,
  },
  {
    path: "/sale-channel/create",
    name: "CreateSaleChannel",
    component: CreateSaleChannel,
  },
  {
    path: "/sale-channel/edit/:id",
    name: "EditSaleChannel",
    props: true,
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
