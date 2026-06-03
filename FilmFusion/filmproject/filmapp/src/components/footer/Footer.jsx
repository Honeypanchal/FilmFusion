import React from 'react'
import logo from '../../assets/tmovie.png'
import footbg from '../../assets/footer-bg.jpg'
import './Footer.css'
const Footer = () => {
    return (
        <footer className="footer" style={{backgroundImage:`URL(${footbg})`}}>
          <div className="footer-content">
            <img src={logo} alt="Logo" className="footer-logo" />
            <ul className="footer-links">
              <li><a href="list/movies">Movies</a></li>
              <li><a href="list/tvshows">TV Shows</a></li>
              <li><a href="/others">Others</a></li>
            </ul>
          </div>
        </footer>
      );
}

export default Footer