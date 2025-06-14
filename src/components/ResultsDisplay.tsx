import React from 'react';
import { ExternalLink, Copy, Check } from 'lucide-react';
import { PromptResponse } from '../types';

interface ResultsDisplayProps {
  results: PromptResponse;
}

export const ResultsDisplay: React.FC<ResultsDisplayProps> = ({ results }) => {
  const [copied, setCopied] = React.useState(false);

  const copyToClipboard = async (text: string) => {
    try {
      await navigator.clipboard.writeText(text);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch (err) {
      console.error('Failed to copy text: ', err);
    }
  };

  return (
    <div className="space-y-8 animate-fade-in">
      {/* Enhanced Prompt */}
      <div className="bg-gradient-to-r from-primary-50 to-secondary-50 p-6 rounded-xl border border-primary-200">
        <div className="flex items-center justify-between mb-4">
          <h3 className="text-lg font-semibold text-gray-800">Enhanced Prompt</h3>
          <button
            onClick={() => copyToClipboard(results.enhanced_prompt)}
            className="flex items-center gap-2 px-3 py-1 bg-white rounded-lg border border-gray-200 hover:bg-gray-50 transition-colors duration-200"
          >
            {copied ? (
              <>
                <Check size={16} className="text-green-500" />
                <span className="text-sm text-green-500">Copied!</span>
              </>
            ) : (
              <>
                <Copy size={16} className="text-gray-600" />
                <span className="text-sm text-gray-600">Copy</span>
              </>
            )}
          </button>
        </div>
        <p className="text-gray-700 leading-relaxed">{results.enhanced_prompt}</p>
      </div>

      {/* Recommended Tools */}
      <div className="space-y-4">
        <h3 className="text-lg font-semibold text-gray-800">Recommended AI Tools</h3>
        {results.recommended_tools.length === 0 ? (
          <div className="text-center py-8 text-gray-500">
            No tools found for your criteria. Try different styles or categories.
          </div>
        ) : (
          <div className="grid gap-4">
            {results.recommended_tools.map((tool, index) => (
              <div
                key={index}
                className="bg-white p-6 rounded-xl border border-gray-200 hover:shadow-lg transition-all duration-200 animate-slide-up"
                style={{ animationDelay: `${index * 0.1}s` }}
              >
                <div className="flex items-start justify-between">
                  <div className="flex-1">
                    <div className="flex items-center gap-3 mb-2">
                      <h4 className="text-xl font-semibold text-gray-800">{tool.name}</h4>
                      <div className="flex items-center gap-1 px-2 py-1 bg-primary-100 text-primary-700 rounded-full text-xs font-medium">
                        <span>Score: {tool.score}</span>
                      </div>
                    </div>
                    <div className="flex flex-wrap gap-2 mb-3">
                      {tool.features.map((feature) => (
                        <span
                          key={feature}
                          className="px-2 py-1 bg-gray-100 text-gray-600 rounded-md text-sm"
                        >
                          {feature}
                        </span>
                      ))}
                    </div>
                  </div>
                  <a
                    href={tool.link}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="flex items-center gap-2 px-4 py-2 bg-primary-500 text-white rounded-lg hover:bg-primary-600 transition-colors duration-200"
                  >
                    <span>Visit Tool</span>
                    <ExternalLink size={16} />
                  </a>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};