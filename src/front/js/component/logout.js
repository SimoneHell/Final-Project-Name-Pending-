import React from "react";
import { Link } from "react-router-dom";
import "../../styles/navbar.css";

export const LogoutFunction = () => {
     
    localStorage.removeItem('jwt-token')
    
   return null

}