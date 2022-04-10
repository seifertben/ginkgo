import instance from "./utils/AxiosInstance";

export const blastSearch = (sequence) => {
    return instance.get("/protein", {
        params: {
            seq: sequence
        }
    }).then((res) => {
        return res.data;
    })
}

export const getSearches = (sequence) => {
    return instance.get("/searches").then((res) => {
        return res.data;
    })
}