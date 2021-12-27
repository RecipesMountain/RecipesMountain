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
            state.isSuperUser = payload
        },
        setRegistrationError(state, payload) {
            state.registrationError = payload;
        },
        setRegistrationSuccess(state, payload) {
            state.registrationSuccess = payload;
        },

    },
    actions: {
        async actionLogIn(context, payload) {
            try {
                const response = await api.logIn(payload.username, payload.password)
                const token = response.data.access_token;
                if (token) {
                    saveLocalToken(token);
                    context.commit("setToken", token);
                    context.commit("setLoggedIn", true)
                    context.commit("setLogInError", false)
                    await context.dispatch("actionGetMe"); //! this can not work, got to check this
                } else {
                    await context.dispatch("actionLogOut");
                }
            } catch (err) {
                context.commit("setLoggedIn", false)
                context.commit("setLogInError", true)
                await context.dispatch("actionLogOut");
            }
        },

        async actionGetMe(context) {
            try {
                const response = await api.getMe(context.state.token, context.state.userID)
                if (response.data) {
                    context.commit("setUserID", response.data.id);
                    context.commit("setUsername", response.data.email);
                    context.commit("setFullName", response.data.full_name);
                    context.commit("setSuperUser", response.data.is_superuser);
                }
            } catch (error) {
                await context.dispatch("actionCheckApiError", error);
            }
        },

        async actionCheckLoggedIn(context) {
            if (!context.state.isLoggedIn) {
                let token = context.state.token;
                if (!token) {
                    const localToken = getLocalToken();
                    if (localToken) {
                        context.commit("setToken", localToken);
                        token = localToken;
                    }
                }
                if (token) {
                    try {
                        await context.dispatch("actionGetMe");
                        context.commit("setLoggedIn", true)
                    } catch (error) {
                        await context.dispatch("actionLogOut");
                        context.commit("openSnackbar", "You're not logged in!")
                    }
                } else {
                    await context.dispatch("actionLogOut");
                    context.commit("openSnackbar", "You're not logged in!")
                }
            }
        },

        async actionLogOut(context) {
            removeLocalToken();
            context.commit("setToken", '');
            context.commit("setLoggedIn", false);
        },

        async actionCheckApiError(context, payload) {
            if (payload.response.status === 401) {
                await context.dispatch("actionLogOut");
                context.commit("openSnackbar", "Wrong credentials!")
            }
            if (payload.response.status === 403) {
                await context.dispatch("actionLogOut");
                context.commit("openSnackbar", "You're not logged in!")
            }
        },

        async actionRegister(context, payload) {
            try {
                const response = await api.createUserOpen(payload)
                if (response.status == 200) {
                    context.commit("setRegistrationError", false)
                    context.commit("setRegistrationSuccess", true)
                } else {
                    context.commit("setRegistrationError", true)
                    context.commit("setRegistrationSuccess", false)
                }
            } catch (err) {
                context.commit("setRegistrationError", true)
                context.commit("setRegistrationSuccess", false)
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
        registrationError: (state) => state.registrationError,
        registrationSuccess: (state) => state.registrationSuccess,
    },
  };


const getLocalToken = () => localStorage.getItem('token');

const saveLocalToken = (token) => localStorage.setItem('token', token);

const removeLocalToken = () => localStorage.removeItem('token');