import React from 'react';
import { Link } from 'react-router-dom';

export default function NavLink (props) {
    return (
        <li className="nav-item">
          <Link to={props.location} className="nav-link">{props.label}</Link>
        </li>
    );
}