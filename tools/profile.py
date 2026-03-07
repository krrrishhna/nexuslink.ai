"""
NexusLink AI — Profile Analysis Tools
"""

from auth.linkedin_auth import linkedin_api_get


def register_profile_tools(mcp):

    @mcp.tool()
    def get_my_profile() -> str:
        """Fetch your LinkedIn profile information including name, headline, and vanity URL."""
        try:
            data = linkedin_api_get("/v2/userinfo")
            return (
                f"Name: {data.get('name', 'N/A')}\n"
                f"Email: {data.get('email', 'N/A')}\n"
                f"Picture: {data.get('picture', 'N/A')}\n"
                f"Locale: {data.get('locale', {}).get('language', 'N/A')}"
            )
        except Exception as e:
            return f"Error fetching profile: {str(e)}"

    @mcp.tool()
    def analyze_profile_strength() -> str:
        """Analyze your LinkedIn profile and suggest improvements for visibility and engagement."""
        try:
            data = linkedin_api_get("/v2/userinfo")
            suggestions = []

            if not data.get("picture"):
                suggestions.append("📸 Add a professional profile photo — profiles with photos get 21x more views.")
            if not data.get("email"):
                suggestions.append("📧 Add a public email to make it easier for recruiters to reach you.")

            suggestions.append("✍️ Ensure your headline includes keywords relevant to your target role.")
            suggestions.append("📝 Write an About section that tells your story, not just lists skills.")
            suggestions.append("🏆 Add at least 3 featured posts or projects to your profile.")
            suggestions.append("💬 Get recommendations from colleagues or managers.")

            return "Profile Strength Analysis:\n" + "\n".join(suggestions)
        except Exception as e:
            return f"Error analyzing profile: {str(e)}"
