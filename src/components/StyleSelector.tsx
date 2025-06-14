import React from 'react';
import { categories } from '../data/categories';
import { Category } from '../types';

interface StyleSelectorProps {
  category: Category;
  selectedStyles: string[];
  onStyleToggle: (style: string) => void;
}

export const StyleSelector: React.FC<StyleSelectorProps> = ({
  category,
  selectedStyles,
  onStyleToggle,
}) => {
  const categoryConfig = categories[category];

  if (!categoryConfig) return null;

  return (
    <div className="space-y-4">
      <h3 className="text-lg font-semibold text-gray-800">Choose Styles</h3>
      <div className="flex flex-wrap gap-2">
        {categoryConfig.styles.map((style) => (
          <button
            key={style}
            onClick={() => onStyleToggle(style)}
            className={`px-4 py-2 rounded-full text-sm font-medium transition-all duration-200 ${
              selectedStyles.includes(style)
                ? 'bg-secondary-500 text-white shadow-md'
                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
            }`}
          >
            {style}
          </button>
        ))}
      </div>
    </div>
  );
};