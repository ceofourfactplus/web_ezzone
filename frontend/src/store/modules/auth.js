import axios from "axios";

export default {
  namespaced: true,
  state: {
    accessToken: null,
    confirm_pass: false,
    refreshToken: null,
    userInfo: "",
    error_login: {
      boolean: false,
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
    userLogin(context, usercredentials) {
      return axios
        .post("http://127.0.0.1:8000/auth/is-active/", {
          username: usercredentials.username,
          password: usercredentials.password,
        })
        .then(() => {
          return axios
            .post("http://127.0.0.1:8000/api-token/", {
              username: usercredentials.username,
              password: usercredentials.password,
            })
            .then((response) => {
              localStorage.setItem('username',usercredentials.username)
              localStorage.setItem('password',usercredentials.password)
              console.log("2");
              context.commit("newToken", {
                access: response.data.access,
                refresh: response.data.refresh,
              });
              const headers = {
                headers: {
                  Authorization: `Bearer ${response.data.access}`,
                },
              };

              axios
                .get("http://127.0.0.1:8000/auth/user-info/", headers)
                .then((response) => {
                  context.commit("updateUserInfo", {
                    userInfo: response.data,
                  });
                });
            });
        })
        .catch((error) => {
          context.state.error_login.text = error;
          context.state.error_login.boolean = true;
        });
    },
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
