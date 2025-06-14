import { PromptRequest, PromptResponse } from '../types';

// Determine the appropriate protocol and base URL
const getApiBaseUrl = () => {
  // If we're running on HTTPS, we need to use HTTPS for the backend too
  // Otherwise, use HTTP to match the backend
  const protocol = window.location.protocol;
  const isSecure = protocol === 'https:';
  
  // For development, always use HTTP to match the Flask backend
  // In production, this would need to be configured appropriately
  return 'http://localhost:5000';
};

const API_BASE_URL = getApiBaseUrl();

export const promptService = {
  async getRecommendations(request: PromptRequest): Promise<PromptResponse> {
    try {
      const response = await fetch(`${API_BASE_URL}/recommend`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(request),
      });

      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`HTTP error! status: ${response.status}, message: ${errorText}`);
      }

      return await response.json();
    } catch (error) {
      console.error('API Error:', error);
      
      // Provide more specific error messages
      if (error instanceof TypeError && error.message.includes('Failed to fetch')) {
        throw new Error('Unable to connect to the backend server. Please ensure the backend is running on http://localhost:5000 and access the frontend via http://localhost:5173 (not https).');
      }
      
      throw new Error('Failed to get recommendations. Please try again.');
    }
  }
};