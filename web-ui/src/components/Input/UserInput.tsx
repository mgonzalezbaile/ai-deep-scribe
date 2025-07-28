import React, { useState } from 'react';
import SendIcon from '../Icons/SendIcon';

interface UserInputProps {
  onGenerate: (request: string) => void;
  isLoading: boolean;
}

const UserInput: React.FC<UserInputProps> = ({ onGenerate, isLoading }) => {
  const [request, setRequest] = useState('');

  const handleGenerateClick = () => {
    if (request.trim()) {
      onGenerate(request);
    }
  };

  return (
    <div className="user-input-container">
      <label htmlFor="userInput">What would you like to write about?</label>
      <textarea
        id="userInput"
        placeholder="e.g., 'The future of artificial intelligence in healthcare' or 'Best practices for sustainable gardening in urban environments'"
        value={request}
        onChange={(e) => setRequest(e.target.value)}
        disabled={isLoading}
      />
      <button onClick={handleGenerateClick} disabled={isLoading}>
        <SendIcon />
        {isLoading ? 'Generating...' : 'Generate Blog Post'}
      </button>
    </div>
  );
};

export default UserInput;

