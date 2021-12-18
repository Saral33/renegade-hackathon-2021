import React from 'react';
import NavBar from '../components/NavBar';
import { Link } from 'react-router-dom';

const RegisterScreen = () => {
  return (
    <div>
      <NavBar />
      <div className="login">
        <h1>Register</h1>
        <form>
          <label>Username</label>
          <input />
          <label>Email</label>
          <input />
          <label>Password</label>
          <input />
          <button className="login_btn">Register</button>
          <Link to="/login">Have Account? Login here</Link>
        </form>
      </div>
    </div>
  );
};

export default RegisterScreen;
