import React, { Component } from 'react';

export default function FormErrors ({errors={}}){
    console.log(errors);
    return (
        <ul>
            {
                Object.keys(errors).map((field) => 
                    errors[field].map((error) =>
                        <li key={error.id} className="alert alert-danger">{error.message}</li>
                    )
                )
            }
        </ul>
    );
}