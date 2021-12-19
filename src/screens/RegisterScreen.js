import React from 'react';
import NavBar from '../components/NavBar';
import { Link, useNavigate } from 'react-router-dom';
import { useState } from 'react/cjs/react.development';
import axios from 'axios';
import { api } from '../api';

const RegisterScreen = () => {
  const navigate = useNavigate();
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [age, setAge] = useState('');
  const [gender, setGender] = useState('');
  const [country, setCountry] = useState('');
  const [state, setState] = useState('');
  const [city, setCity] = useState('');
  const [password, setPassword] = useState('');

  const submitHandler = async (e) => {
    e.preventDefault();
    await axios.post(`${api}/users/create_user`, {
      name,
      age: Number(age),
      gender,
      country,
      state,
      city,
      password,
      email,
    });
    navigate('/login');
  };
  return (
    <div>
      <NavBar />
      <div className="login">
        <h1>Register</h1>
        <form>
          <label>Username</label>
          <input onChange={(e) => setName(e.target.value)} value={name} />
          <label>Age</label>
          <input onChange={(e) => setAge(e.target.value)} />
          <label>Gender</label>
          <input onChange={(e) => setGender(e.target.value)} />
          <label>Country</label>
          <input onChange={(e) => setCountry(e.target.value)} />
          <label>State</label>
          <input onChange={(e) => setState(e.target.value)} />
          <label>City</label>
          <input onChange={(e) => setCity(e.target.value)} />
          <label>Email</label>
          <input onChange={(e) => setEmail(e.target.value)} />
          <label>Password</label>
          <input onChange={(e) => setPassword(e.target.value)} />
          <button onClick={submitHandler} className="login_btn">
            Register
          </button>
          <Link to="/login">Have Account? Login here</Link>
        </form>
      </div>
    </div>
  );
};

export default RegisterScreen;
