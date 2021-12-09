import { api } from '@/api';

const defaultState = {
    isLoggedIn: null,
    token: '',
    userID: null,
    username: null,
    logInError: false,
  };
  
  export const userModule = {
    state: defaultState,
    mutations: {
        setToken(state, payload) {
            state.token = payload;
        },
        setUsername(state, payload) {
            state.username = payload
        },
        setUserID(state, payload) {
            state.userID = payload
        },
        setLoggedIn(state, payload) {
            state.isLoggedIn = payload;
        },
        setLogInError(state, payload) {
            state.logInError = payload;
        },
    },
    actions: {
        async actionLogIn(state, payload) {
            try {
                const response = await api.LogIn(payload)
                const token = response.data.access_token;
                if (token) {
                    saveLocalToken(token);
                    state.commit("setToken", token);
                    state.commit("setLoggedIn", true)
                    state.commit("setLoggedIn", false)
                    await state.dispatch("actionGetUser"); //! this can not work, got to check this
                } else {
                    await state.dispatch("actionLogOut");
                }
            } catch (err) {
                state.commit("setLoggedIn", true)
                await state.dispatch("actionLogOut");
            }
        },
        async actionGetUser(state) {
            try {
                const response = await api.getUser(state.state.token, state.state.userID)
                if (response.data) {
                    //TODO: SET USER DATA
                }
            } catch (error) {
                await state.dispatch("actionCheckApiError", error);
            }
        },
        async actionCheckLoggedIn(state) {
            if (!state.state.isLoggedIn) {
                let token = state.state.token;
                if (!token) {
                    const localToken = getLocalToken();
                    if (localToken) {
                        state.commit("setToken", localToken);
                        token = localToken;
                    }
                }
                if (token) {
                    try {
                        state.dispatch("actionGetUser");
                        state.commit("setLoggedIn", true)
                    } catch (error) {
                        await state.dispatch("actionLogOut");
                    }
                } else {
                    await state.dispatch("actionLogOut");
                }
            }
        },
        async actionLogOut(state) {
            removeLocalToken();
            state.commit("setToken", '');
            state.commit("setLoggedIn", false);
        },
        async actionCheckApiError(state, payload) {
            if (payload.response.status === 401) {
                await state.dispatch("actionLogOut");
            }
        },
    },
    getters: {
        loginError: (state) => state.logInError,
        dashboardMiniDrawer: (state) => state.dashboardMiniDrawer,
        token: (state) => state.token,
        isLoggedIn: (state) => state.isLoggedIn,
    },
  };


const getLocalToken = () => localStorage.getItem('token');

const saveLocalToken = (token) => localStorage.setItem('token', token);

const removeLocalToken = () => localStorage.removeItem('token');