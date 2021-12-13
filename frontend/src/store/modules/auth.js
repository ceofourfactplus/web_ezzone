import axios from "axios";
export default {
  namespaced: true,
  state: {
    accessToken: null,
    confirm_pass: false,
    refreshToken: null,
    userInfo: "",
    error: {
      status: false,
      text: "",
    },
  },
  mutations: {
    destroyToken(state) {
      localStorage.removeItem('username')
      localStorage.removeItem('password')
      state.accessToken = null;
      state.refreshToken = null;
    },
    newToken(state, { access, refresh }) {
      state.accessToken = access;
      state.refreshToken = refresh;
    },
    check_pass(state, bo) {
      state.check_pass = bo;
    },
    updateUserInfo(state, { userInfo }) {
      state.userInfo = userInfo;
    },
  },
  actions: {
    userLogout(context) {
      if (context.getters.loggedIn) {
        context.commit("destroyToken");
      }
    },
    confirm_pass_f(context, password) {
      axios
        .post("http://127.0.0.1:8000/auth/conf-pas/", {
          password: password,
          id: context.state.userInfo.id,
        })
        .then(() => {
          context.commit("check_pass", true);
          return "success";
        })
        .catch(() => {
          context.commit("check_pass", false);
          return "password incorrect";
        });
    },
  },
  getters: {
    userInfo(state) {
      return state.userInfo;
    },
    loggedIn(state) {
      return state.accessToken != null;
    },
    error_login(state) {
      return state.error_login;
    },
  },
};
