import React from 'react';
import { Link } from 'react-router-dom';

export default function NavDropdownMenu (props) {
    return (
        <li className="nav-item dropdown">
          <Link className="nav-link dropdown-toggle" to="#" id="navbardrop" data-toggle="dropdown">
            {props.label}
          </Link>
          <div className="dropdown-menu bg-dark dropdown-menu-right">
            {props.children}
          </div>
        </li>
    );
}