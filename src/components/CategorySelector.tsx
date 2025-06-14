import React from 'react';
import { categories } from '../data/categories';
import { Category } from '../types';

interface CategorySelectorProps {
  selectedCategory: Category | '';
  onCategoryChange: (category: Category) => void;
}

export const CategorySelector: React.FC<CategorySelectorProps> = ({
  selectedCategory,
  onCategoryChange,
}) => {
  return (
    <div className="space-y-4">
      <h3 className="text-lg font-semibold text-gray-800">Select Category</h3>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {Object.entries(categories).map(([key, category]) => (
          <button
            key={key}
            onClick={() => onCategoryChange(key as Category)}
            className={`p-4 rounded-xl border-2 transition-all duration-200 hover:scale-105 ${
              selectedCategory === key
                ? 'border-primary-500 bg-primary-50 shadow-lg'
                : 'border-gray-200 bg-white hover:border-primary-300 hover:shadow-md'
            }`}
          >
            <div className="text-3xl mb-2">{category.icon}</div>
            <h4 className="font-semibold text-gray-800 mb-1">{category.name}</h4>
            <p className="text-sm text-gray-600">{category.description}</p>
          </button>
        ))}
      </div>
    </div>
  );
};