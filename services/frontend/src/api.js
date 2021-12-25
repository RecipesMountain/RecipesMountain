import axios from 'axios';

function authHeaders(token) {
  return {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
}

function basicConfig(token, skip, limit) {
  let config = authHeaders(token);
  config["params"] = {}
  config.params["skip"] = skip
  config.params["limit"] = limit
  return config
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
  async createUserOpen(data) {
    return axios.post(`${APISUFFIX}/api/users/open`, data);
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
  async getPopular(token, skip, limit){
    return axios.get(`${APISUFFIX}/api/recipes/popular`, basicConfig(token, skip, limit))
  },
  async getBest(token, skip, limit){
    return axios.get(`${APISUFFIX}/api/recipes/best`, basicConfig(token, skip, limit))
  },
  async search(token, keyword, tags, sort, skip, limit){
    let config = basicConfig(token, skip, limit)
    if (tags != null)
      config.params["tags"] = tags
    if (keyword != null && keyword != "")
      config.params["keywords"] = keyword
    if (sort != null)
      config.params["sort"] = sort
    config.params["tagsConnect"] = "and"
    return axios.get(`${APISUFFIX}/api/recipes/search`, config)
  },

};