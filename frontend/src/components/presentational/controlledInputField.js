import React, { Component } from 'react';

export default function ControlledInputField ({displayName='', name='',type='text',value='', handleChange, label=false}){
    return (
        <div>
            {label ? <label>{displayName}</label> : ''}
            <input placeholder={displayName} name={name} onChange={handleChange} type={type} value={value}/>
        </div>
    );
}
