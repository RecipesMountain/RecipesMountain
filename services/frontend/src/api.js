import axios from 'axios';
import qs from 'qs';

function authHeaders(token) {
  return {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
}

function ImageHeaders(token) {
  return {
    headers: {
      Authorization: `Bearer ${token}`,
      "Content-Type": "multipart/form-data;"
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
    if (tags != null && tags != [])
      config.params["tags"] = tags
    if (keyword != null && keyword != "")
      config.params["keywords"] = keyword.replace(" ","+")
    if (sort != null)
      config.params["sort"] = sort
    config.params["tagsConnect"] = "and"
    config["paramsSerializer"] = (params) => {
      return qs.stringify(params, { arrayFormat: 'repeat' })
    }
    return axios.get(`${APISUFFIX}/api/recipes/search`, config)
  },
  async getTags() {
    return axios.get(`${APISUFFIX}/api/tags/`)
  },

  // new 
  async getProducts(){
    return axios.get(`${APISUFFIX}/api/products/`)
  },
  async getRecipe(id){
    return axios.get(`${APISUFFIX}/api/recipes/` + id)
  },
  async getRecipeImage(id){
    return axios.defaults.baseURL+`${APISUFFIX}api/recipes/img/` + id
  },
  async createRecipe(token, data){
    return axios.post(`${APISUFFIX}/api/recipes/`, data, authHeaders(token))
  },
  async sendImage(token, data, id){
    return axios.post(`${APISUFFIX}/api/recipes/img/`+ id, data, ImageHeaders(token))
  }
  

};