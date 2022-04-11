import axios from "axios";

const headers = {
    Pragma: "no-cache",
    "Access-Control-Allow-Origin": "*"
}

const host = window.location.origin;

let url = "https://ginkgo-demo-api.herokuapp.com"
if (host.includes("http://localhost")) {
    url = "http://localhost:5000"
}


const instance = axios.create({
    baseURL: url,
    headers,
})

export default instance;