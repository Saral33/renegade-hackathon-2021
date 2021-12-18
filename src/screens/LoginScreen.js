import React, { useState } from 'react';
import NavBar from '../components/NavBar';
import { Link } from 'react-router-dom';
import axios from 'axios';
import { api } from '../api';

const LoginScreen = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const submitHandler = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post(`${api}/auth/login`, { email, password });
    } catch (error) {}
  };
  return (
    <div>
      <NavBar />
      <div className="login">
        <h1>Login</h1>
        <form onSubmit={submitHandler}>
          <label>Email</label>
          <input onChange={(e) => setEmail(e.target.value)} />
          <label>Password</label>
          <input onChange={(e) => setPassword(e.target.value)} />
          <button type="submit" className="login_btn">
            Login
          </button>
          <Link to="/register">No Account? Register Here</Link>
        </form>
      </div>
    </div>
  );
};

export default LoginScreen;
