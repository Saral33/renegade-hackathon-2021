import React from 'react';
import { Link } from 'react-router-dom';

const NavBar = () => {
  return (
    <nav>
      <div className="logo">
        <Link to="/">Logo</Link>
      </div>
      <div className="links">
        <Link to="/login">Login/Register</Link>
      </div>
    </nav>
  );
};

export default NavBar;
