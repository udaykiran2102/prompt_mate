import React from 'react';

export const LoadingSpinner: React.FC = () => {
  return (
    <div className="flex flex-col items-center justify-center py-12">
      <div className="relative">
        <div className="w-12 h-12 border-4 border-primary-200 border-t-primary-500 rounded-full animate-spin"></div>
        <div className="absolute inset-0 w-12 h-12 border-4 border-transparent border-r-secondary-500 rounded-full animate-spin animation-delay-150"></div>
      </div>
      <p className="mt-4 text-gray-600 animate-pulse-slow">Generating recommendations...</p>
    </div>
  );
};