# recommender.py - Content-Based Filtering Logic

from tools import tools
import re

def recommend_tools(user_category: str, user_styles: list):
    """
    Content-based filtering recommendation algorithm
    
    Args:
        user_category (str): Selected category (image, text, music, video, business)
        user_styles (list): List of selected styles/features
    
    Returns:
        list: Ranked list of recommended tools
    """
    recommendations = []
    
    # Normalize inputs
    user_category = user_category.lower().strip()
    user_styles = [style.lower().strip() for style in user_styles]
    
    for tool in tools:
        # Calculate category match (binary: 1 or 0)
        category_match = 1 if tool["category"].lower() == user_category else 0
        
        # Calculate style overlap
        tool_features = [feature.lower() for feature in tool["features"]]
        style_overlap = list(set(tool_features) & set(user_styles))
        style_overlap_count = len(style_overlap)
        
        # Calculate total score
        # Category match is weighted higher (base score of 1)
        # Each style match adds 0.5 to the score
        score = category_match + (style_overlap_count * 0.5)
        
        # Only include tools with some relevance (score > 0)
        if score > 0:
            recommendations.append({
                "name": tool["name"],
                "category": tool["category"],
                "link": tool["link"],
                "features": tool["features"],
                "description": tool.get("description", ""),
                "score": round(score, 1),
                "matched_styles": style_overlap
            })
    
    # Sort by score (highest first), then by name for consistency
    recommendations.sort(key=lambda x: (-x["score"], x["name"]))
    
    return recommendations

def enhance_prompt(prompt: str, category: str, styles: list):
    """
    Generate an enhanced, detailed prompt based on user input
    
    Args:
        prompt (str): Original user prompt
        category (str): Selected category
        styles (list): Selected styles
    
    Returns:
        str: Enhanced, detailed prompt
    """
    # Clean and format inputs
    prompt = prompt.strip()
    category = category.lower()
    styles = [style.lower() for style in styles if style.strip()]
    
    if not styles:
        return f"Create a high-quality {category} of: '{prompt}'"
    
    # Style descriptions for more detailed prompts
    style_descriptions = {
        # Image styles
        "realistic": "photorealistic detail with lifelike textures, accurate proportions, and natural lighting",
        "cinematic": "movie-quality lighting, dramatic angles, and professional film aesthetics",
        "fantasy": "magical elements, mythical creatures, and otherworldly atmospheres",
        "abstract": "non-representational forms, geometric patterns, and conceptual visual elements",
        "minimalist": "clean, simple composition with essential elements and plenty of negative space",
        "vintage": "nostalgic vintage aesthetics, aged textures, and classic design elements from bygone eras",
        "cyberpunk": "futuristic neon-lit urban landscapes with high-tech and low-life themes",
        "watercolor": "soft, flowing watercolor techniques with translucent layers and organic color bleeding",
        "oil painting": "rich, textured oil painting style with visible brushstrokes and classical techniques",
        "digital art": "modern digital illustration techniques with crisp details and vibrant colors",
        "impressionist": "loose brushwork, light effects, and atmospheric color harmony",
        "western": "Wild West themes, desert landscapes, and frontier-era visual elements",
        "horror": "dark, unsettling atmosphere, dramatic shadows, and spine-chilling visual elements",
        "anime": "Japanese anime aesthetic with distinctive character features, dynamic poses, and vibrant colors",
        "pixel art": "retro pixel art style with 8-bit or 16-bit graphics, blocky textures, and nostalgic gaming aesthetics",
        "steampunk": "Victorian-era industrial design with brass, copper, and steam-powered machinery",
        "art nouveau": "elegant Art Nouveau style with flowing organic lines and decorative natural motifs",
        "surreal": "dreamlike, impossible scenarios with distorted reality and subconscious imagery",
        "gothic": "dark Gothic architecture, mysterious atmosphere, and medieval aesthetic elements",
        "pop art": "bold Pop Art style with bright colors, commercial imagery, and graphic design elements",
        "noir": "film noir aesthetic with high contrast lighting, shadows, and moody atmosphere",
        "baroque": "ornate Baroque style with dramatic lighting, rich details, and emotional intensity",
        "renaissance": "classical Renaissance techniques with perfect proportions and masterful composition",
        "futuristic": "advanced technology, sleek designs, and sci-fi elements from the distant future",
        "tribal": "indigenous tribal art patterns, earthy colors, and cultural symbolic elements",
        "grunge": "raw, edgy grunge aesthetic with distressed textures and alternative culture themes",
        "comic book": "comic book illustration style with bold outlines, dynamic action, and speech bubbles",
        "photorealistic": "extremely detailed photographic realism with perfect lighting and textures",
        "sketch": "hand-drawn sketch style with pencil lines, crosshatching, and artistic imperfections",
        "neon": "vibrant neon colors, glowing effects, and electric urban nightlife atmosphere",
        "pastel": "soft pastel color palette with gentle, soothing tones and dreamy atmosphere",
        "monochrome": "single-color or black and white treatment with strong tonal contrast",
        "sepia": "warm sepia tones evoking nostalgia and vintage photography aesthetics",
        "HDR": "high dynamic range with enhanced contrast, vivid colors, and detailed shadows and highlights",
        "macro": "extreme close-up macro photography revealing intricate details and textures",
        "panoramic": "wide panoramic view capturing expansive landscapes and broad perspectives",
        
        # Text styles
        "professional": "polished, business-appropriate tone with clear structure and formal language",
        "conversational": "friendly, approachable tone as if speaking directly to the reader",
        "creative": "imaginative, original approach with unique perspectives and artistic flair",
        "formal": "structured, official tone following proper grammar and professional conventions",
        "casual": "relaxed, informal style with everyday language and personal touch",
        "persuasive": "compelling arguments designed to convince and motivate the reader to action",
        "technical": "precise, detailed explanations with industry-specific terminology and accuracy",
        "storytelling": "narrative structure with engaging plot, characters, and emotional connection",
        "marketing": "promotional content designed to attract, engage, and convert potential customers",
        "academic": "scholarly approach with research-based content, citations, and analytical depth",
        "humorous": "witty, entertaining tone with jokes, puns, and lighthearted observations",
        "dramatic": "intense, emotional language with powerful imagery and theatrical elements",
        "poetic": "lyrical, metaphorical language with rhythm, imagery, and artistic expression",
        "journalistic": "objective, factual reporting style with who, what, when, where, why structure",
        "scientific": "evidence-based, methodical approach with data, research, and logical conclusions",
        
        # Music styles
        "ambient": "atmospheric, immersive soundscapes with ethereal textures and spatial depth",
        "cinematic": "orchestral, dramatic compositions suitable for film scores and emotional storytelling",
        "lo-fi": "warm, nostalgic sound with vinyl crackle, tape hiss, and relaxed, downtempo rhythms",
        "electronic": "synthesized sounds, digital effects, and modern electronic production techniques",
        "classical": "traditional orchestral arrangements with complex harmonies and formal structures",
        "jazz": "improvisational elements, swing rhythms, and sophisticated harmonic progressions",
        "rock": "guitar-driven sound with strong rhythms, powerful vocals, and energetic performance",
        "orchestral": "full symphony orchestra with rich instrumentation and dynamic arrangements",
        "meditation": "peaceful, calming tones designed for relaxation, mindfulness, and inner peace",
        "upbeat": "energetic, positive rhythms that inspire movement and elevate mood",
        
        # Video styles
        "documentary": "factual, informative approach with real-world footage and educational content",
        "animated": "cartoon or computer-generated animation with creative visual storytelling",
        "stylized": "artistic visual treatment with unique aesthetic choices and creative direction",
        "commercial": "polished, professional production values suitable for advertising and promotion",
        "educational": "instructional content designed to teach, inform, and engage learners",
        "artistic": "creative, experimental approach prioritizing visual beauty and artistic expression",
        "promotional": "marketing-focused content designed to showcase products, services, or brands",
        "social media": "short-form, engaging content optimized for social media platforms and sharing",
        
        # Business styles
        "analytical": "data-driven approach with metrics, charts, and quantitative analysis",
        "strategic": "long-term planning focus with goal-setting, market analysis, and competitive positioning",
        "presentation": "visual, slide-based format suitable for meetings, pitches, and formal presentations",
        "reporting": "structured documentation of results, progress, and key performance indicators",
        "automation": "streamlined, efficient processes that reduce manual work and increase productivity",
        "planning": "organized, systematic approach to project management and resource allocation",
        "communication": "clear, effective messaging for internal teams and external stakeholders"
    }
    
    # Build detailed style descriptions
    style_parts = []
    for style in styles:
        if style in style_descriptions:
            style_parts.append(f"while also {get_style_verb(category)} with {style_descriptions[style]}")
    
    # Create the enhanced prompt
    base_action = get_category_action(category)
    enhanced = f"{base_action} {prompt}"
    
    if style_parts:
        enhanced += ", " + ", ".join(style_parts)
    
    enhanced += ", maintaining professional excellence and technical precision."
    
    return enhanced

