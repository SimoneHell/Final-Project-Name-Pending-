
import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";
import { useNavigate } from "react-router-dom";

export const SignUp = () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const { store, actions } = useContext(Context);

  let navigate = useNavigate();

  const CreateUser = async (e) => {
    e.preventDefault();
    const response = await fetch(
      "https://3002-nealxero-authentication-cf8499sax29.ws-eu63.gitpod.io/api/signup",
      {
        method: "POST",
        body: JSON.stringify({ email, password }),
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    const confirmation = await response.json();
    if (response.status == 200) {
      navigate("/login");
    } else {
      alert(confirmation.alert);
    }
  };

  return  <div className="log-form">
    <h2>Create your account!</h2>
    <form>
      <input type="text" title="username" placeholder="username" />
      <input type="password" title="username" placeholder="password" />
      <button type="submit" className="btn">Signup</button>
    </form>
  </div>
}