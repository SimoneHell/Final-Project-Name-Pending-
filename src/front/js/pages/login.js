import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import "../../styles/index.css";





export const Login = () => {
    return <div className="log-form">
    <h2>Login to your account</h2>
    <form>
      <input type="text" title="username" placeholder="username" />
      <input type="password" title="username" placeholder="password" />
      <button type="submit" className="btn">Login</button>
      <a className="forgot" >Forgot Username?</a>
    </form>
  </div>
}