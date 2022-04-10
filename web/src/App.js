import SearchContainer from "./pages/SearchContainer";
import { Layout } from 'antd';
import 'antd/dist/antd.css';
import './App.css';
import styled from "styled-components";

const HeaderTitle = styled.h1`
  color: white;
`

const { Header, Footer, Sider, Content } = Layout;

function App() {
  return (
    <div className="App">
          <Layout style={{height: "100vh"}}>
            <Header><HeaderTitle>
              FastBlast
              </HeaderTitle></Header>
            <Content>      
              <SearchContainer />
            </Content>
            <Footer>Ben Seifert 2022</Footer>
          </Layout>
    </div>
  );
}

export default App;
