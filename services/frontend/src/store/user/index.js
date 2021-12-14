import { api } from '@/api';

const defaultState = {
    isLoggedIn: null,
    logInError: false,
    registrationError: false,
    registrationSuccess: false, 
    token: '',
    userID: null,
    username: null,
    isSuperUser: false,
    fullName: null,
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
        setFullName(state, payload) {
            state.fullName = payload;
        },
        setSuperUser(state, payload) {
            state.isSuperUser = payload;
        },
        setRegistrationError(state, payload) {
            state.registrationError = payload;
        },
        setRegistrationSuccess(state, payload) {
            state.registrationSuccess = payload;
        },

    },
    actions: {
        async actionLogIn(state, payload) {
            try {
                const response = await api.logIn(payload.username, payload.password)
                const token = response.data.access_token;
                if (token) {
                    saveLocalToken(token);
                    state.commit("setToken", token);
                    state.commit("setLoggedIn", true)
                    state.commit("setLogInError", false)
                    await state.dispatch("actionGetMe"); //! this can not work, got to check this
                } else {
                    await state.dispatch("actionLogOut");
                }
            } catch (err) {
                state.commit("setLogInError", true)
                console.log(err);
                await state.dispatch("actionLogOut");
            }
        },

        async actionGetMe(state) {
            try {
                const response = await api.getMe(state.state.token, state.state.userID)
                if (response.data) {
                    console.log(response.data)
                    state.commit("setUserID", response.data.id);
                    state.commit("setUsername", response.data.email);
                    state.commit("setFullName", response.data.full_name);
                    state.commit("setSuperUser", response.data.is_superuser);
                    console.log(state)
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
                        state.dispatch("actionGetMe");
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

        async actionRegister(state, payload) {
            try {
                const response = await api.createUserOpen(payload)
                if (response.status == 200) {
                    state.commit("setRegistrationError", false)
                    state.commit("setRegistrationSuccess", true)
                    console.log(response);
                } else {
                    state.commit("setRegistrationError", true)
                    state.commit("setRegistrationSuccess", false)
                    console.log(response);
                }
            } catch (err) {
                state.commit("setRegistrationError", true)
                state.commit("setRegistrationSuccess", false)
                console.log(err);
            }
        }
    },
    getters: {
        loginError: (state) => state.logInError,
        dashboardMiniDrawer: (state) => state.dashboardMiniDrawer,
        token: (state) => state.token,
        isLoggedIn: (state) => state.isLoggedIn,
        username: (state) => state.username,
        email: (state) => state.username,
        fullName: (state) => state.fullName,
    },
  };


const getLocalToken = () => localStorage.getItem('token');

const saveLocalToken = (token) => localStorage.setItem('token', token);

const removeLocalToken = () => localStorage.removeItem('token');