def get_category_action(category: str) -> str:
    """Get the appropriate action verb for each category"""
    actions = {
        "image": "Create an image of",
        "text": "Write content about",
        "music": "Compose music inspired by",
        "video": "Create a video featuring",
        "business": "Develop a business solution for"
    }
    return actions.get(category, f"Create {category} content about")

def get_style_verb(category: str) -> str:
    """Get appropriate style application verb for each category"""
    verbs = {
        "image": "designed",
        "text": "written",
        "music": "composed",
        "video": "produced",
        "business": "structured"
    }
    return verbs.get(category, "created")

# Additional utility functions for ML-like features

def calculate_similarity_score(tool_features: list, user_styles: list):
    """
    Calculate Jaccard similarity between tool features and user styles
    
    Args:
        tool_features (list): Features supported by the tool
        user_styles (list): Styles selected by user
    
    Returns:
        float: Similarity score between 0 and 1
    """
    if not tool_features or not user_styles:
        return 0.0
    
    tool_set = set(feature.lower() for feature in tool_features)
    user_set = set(style.lower() for style in user_styles)
    
    intersection = len(tool_set & user_set)
    union = len(tool_set | user_set)
    
    return intersection / union if union > 0 else 0.0

def get_tool_statistics():
    """
    Get statistics about the tools dataset
    
    Returns:
        dict: Statistics about tools and features
    """
    categories = {}
    all_features = set()
    
    for tool in tools:
        category = tool["category"]
        categories[category] = categories.get(category, 0) + 1
        all_features.update(feature.lower() for feature in tool["features"])
    
    return {
        "total_tools": len(tools),
        "categories": categories,
        "total_features": len(all_features),
        "features": sorted(list(all_features))
    }