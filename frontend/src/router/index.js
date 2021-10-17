import { createRouter, createWebHashHistory } from "vue-router";
import POS from "../views/POS/POS.vue";
import Category from "../views/Product/Category.vue";
import MainCreate from "../views/Product/MainCreate.vue";
import Stock from "../views/Stock/Stock.vue";
import Login from "../views/Login.vue";
import Logout from "../views/Logout.vue";
import Windows from "../views/Windows.vue";
import Register from "../views/Register.vue";
import store from "../store";
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
        name: "Categpry",
        path: "/category",
        component: Category,
      },
    ],
  },
  {
    path: "/stock",
    name: "Stock",
    component: Stock,
    meta: {
      requiresLogin: true,
    },
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
    if (!store.getters['auth/loggedIn']) {
      next({ name: "Login" });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
