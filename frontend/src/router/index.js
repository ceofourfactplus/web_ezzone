import { createRouter, createWebHashHistory } from "vue-router";
import Login from "../views/User/Login.vue";
import Register from "../views/User/Register.vue";
import Test from '../views/Test.vue'
import UserStatus from '../views/User/UserStatus.vue'
import store from "../store";
const routes = [
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
