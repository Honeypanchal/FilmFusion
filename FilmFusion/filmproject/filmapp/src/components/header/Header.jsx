import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css'
import logo from '../../assets/tmovie.png';
const Header = () => {
  return (
    <nav>
      <div className="navbar-container">
        <Link to="/" className="navbar-logo">
          <img src={logo} alt="MovieSite Logo" />
        </Link>
        <form action="/search" method="get" className="navbar-search">
          <input type="text" name="query" placeholder="Search..." />
          <button type="submit">Search</button>
        </form>
        <ul className="navbar-menu">
          <li><Link to="/trending">Trending</Link></li>
          <li><Link to="/login">Login</Link></li>
          <li><Link to="/signup">Signup</Link></li>
        </ul>
      </div>
    </nav>
  );
};

export default Header;
