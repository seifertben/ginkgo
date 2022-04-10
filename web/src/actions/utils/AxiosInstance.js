import axios from "axios";

const headers = {
    Pragma: "no-cache",
    "Access-Control-Allow-Origin": "*"
}

const url = "http://localhost:5000"

const instance = axios.create({
    baseURL: url,
    headers,
})

export default instance;