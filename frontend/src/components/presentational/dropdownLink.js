import React from 'react';
import { Link } from 'react-router-dom';

export default function DropdownLink (props) {
    return (
        <Link to={props.location} className="dropdown-item text-white bg-dark" onClick={props.onClick}>{props.label}</Link>
    );
}