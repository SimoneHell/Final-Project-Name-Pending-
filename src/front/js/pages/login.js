import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import "../../styles/index.css";



export const Login = () => {
  const { store, actions } = useContext(Context);

  // This is a hook and returns an array of [state, setState]
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const logClick = async (e) => {
    // This is necessary if we are using a form
    // Whit this we are overrinding the default behaviour of the form so it doesn't refresh
    e.preventDefault();
    const loginOptions = {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify({
        email,
        password,
      }),
    };

    const promiseResponse = await fetch(
      "https://3001-nealxero-finalprojectna-w4rqtnneran.ws-eu63.gitpod.io/api/login",
      loginOptions,
      {
       
      }
    )
      .then((resp) => resp.json())
      .then((res) => {
        alert("Login in successfull");
        return res;
      })
      .catch((error) => console.error("Something went wrong", error));

    localStorage.setItem("jwt-token", promiseResponse.token);
  };

  return (
    <div className="log-form">
      <h2>Login to your account</h2>
      <form>
        <input type="text" title="username" placeholder="username" value={email} onChange={(e) => setEmail(e.target.value)}/>
        <input type="password" title="username" placeholder="password" value={password} onChange={(e) => setPassword(e.target.value)}/>
        <button type="submit" className="btn"  onClick={(e) => logClick(e)}>
          Login
        </button>
        <a className="forgot">Forgot Username?</a>
      </form>
    </div>
  );
};
