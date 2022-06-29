import logo from './logo.svg';
import React, { Component } from 'react';
import './App.css';
import UploadImageToS3WithNativeSdk from './UploadImageToS3WithNativeSdk.jsx'

function App() {

  return (
    <div className="App">
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
          <UploadImageToS3WithNativeSdk />
         
        </a>
      </header>
      
    </div>
  );
}

export default App;
