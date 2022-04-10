import React from "react";
import { Card } from 'antd';
import styled from "styled-components";

const StyledCard = styled(Card)`
    margin-top: 5vh
`

function SearchResults(props) {
    const { result } = props;

    return <StyledCard title={result.protein_name} bordered={false} style={{ width: 300 }}>
    <p>Match Start: {result.match_start}</p>
    <p>Match End: {result.match_end}</p>
    <a target="_blank" rel="noopener noreferrer" href={`https://www.ncbi.nlm.nih.gov/protein/${result.protein_id}`}>Protein ID: {result.protein_id}</a>
  </StyledCard>
;
}

export default SearchResults;