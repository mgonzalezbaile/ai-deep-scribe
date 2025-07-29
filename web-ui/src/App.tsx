import React, { useState, useCallback } from 'react';
import { Toaster, toast } from 'react-hot-toast';
import Header from './components/Layout/Header';
import UserInput from './components/Input/UserInput';
import MarkdownDisplay from './components/Output/MarkdownDisplay';

interface Post {
  id: string;
  content: string;
  state: string;
}

const App: React.FC = () => {
  const [content, setContent] = useState<string>('');
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [isPolling, setIsPolling] = useState<boolean>(false);

  const pollPostStatus = useCallback(async (postId: string): Promise<string> => {
    const maxAttempts = 30; // 30 attempts with 2s delay = 1 minute total
    const delay = 2000; // 2 seconds

    for (let attempt = 0; attempt < maxAttempts; attempt++) {
      try {
        const response = await fetch(`/api/posts/${postId}`);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const post: Post = await response.json();
        
        if (post.state === 'completed') {
          return post.content;
        } else if (post.state === 'failed') {
          throw new Error('Post generation failed. Please try again.');
        }
        // If not completed or failed, continue polling
      } catch (err) {
        console.error('Error polling post status:', err);
        // On last attempt, rethrow the error
        if (attempt === maxAttempts - 1) {
          throw err;
        }
      }
      
      // Wait before next poll, except on last iteration
      if (attempt < maxAttempts - 1) {
        await new Promise(resolve => setTimeout(resolve, delay));
      }
    }

    throw new Error('Post generation timed out. Please try again.');
  }, []);

  const handleGenerate = async (userRequest: string) => {
    if (isLoading || isPolling) return;
    
    setIsLoading(true);
    setContent('');

    try {
      // Step 1: Create the post and get the ID
      const response = await fetch('/api/posts', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_request: userRequest }),
      });

      if (!response.ok) {
        throw new Error('Failed to start post generation. Please try again.');
      }

      const { id: postId } = await response.json();
      if (!postId) {
        throw new Error('Invalid response from server: Missing post ID');
      }

      // Step 2: Start polling for the post status
      setIsPolling(true);
      toast.loading('Generating your post...', { id: 'post-status' });
      
      const postContent = await pollPostStatus(postId);
      
      // Step 3: Update the UI with the generated content
      setContent(postContent);
      toast.success('Post generated successfully!', { id: 'post-status' });
    } catch (err) {
      toast.dismiss('post-status');
      if (err instanceof Error) {
        toast.error(err.message);
      } else {
        toast.error('An unknown error occurred.');
      }
    } finally {
      setIsLoading(false);
      setIsPolling(false);
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

