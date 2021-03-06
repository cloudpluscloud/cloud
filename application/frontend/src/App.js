import logo from './logo.svg';
import React, { Component } from 'react';
import './App.css';
import AlertComp from "./AlertComponent/AlertComp.js"

function App() {
  return (
    <div className="App">
      <AlertComp />
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Hello World
          {/* Edit <code>src/App.js</code> and save to reload. */}
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Hello World
        </a>
      </header>
    </div>
  );
}

export default App;
