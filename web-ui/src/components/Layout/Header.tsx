import React from 'react';
import SparkleIcon from '../Icons/SparkleIcon';

const Header: React.FC = () => {
  return (
    <header className="app-header">
      <h1 className="app-title">
        <SparkleIcon className="title-icon" /> AI Blog Generator
      </h1>
      <p className="app-subtitle">
        Transform your ideas into compelling blog posts with our intelligent agentic system. Just describe your topic, and watch as AI researches and crafts your content.
      </p>
    </header>
  );
};

export default Header;
