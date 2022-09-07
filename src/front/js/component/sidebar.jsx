import React from "react";
import {
    FaTh,
    FaUserAlt,
    FaHeart,
    FaSearch,
    FaBars
}
from "react-icons/fa";
import { NavLink } from "react-router-dom";

const Sidebar = ({children})=>{
    const[isOpen ,setIsOpen] = useState(false);
    const toggle = () => setIsOpen (!isOpen);
    const menuItem=[
        {
            path:"/",
            name:"dashboard",
            icon: <FaTh/>
        },
        {
            path:"/account",
            name:"Account",
            icon: <FaUserAlt/>
        },
        {
            path:"/recipesearch",
            name:"Recipe Search",
            icon: <FaSearch/>
        },

        {
            path:"/favorites",
            name:"Davorites",
            icon: <FaHeart/>
        },
        
        
    ]
    return (
        <div className="container">
            <div className="sidebar">
                <div className="top_section">
                    <h1 style={{display: isOpen ? "block" : "none"}} className="logo">Logo</h1>
                    <div style={{marginLeft: isOpen ? "50px" : "0px"}} className="bars">
                        <FaBars onClick={toggle}/>
                    </div>
                    {
                        menuItem.map((item, index)=>(
                            <NavLink to={item.path} key={index} className="link" activeclassName="active">
                                <div className="icon">{item.icon}</div>
                                <div style={{display: isOpen ? "block" : "none"}} className="link_text">{item.name}</div>                            </NavLink>
                        ))
                    }
                </div>
            </div>
            <main>{children}</main>
        </div>
    );
};

export default Sidebar