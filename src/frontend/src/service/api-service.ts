// source: https://github.com/codeforpdx/recordexpungPDX/tree/a978637d48971e42b42413c93aafb06b4880bcd4/src/frontend/src/service
import axios, { AxiosPromise, AxiosRequestConfig } from "axios";
export default function apiService<T>(
    dispatch: Function,
    request: AxiosRequestConfig
  ): AxiosPromise {
    return axios.request<T>(request).catch((error) => {
      return Promise.reject(error);
    });
  }