import React, { useState, useEffect } from "react";
import { Form, Input, Button, Modal } from 'antd';
import { blastSearch, getSearches } from "../actions/SearchActions";
import { Table } from 'antd';
import SearchResults from "./components/SearchResults";
import styled from "styled-components";
import moment from "moment";

const SearchContent = styled.div`
    padding: 5vh;
    padding-top: 10vh;
    width:100%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
`

const StyledTable = styled(Table)`
    width: 50%;
    margin-top: 2vh;
    .ant-table-row {
        cursor: pointer;
    }
`

function SearchContainer(props) {
    const [searchResult, setSearchResult] = useState(null);
    const [isModalVisible, setIsModalVisible] = useState(false);
    const [modalContent, setModalContent] = useState("");

    const [searchHistory, setSearchHistory] = useState([]);

    useEffect(() => {
        updateSearches();
    }, []);

    const updateSearches = () => {
        getSearches().then((searches) => {
            const sortedSearches = searches.sort((a, b) => {
                return new Date(a.create_dttm).getTime() -
                    new Date(b.create_dttm).getTime()
            }).reverse();

            setSearchHistory(sortedSearches);
        })
    }

    const onSubmit = (values) => {
        console.log('Received values from form: ', values);
        blastSearch(values.sequence).then((res) => {
            setSearchResult(res)
            updateSearches();
        })
    };


    const validateSequence = (_, sequence) => {
        if (sequence.length == 0) {
            return Promise.reject(new Error("Sequence cannot be empty."))
        }
        if (!/^[A,T,G,C,a,t,g,c]+$/.test(sequence)) {
            return Promise.reject(new Error("DNA sequences must contain only A, T, G, and C"))
        }
        return Promise.resolve();
    }

    const showModal = () => {
        setIsModalVisible(true);
    };

    const hideModal = () => {
        setIsModalVisible(false);
    };

    const columns = [
        {
            title: 'Search Date',
            dataIndex: 'created_dttm',
            key: 'created_dttm',
            width: "20%",
            render: (date) => moment(date).format('MM/DD/YY, h:mm:ss a')
        },
        {
            title: 'Search',
            dataIndex: 'search_string',
            key: 'search_string',
            render: (text) => getSearchText(text)
        }
    ];

    const getSearchText = (text) => {
        if (text.length > 50) {
            return <a onClick={() => {
                setModalContent(text);
                showModal();
            }}>{`${text.substring(0, 50)}...`}</a>
        }
        return text;
    }

    return (
        <SearchContent>
            <Form
                name="customized_form_controls"
                layout="inline"
                onFinish={onSubmit}
            >
                <Form.Item
                    name="sequence"
                    rules={[
                        {
                            validator: validateSequence,
                        },
                    ]}
                >
                    <Input style={{width: "75vw"}} />
                </Form.Item>
                <Form.Item>
                    <Button type="primary" htmlType="submit">
                        Search
                    </Button>
                </Form.Item>
            </Form>
            <StyledTable
                columns={columns}
                dataSource={searchHistory}
                onRow={(record) => ({
                    onClick: () => {
                        setSearchResult(record);
                    }
                })}
                scroll={{ y: 300 }}
                pagination={false}

            />
            <Modal title="Full Search Text" visible={isModalVisible} onOk={hideModal} onCancel={hideModal} style={{ top: "30vh" }}>
                <p>{modalContent}</p>
            </Modal>
            {searchResult && <SearchResults result={searchResult} />}
        </SearchContent>
    );
}

export default SearchContainer;