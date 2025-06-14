# Prompt Mate Backend

This is the Python Flask backend for Prompt Mate, implementing a content-based filtering recommendation algorithm for AI tools.

## Features

- **Content-Based Filtering**: Recommends AI tools based on category and style matching
- **Prompt Enhancement**: Generates improved prompts using category and style templates
- **RESTful API**: Clean API endpoints for frontend integration
- **Comprehensive Tool Dataset**: Curated list of free AI tools across multiple categories

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Flask server:
```bash
python app.py
```

The server will start on `http://localhost:5000`

## API Endpoints

### POST /recommend
Generate enhanced prompts and tool recommendations.

**Request Body:**
```json
{
  "prompt": "A futuristic cityscape at night",
  "category": "image",
  "styles": ["cinematic", "realistic"]
}
```

**Response:**
```json
{
  "enhanced_prompt": "Create a cinematic, realistic image of: 'A futuristic cityscape at night'",
  "recommended_tools": [
    {
      "name": "Leonardo AI",
      "category": "image",
      "link": "https://leonardo.ai",
      "features": ["cinematic", "realistic", "fantasy", "digital art"],
      "score": 2.0,
      "matched_styles": ["cinematic", "realistic"]
    }
  ]
}
```

### GET /categories
Get available categories and their supported styles.

### GET /stats
Get statistics about the tools dataset.

### GET /
Health check endpoint.

## Algorithm Details

The content-based filtering algorithm works by:

1. **Category Matching**: Tools matching the user's selected category get a base score of 1
2. **Style Overlap**: Each matching style adds 0.5 to the score
3. **Ranking**: Tools are sorted by score (highest first)
4. **Filtering**: Only tools with score > 0 are returned

## File Structure

- `app.py` - Main Flask application and API endpoints
- `recommender.py` - Content-based filtering algorithm implementation
- `tools.py` - Static dataset of AI tools
- `requirements.txt` - Python dependencies