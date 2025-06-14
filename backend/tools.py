# tools.py - Comprehensive Dataset of Free AI Tools

tools = [
    # Image Generation Tools
    {
        "name": "Leonardo AI",
        "category": "image",
        "features": ["cinematic", "realistic", "fantasy", "digital art", "anime", "photorealistic"],
        "link": "https://leonardo.ai",
        "description": "Advanced AI image generation with multiple models"
    },
    {
        "name": "Midjourney",
        "category": "image", 
        "features": ["artistic", "fantasy", "abstract", "cinematic", "surreal", "impressionist"],
        "link": "https://midjourney.com",
        "description": "High-quality AI art generation"
    },
    {
        "name": "DALL-E 2",
        "category": "image",
        "features": ["realistic", "creative", "abstract", "minimalist", "photorealistic", "pop art"],
        "link": "https://openai.com/dall-e-2",
        "description": "OpenAI's image generation model"
    },
    {
        "name": "Stable Diffusion",
        "category": "image",
        "features": ["realistic", "artistic", "fantasy", "cyberpunk", "anime", "horror"],
        "link": "https://stability.ai",
        "description": "Open-source image generation"
    },
    {
        "name": "Deepdreamgenerator",
        "category": "image",
        "features": ["abstract", "artistic", "surreal", "vintage", "psychedelic", "experimental"],
        "link": "https://deepdreamgenerator.com",
        "description": "AI-powered dream-like image generation"
    },
    {
        "name": "Artbreeder",
        "category": "image",
        "features": ["realistic", "fantasy", "portrait", "digital art", "renaissance", "baroque"],
        "link": "https://artbreeder.com",
        "description": "Collaborative AI art creation"
    },
    {
        "name": "NightCafe",
        "category": "image",
        "features": ["artistic", "abstract", "oil painting", "watercolor", "impressionist", "gothic"],
        "link": "https://nightcafe.studio",
        "description": "AI art generator with multiple styles"
    },
    {
        "name": "Craiyon",
        "category": "image",
        "features": ["creative", "minimalist", "abstract", "digital art", "comic book", "pixel art"],
        "link": "https://craiyon.com",
        "description": "Free AI image generator"
    },
    
    # Text Generation Tools
    {
        "name": "Copy.ai",
        "category": "text",
        "features": ["professional", "conversational", "marketing", "creative", "persuasive", "humorous"],
        "link": "https://copy.ai",
        "description": "AI-powered copywriting assistant"
    },
    {
        "name": "Jasper AI",
        "category": "text",
        "features": ["professional", "marketing", "formal", "persuasive", "technical", "educational"],
        "link": "https://jasper.ai",
        "description": "Enterprise AI writing platform"
    },
    {
        "name": "ChatGPT",
        "category": "text",
        "features": ["conversational", "creative", "technical", "academic", "analytical", "instructional"],
        "link": "https://chat.openai.com",
        "description": "Versatile AI chat assistant"
    },
    {
        "name": "Grammarly",
        "category": "text",
        "features": ["professional", "formal", "academic", "technical", "educational", "legal"],
        "link": "https://grammarly.com",
        "description": "AI writing enhancement tool"
    },
    {
        "name": "AI-Writer",
        "category": "text",
        "features": ["academic", "professional", "storytelling", "technical", "journalistic", "scientific"],
        "link": "https://ai-writer.com",
        "description": "AI article and content writer"
    },
    {
        "name": "Writesonic",
        "category": "text",
        "features": ["marketing", "creative", "professional", "persuasive", "social media", "e-commerce"],
        "link": "https://writesonic.com",
        "description": "AI writing assistant for marketing"
    },
    {
        "name": "QuillBot",
        "category": "text",
        "features": ["academic", "formal", "casual", "professional", "analytical", "comparative"],
        "link": "https://quillbot.com",
        "description": "AI paraphrasing and writing tool"
    },
    {
        "name": "Rytr",
        "category": "text",
        "features": ["creative", "marketing", "casual", "storytelling", "dramatic", "poetic"],
        "link": "https://rytr.me",
        "description": "AI writing assistant for various content types"
    },
    
    # Music & Audio Tools
    {
        "name": "Soundraw",
        "category": "music",
        "features": ["ambient", "cinematic", "lo-fi", "electronic", "upbeat", "meditation"],
        "link": "https://soundraw.io",
        "description": "AI music composition platform"
    },
    {
        "name": "AIVA",
        "category": "music",
        "features": ["classical", "orchestral", "cinematic", "ambient", "baroque", "romantic"],
        "link": "https://aiva.ai",
        "description": "AI composer for emotional soundtracks"
    },
    {
        "name": "Mubert",
        "category": "music",
        "features": ["electronic", "ambient", "upbeat", "lo-fi", "techno", "house"],
        "link": "https://mubert.com",
        "description": "Real-time AI music generation"
    },
    {
        "name": "DeepBeat",
        "category": "music",
        "features": ["jazz", "rock", "electronic", "upbeat", "hip-hop", "blues"],
        "link": "https://deepbeat.org",
        "description": "AI rap lyrics generator"
    },
    {
        "name": "Boomy",
        "category": "music",
        "features": ["electronic", "ambient", "classical", "meditation", "experimental", "minimalist"],
        "link": "https://boomy.com",
        "description": "Create original songs with AI"
    },
    {
        "name": "Amper Music",
        "category": "music",
        "features": ["cinematic", "orchestral", "electronic", "ambient", "folk", "world music"],
        "link": "https://ampermusic.com",
        "description": "AI music composition for content creators"
    },
    {
        "name": "Jukebox",
        "category": "music",
        "features": ["rock", "jazz", "classical", "electronic", "country", "reggae"],
        "link": "https://openai.com/blog/jukebox",
        "description": "OpenAI's neural net for music generation"
    },
    
    # Video Generation Tools
    {
        "name": "RunwayML",
        "category": "video",
        "features": ["cinematic", "realistic", "stylized", "artistic", "experimental", "short film"],
        "link": "https://runwayml.com",
        "description": "AI video generation and editing"
    },
    {
        "name": "Synthesia",
        "category": "video",
        "features": ["professional", "educational", "commercial", "presentation", "training", "corporate"],
        "link": "https://synthesia.io",
        "description": "AI avatar video creation"
    },
    {
        "name": "Pictory",
        "category": "video",
        "features": ["social media", "promotional", "educational", "commercial", "marketing", "tutorial"],
        "link": "https://pictory.ai",
        "description": "AI video creation from text"
    },
    {
        "name": "Lumen5",
        "category": "video",
        "features": ["social media", "promotional", "educational", "animated", "news", "marketing"],
        "link": "https://lumen5.com",
        "description": "AI-powered video creation platform"
    },
    {
        "name": "InVideo",
        "category": "video",
        "features": ["commercial", "social media", "promotional", "educational", "vlog", "travel"],
        "link": "https://invideo.io",
        "description": "AI video editor and creator"
    },
    {
        "name": "Descript",
        "category": "video",
        "features": ["documentary", "educational", "realistic", "commercial", "interview", "podcast"],
        "link": "https://descript.com",
        "description": "AI-powered video and audio editing"
    },
    {
        "name": "Fliki",
        "category": "video",
        "features": ["educational", "commercial", "social media", "animated", "tutorial", "explainer"],
        "link": "https://fliki.ai",
        "description": "Text to video with AI voices"
    },
    
    # Business Tools
    {
        "name": "Notion AI",
        "category": "business",
        "features": ["professional", "planning", "communication", "project management", "team building", "documentation"],
        "link": "https://notion.so",
        "description": "AI-powered workspace and productivity"
    },
    {
        "name": "Zapier",
        "category": "business",
        "features": ["automation", "professional", "data analysis", "reporting", "operations", "workflow"],
        "link": "https://zapier.com",
        "description": "Workflow automation platform"
    },
    {
        "name": "Monday.com",
        "category": "business",
        "features": ["project management", "planning", "professional", "analytical", "team building", "operations"],
        "link": "https://monday.com",
        "description": "Work management platform with AI"
    },
    {
        "name": "Canva AI",
        "category": "business",
        "features": ["presentation", "professional", "marketing", "creative", "social media", "branding"],
        "link": "https://canva.com",
        "description": "AI-powered design platform"
    },
    {
        "name": "Otter.ai",
        "category": "business",
        "features": ["communication", "professional", "reporting", "analytical", "meeting", "transcription"],
        "link": "https://otter.ai",
        "description": "AI meeting notes and transcription"
    },
    {
        "name": "Calendly",
        "category": "business",
        "features": ["automation", "planning", "professional", "communication", "scheduling", "customer service"],
        "link": "https://calendly.com",
        "description": "AI-powered scheduling assistant"
    },
    {
        "name": "Tome",
        "category": "business",
        "features": ["presentation", "professional", "strategic", "marketing", "storytelling", "executive"],
        "link": "https://tome.app",
        "description": "AI-powered presentation creator"
    },
    {
        "name": "Beautiful.ai",
        "category": "business",
        "features": ["presentation", "professional", "strategic", "analytical", "executive", "consulting"],
        "link": "https://beautiful.ai",
        "description": "AI presentation design platform"
    }
]