import React from "react";
import { Link } from "react-router-dom";
import "../../styles/navbar.css";

export const Logout = () => {
     
    localStorage.removeItem('jwt-token')
    
    return <div>
       <h1> Log Out </h1>
       <button className="btn btn-primary" onClick={Logout}> Log Out </button>
    </div>

}