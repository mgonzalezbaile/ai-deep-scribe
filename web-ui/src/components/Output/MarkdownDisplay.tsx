import React from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';

interface MarkdownDisplayProps {
  content: string;
  isLoading: boolean;
}

const MarkdownDisplay: React.FC<MarkdownDisplayProps> = ({ content, isLoading }) => {
  return (
    <div className="markdown-display-container">
      <h2>Generated Post</h2>
      <div className="markdown-content">
        {isLoading ? (
          <div className="loading-spinner"></div>
        ) : content ? (
          <ReactMarkdown remarkPlugins={[remarkGfm]}>{content}</ReactMarkdown>
        ) : (
          <p className="placeholder-text">Your generated content will appear here...</p>
        )}
      </div>
    </div>
  );
};

export default MarkdownDisplay;


