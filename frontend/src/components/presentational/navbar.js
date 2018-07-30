import React from 'react';
import { Link } from 'react-router-dom';

export default function Navbar (props) {
    return (
        <nav className="navbar navbar-expand-sm bg-dark navbar-dark">
          <Link to='/' className="nav-link navbar-brand">{props.siteLabel}</Link>
          <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarSupportedContent">
              <ul className="navbar-nav ml-auto">
              {props.children}
              </ul>
          </div>
        </nav>
    );
}