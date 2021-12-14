import axios from 'axios';

function authHeaders(token) {
  return {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
}

const APISUFFIX = ""

export const api = {
  async logIn(username, password) {
    const params = new URLSearchParams();
    params.append('username', username);
    params.append('password', password);

    return axios.post(`${APISUFFIX}/api/login/access-token`, params);
  },

  async getMe(token) {
    return axios.get(`${APISUFFIX}/api/users/me`, authHeaders(token));
  },
  async updateMe(token, data) {
    return axios.put(`${APISUFFIX}/api/users/me`, data, authHeaders(token));
  },
  async getUsers(token) {
    return axios.get(`${APISUFFIX}/api/users/`, authHeaders(token));
  },
  async updateUser(token, userId, data) {
    return axios.put(`${APISUFFIX}/api/users/${userId}`, data, authHeaders(token));
  },
  async createUser(token, data) {
    return axios.post(`${APISUFFIX}/api/users/`, data, authHeaders(token));
  },
  async passwordRecovery(email) {
    return axios.post(`${APISUFFIX}/api/password-recovery/${email}`);
  },
  async resetPassword(password, token) {
    return axios.post(`${APISUFFIX}/api/reset-password/`, {
      new_password: password,
      token,
    });
  },

};