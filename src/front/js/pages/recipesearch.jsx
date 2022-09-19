import React from "react";
import SearchBar from "../component/searchbar.jsx";
import BookData from '../../../../data.json';

const RecipeSearch = ()=>{
    return (
        <div>
            <SearchBar placeholder="Search..." data={BookData}/>
        </div>
    );
};

export default RecipeSearch