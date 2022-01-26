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
import KeyPromotionDetail from "../views/POS/KeyPromotionDetail.vue";
import OrderReceipt from "../views/POS/OrderReceipt.vue";

// database settings
import DataBaseSettings from "../views/DataBaseSettings/DataBaseSettings.vue";

// Order Manage
import OrderDetail from "../views/OrderManage/OrderDetail.vue";
import FoodOrder from "../views/OrderManage/FoodOrder.vue";
import DrinkOrder from "../views/OrderManage/DrinkOrder.vue";

// promotion
import Promotion from "../views/Promotion/Promotion.vue";
import NewPoint from "../views/Promotion/NewPoint.vue";
import NewVoucher from "../views/Promotion/NewVoucher.vue";
import NewPackage from "../views/Promotion/NewPackage.vue";
import NewReward from "../views/Promotion/NewReward.vue";
import PointDetail from "../views/Promotion/PointDetail.vue";
import VoucherDetail from "../views/Promotion/VoucherDetail.vue";
import PackageDetail from "../views/Promotion/PackageDetail.vue";
import Redemption from "../views/Promotion/Redemption.vue";
import History from "../views/Promotion/History.vue";
import AllReward from "../views/Promotion/AllReward.vue";
import PreOrderReward from "../views/Promotion/PreOrderReward.vue";
import RewardDetail from "../views/Promotion/RewardDetail.vue";
import RewardName from "../views/Promotion/RewardName.vue";

// Consignment
import Consigner from "../views/Consignment/Consigner.vue";
import ConsignerProduct from "../views/Consignment/ConsignerProduct.vue";
import RecordProduct from "../views/Consignment/RecordProduct.vue";
import NewConsignment from "../views/Consignment/NewConsignment.vue";
import NewConsigner from "../views/Consignment/NewConsigner.vue";
import PayShare from "../views/Consignment/PayShare.vue";
import SharePayment from "../components/consignment/SharePayment.vue";
import OutConsignment from "../components/consignment/OutConsignment.vue";
import AddConsignment from "../components/consignment/AddConsignment.vue";

// Home
import Home from "../views/Test.vue";

// Report
import MainReport from "../views/Report/MainReport.vue";
import SelectReport from "../views/Report/SelectReport.vue";
import ProductReportDetail from "../views/Report/ProductReportDetail.vue";
import ProductReport from "../views/Report/ProductReport.vue";

import Chart1 from "../views/TestChart/Chart1.vue";
import FaceLogin from "../views/FaceDetector/LoginFace.vue";
import Payment from "../views/Payment/Payment.vue";

