import React, { useState } from 'react';
import { Toaster, toast } from 'react-hot-toast';
import Header from './components/Layout/Header';
import UserInput from './components/Input/UserInput';
import MarkdownDisplay from './components/Output/MarkdownDisplay';

const App: React.FC = () => {
  const [content, setContent] = useState<string>('');
  const [isLoading, setIsLoading] = useState<boolean>(false);


  const handleGenerate = async (userRequest: string) => {
    setIsLoading(true);

    try {
            const response = await fetch('/api/posts', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_request: userRequest }),
      });

      if (!response.ok) {
        throw new Error('Failed to generate post. Please try again.');
      }

      const data = await response.json();
      if (typeof data.content !== 'string') {
        throw new Error('Received invalid data format from the server.');
      }
      setContent(data.content);
      toast.success('Post generated successfully!');
    } catch (err) {
      if (err instanceof Error) {
        toast.error(err.message);
      } else {
        toast.error('An unknown error occurred.');
      }
    } finally {
      setIsLoading(false);
    }

  };

  return (
    <div className="App">
      <Toaster position="bottom-right" />
      <Header />
      <main className="main-content">
        {content ? (
          <>
            <MarkdownDisplay content={content} isLoading={isLoading} />
            <UserInput onGenerate={handleGenerate} isLoading={isLoading} hasContent={!!content} />
          </>
        ) : (
          <UserInput onGenerate={handleGenerate} isLoading={isLoading} hasContent={!!content} />
        )}
      </main>
    </div>
  );
};

export default App;

