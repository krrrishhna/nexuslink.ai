"""
NexusLink AI — Content Creation & Publishing Tools
"""

import json
from auth.linkedin_auth import linkedin_api_get, linkedin_api_post


def register_content_tools(mcp):

    @mcp.tool()
    def create_linkedin_post(text: str, visibility: str = "PUBLIC") -> str:
        """
        Create and publish a text post on LinkedIn.
        
        Args:
            text: The content of your post (supports emojis and hashtags)
            visibility: Post visibility — PUBLIC or CONNECTIONS (default: PUBLIC)
        """
        try:
            # Get user URN
            profile = linkedin_api_get("/v2/userinfo")
            user_sub = profile.get("sub", "")

            post_data = {
                "author": f"urn:li:person:{user_sub}",
                "lifecycleState": "PUBLISHED",
                "specificContent": {
                    "com.linkedin.ugc.ShareContent": {
                        "shareCommentary": {"text": text},
                        "shareMediaCategory": "NONE",
                    }
                },
                "visibility": {
                    "com.linkedin.ugc.MemberNetworkVisibility": visibility
                },
            }

            result = linkedin_api_post("/v2/ugcPosts", post_data)

            if "id" in result:
                return f"✅ Post published successfully!\nPost ID: {result['id']}"
            else:
                return f"❌ Failed to publish: {json.dumps(result, indent=2)}"
        except Exception as e:
            return f"Error creating post: {str(e)}"

    @mcp.tool()
    def generate_post_ideas(topic: str, count: int = 5) -> str:
        """
        Generate engaging LinkedIn post ideas on a given topic.
        
        Args:
            topic: The subject area for post ideas
            count: Number of ideas to generate (default: 5)
        """
        templates = [
            f"🔥 Hot take: Why most people get {topic} wrong (and what to do instead)",
            f"📊 I analyzed 100+ {topic} examples. Here are 5 patterns that stood out:",
            f"💡 3 lessons I learned about {topic} that nobody talks about:",
            f"🚀 The {topic} framework that changed my career (thread):",
            f"❌ Stop doing this with {topic}. Here's what works better:",
            f"📈 How I used {topic} to [achieve result] in 30 days:",
            f"🤔 Unpopular opinion about {topic}:",
            f"✅ The beginner's guide to {topic} (save this post):",
        ]
        ideas = templates[:count]
        return "LinkedIn Post Ideas:\n\n" + "\n\n".join(
            [f"{i+1}. {idea}" for i, idea in enumerate(ideas)]
        )

    @mcp.tool()
    def draft_linkedin_article(title: str, key_points: str) -> str:
        """
        Draft a structured LinkedIn article outline.
        
        Args:
            title: Article title
            key_points: Comma-separated key points to cover
        """
        points = [p.strip() for p in key_points.split(",")]
        article = f"# {title}\n\n"
        article += "## Introduction\n[Hook your reader with a compelling opening]\n\n"

        for i, point in enumerate(points, 1):
            article += f"## {i}. {point}\n[Expand on this point with examples and data]\n\n"

        article += "## Key Takeaways\n[Summarize the main insights]\n\n"
        article += "## Call to Action\n[What should the reader do next?]\n\n"
        article += "---\n*What are your thoughts? Drop a comment below.*\n"

        return article