// Components
import ProductQty from "../components/product/ProductQty.vue";

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
    path: "/report/:type",
    props: true,
    name: "MainReport",
    component: MainReport,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/select-report",
    name: "SelectReport",
    component: SelectReport,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/product-report",
    name: "ProductReport",
    component: ProductReport,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/report/product/:type",
    props: true,
    name: "ProductReportDetail",
    component: ProductReportDetail,
    meta: {
      requiresLogin: true,
    },
  },
  // Order manage

  {
    path: "/order-manage/order-detail",
    name: "OrderDetail",
    component: OrderDetail,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/order-manage/food-order",
    name: "FoodOrder",
    component: FoodOrder,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/order-manage/drink-order",
    name: "DrinkOrder",
    component: DrinkOrder,
    meta: {
      requiresLogin: true,
    },
  },

  // promotion
  {
    path: "/promotion",
    name: "Promotion",
    component: Promotion,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/promotion/redemption",
    name: "Redemption",
    component: Redemption,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/promotion/reward-detail/:id",
    name: "RewardDetail",
    component: RewardDetail,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/promotion/package-detail/:id",
    name: "PackageDetail",
    component: PackageDetail,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/promotion/voucher-detail/:id",
    name: "VoucherDetail",
    component: VoucherDetail,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/promotion/point-detail/:id",
    name: "PointDetail",
    component: PointDetail,
    meta: {
      requiresLogin: true,
    },
  },

  {
    path: "/promotion/new-promotion",
    name: "NewPoint",
    component: NewPoint,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/promotion/new-voucher",
    name: "NewVoucher",
    component: NewVoucher,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/promotion/new-package",
    name: "NewPackage",
    component: NewPackage,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/promotion/new-reward",
    name: "NewReward",
    component: NewReward,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/promotion/redemption",
    name: "Redemption",
    component: Redemption,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/promotion/redemption/history",
    name: "History",
    component: History,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/promotion/redemption/allreward",
    name: "AllReward",
    component: AllReward,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/promotion/redemption/preorderreward",
    name: "PreOrderReward",
    component: PreOrderReward,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/promotion/redemption/rewardname",
    name: "RewardName",
    component: RewardName,
    meta: {
      requiresLogin: true,
    },
  },

  // database settings
  {
    path: "/dbs/dbs",
    name: "DataBaseSettings",
    component: DataBaseSettings,
    meta: {
      requiresLogin: true,
    },
  },

  // pos
  {
    path: "/pos/select-sale-channel",
    name: "SelectSaleChannel",
    component: SelectSaleChannel,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/pos/key-order",
    name: "KeyOrder",
    component: KeyOrder,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/pos/key-order/:product_id/key-product-detail",
    name: "KeyProductDetail",
    component: KeyProductDetail,
    props: true,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/pos/key-order/:package_id/key-promotion-detail",
    name: "KeyPromotionDetail",
    component: KeyPromotionDetail,
    props: true,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/pos/key-order/:topping_id/key-topping-detail",
    name: "KeyToppingDetail",
    component: KeyToppingDetail,
    props: true,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/pos/order-receipt",
    name: "OrderReceipt",
    component: OrderReceipt,
    meta: {
      requiresLogin: true,
    },
  },

  // product
  {
    path: "/product/category",
    name: "ProductCategory",
    component: ProductCategory,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/product/create-product",
    name: "CreateProduct",
    component: CreateProduct,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/product/edit-product/:id",
    props: true,
    name: "EditProduct",
    component: EditProduct,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/product/product-qty",
    name: "ProductQty",
    component: ProductQty,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/product",
    name: "Product",
    component: Product,
    meta: {
      requiresLogin: true,
    },
  },

  // topping
  {
    path: "/topping/category",
    name: "ToppingCategory",
    component: ToppingCategory,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/topping/category/create",
    name: "CreateCategoryTopping",
    component: CreateCategoryTopping,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/topping/category/edit/:id",
    props: true,
    name: "EditCategoryTopping",
    component: EditCategoryTopping,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/topping/create",
    name: "CreateTopping",
    component: CreateTopping,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/topping/edit/:id",
    props: true,
    name: "EditTopping",
    component: EditTopping,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/topping",
    name: "Topping",
    component: Topping,
    meta: {
      requiresLogin: true,
    },
  },

  // dash board
  {
    path: "/dash-board",
    name: "DashBoard",
    component: DashBoard,
    meta: {
      requiresLogin: true,
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
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/user/edit/:id",
    props: true,
    component: EditUser,
    name: "EditUser",
    meta: {
      requiresLogin: true,
    },
  },

  // customer
  {
    path: "/customer",
    props: true,
    component: Customer,
    name: "Customer",
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/customer/create",
    props: true,
    component: CreateCustomer,
    name: "CreateCustomer",
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/customer/edit/:id",
    props: true,
    component: EditCustomer,
    name: "EditCustomer",
    meta: {
      requiresLogin: true,
    },
  },

  // raw material
  {
    path: "/rm/unit",
    component: RMUnit,
    name: "RMUnit",
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/rm/pickup-list",
    name: "PickupList",
    component: PickupList,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/rm/edit/:id",
    name: "EditRM",
    component: EditRM,
    props: true,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/rm/category",
    name: "RawMaterialCategory",
    component: RawMaterialCategory,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/rm/create-rm",
    name: "CreateRM",
    component: CreateRM,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/rm/raw-materials",
    name: "RawMaterials",
    component: RawMaterials,
    meta: {
      requiresLogin: true,
    },
  },

  // supplier
  {
    path: "/rm/supplier",
    name: "Supplier",
    component: Supplier,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/rm/supplier/create",
    name: "CreateSupplier",
    component: CreateSupplier,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/rm/supplier/edit/:id",
    props: true,
    name: "EditSupplier",
    component: EditSupplier,
    meta: {
      requiresLogin: true,
    },
  },

  // po
  {
    path: "/rm/po-notice",
    name: "PONotice",
    component: PONotice,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/rm/po",
    name: "PO",
    component: PO,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/rm/confirm-po",
    name: "ConfirmPO",
    component: ConfirmPO,
    meta: {
      requiresLogin: true,
    },
  },

  // sale channel
  {
    path: "/sale-channel",
    name: "SaleChannel",
    component: SaleChannel,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/sale-channel/create",
    name: "CreateSaleChannel",
    component: CreateSaleChannel,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/sale-channel/edit/:id",
    name: "EditSaleChannel",
    props: true,
    component: EditSaleChannel,
    meta: {
      requiresLogin: true,
    },
  },
  // sale channel
  {
    path: "/sale-channel",
    name: "SaleChannel",
    component: SaleChannel,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/sale-channel/create",
    name: "CreateSaleChannel",
    component: CreateSaleChannel,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/sale-channel/edit/:id",
    name: "EditSaleChannel",
    props: true,
    component: EditSaleChannel,
    meta: {
      requiresLogin: true,
    },
  },

  // Consingment
  {
    path: "/consignment/consigner",
    name: "Consigner",
    props: true,
    component: Consigner,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/consignment/consignerproduct",
    name: "ConsignerProduct",
    props: true,
    component: ConsignerProduct,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/consignment/recordproduct",
    name: "RecordProduct",
    props: true,
    component: RecordProduct,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/consignment/newconsignment",
    name: "NewConsignment",
    props: true,
    component: NewConsignment,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/payments",
    name: "Payments",
    component: Payment,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/consignment/newconsigner",
    name: "NewConsigner",
    props: true,
    component: NewConsigner,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/consignment/payshare",
    name: "PayShare",
    props: true,
    component: PayShare,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/consignment/sharepayment",
    name: "SharePayment",
    props: true,
    component: SharePayment,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/consignment/outconsignment",
    name: "OutConsignment",
    props: true,
    component: OutConsignment,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/consignment/addconsignment",
    name: "AddConsignment",
    props: true,
    component: AddConsignment,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/sale-channel",
    name: "SaleChannel",
    component: SaleChannel,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/sale-channel/create",
    name: "CreateSaleChannel",
    component: CreateSaleChannel,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/sale-channel/edit/:id",
    name: "EditSaleChannel",
    props: true,
    component: EditSaleChannel,
    meta: {
      requiresLogin: true,
    },
  },

  // Consingment
  {
    path: "/consignment/consigner",
    name: "Consigner",
    props: true,
    component: Consigner,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/consignment/consignerproduct",
    name: "ConsignerProduct",
    props: true,
    component: ConsignerProduct,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/consignment/newconsignment",
    name: "NewConsignment",
    props: true,
    component: NewConsignment,
    meta: {
      requiresLogin: true,
    },
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
