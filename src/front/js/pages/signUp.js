import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import "../../styles/index.css";

export const Signup = () => {
    return <div className="log-form">
    <h2>Create your account!</h2>
    <form>
      <input type="text" title="name" placeholder="name"/>
      <input type="text" title="username" placeholder="username" />
      <input type="password" title="username" placeholder="password" />
      <button type="submit" className="btn">Signup</button>
    </form>
  </div>
}