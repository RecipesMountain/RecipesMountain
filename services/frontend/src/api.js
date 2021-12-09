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

    return axios.post(`${APISUFFIX}/login/`, params);
  },
  async getUser(token, userID) {
    return axios.get(`${APISUFFIX}/user/${userID}`, authHeaders(token));
  },

  async getUsers(token) {
    return axios.get(`${APISUFFIX}/users`, authHeaders(token));
  },


};