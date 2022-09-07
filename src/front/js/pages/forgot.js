import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";
import { useNavigate } from "react-router-dom";
import { Link } from "react-router-dom";

export const ForgotPassword = () => {
  return (
    <div id="card">
      <div id="card-content">
        <div id="card-title">
          <h2>Get a new password in one click</h2>
          <div className="underline-title"></div>
        </div>
        <form className="form">
          <label htmlFor="user-email">Enter the email address linked to your account</label>
          <input
            id="user-email"
            className="form-content"
            type="email"
            name="email"
            autoComplete="on"
            required
          />
          <div className="form-border"></div>

          <input id="submit-btn" type="submit" name="submit" value="SEND" />
          <p id="signup">
            <Link to="/signup">Cancel</Link>
          </p>
        </form>
      </div>
    </div>
  );
};
