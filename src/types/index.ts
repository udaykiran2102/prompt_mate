export interface Tool {
  name: string;
  category: string;
  features: string[];
  link: string;
  description?: string;
}

export interface RecommendedTool extends Tool {
  score: number;
}

export interface PromptRequest {
  prompt: string;
  category: string;
  styles: string[];
}

export interface PromptResponse {
  enhanced_prompt: string;
  recommended_tools: RecommendedTool[];
}

export type Category = 'image' | 'text' | 'music' | 'video' | 'business';

export interface CategoryConfig {
  name: string;
  icon: string;
  styles: string[];
  description: string;
}