import { createRouter, createWebHashHistory } from "vue-router";
import POS from "../views/POS/POS.vue";
import Category from "../views/Product/Category.vue";
import MainCreate from "../views/Product/MainCreate.vue";
import MainStock from "../views/Stock/MainStock.vue";
import Login from "../views/User/Login.vue";
import Logout from "../views/User/Logout.vue";
import Windows from "../views/Windows.vue";
import Register from "../views/Register.vue";
import AllStock from "../views/Stock/AllStock.vue";
import ToBuy from "../views/Stock/ToBuy.vue"
import store from "../store";
import Product from "../views/Product/Product.vue"
import Topping from "../views/Product/Topping.vue"
import TypeTopping from "../views/Product/TypeTopping.vue"
import SaleChannel from "../views/Product/SaleChannel.vue"
import SelectApp from "../views/Product/SelectApp.vue"
const routes = [
  {
    path: "/",
    name: "Home",
    component: Windows,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/product",
    name: "MainCreate",
    component: MainCreate,
    meta: {
      requiresLogin: true,
    },
    children: [
      {
        name: "Category",
        path: "/category",
        component: Category,
        params: {text:'category'}
      },{
        name: "Topping",
        path: "/topping",
        component: Topping,
        params: {text:'topping'}
      },{
        name: "Product",
        path: "/product",
        component: Product,
        params: {text:'product'}
      },{
        name: "SaleChannel",
        path: "/sale-channel",
        component: SaleChannel,
        params: {text:'sale-channel'}
      },{
        name: "TypeTopping",
        path: "/type-topping",
        component: TypeTopping,
        params: {text:'type-topping'}
      },
      { 
        name:"SelectApp",
        path:'/',
        component: SelectApp,
      }
    ],
  },
  {
    path: "/stock",
    name: "MainStock",
    component: MainStock,
    meta: {
      requiresLogin: true,
    },
    children: [
      {
        name: "ToBuy",
        path: "/to-buy",
        component: ToBuy,
      },
      {
        name: "AllStock",
        path: "/all-stock",
        component: AllStock,
      },
    ],
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/logout",
    name: "Logout",
    component: Logout,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/pos",
    name: "POS",
    component: POS,
    meta: {
      requiresLogin: true,
    },
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
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
