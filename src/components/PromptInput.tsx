import React from 'react';

interface PromptInputProps {
  prompt: string;
  onPromptChange: (prompt: string) => void;
}

export const PromptInput: React.FC<PromptInputProps> = ({
  prompt,
  onPromptChange,
}) => {
  return (
    <div className="space-y-4">
      <h3 className="text-lg font-semibold text-gray-800">Enter Your Prompt</h3>
      <textarea
        value={prompt}
        onChange={(e) => onPromptChange(e.target.value)}
        placeholder="Describe what you want to create... (e.g., 'A futuristic cityscape at night')"
        className="w-full p-4 border-2 border-gray-200 rounded-xl focus:border-primary-500 focus:outline-none resize-none transition-colors duration-200"
        rows={4}
      />
    </div>
  );
};