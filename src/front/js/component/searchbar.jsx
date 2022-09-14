import React from 'react';
import {FaSearch} from "react-icons/fa";
function SearchBar ({placeholder, data}) {
    return (
        <div className='search'>
            <div className='searchInput'>
                <input type="text" placeholder={placeholder}/>
                <div classname="searchIcon"><FaSearch/></div>
            </div>
            <div className='searchResults'></div>
        </div>
    )
};
export default SearchBar;