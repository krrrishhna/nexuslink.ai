"""
NexusLink AI — Personal Branding Tools
"""


def register_branding_tools(mcp):

    @mcp.tool()
    def generate_headline(role: str, specialties: str, style: str = "professional") -> str:
        """
        Generate LinkedIn headline options optimized for search and engagement.
        
        Args:
            role: Your current or target role
            specialties: Comma-separated areas of expertise
            style: Headline style — professional, creative, or bold
        """
        specs = [s.strip() for s in specialties.split(",")]

        headlines = {
            "professional": [
                f"{role} | {' • '.join(specs[:3])}",
                f"{role} — Helping teams leverage {specs[0]} for impact",
                f"{role} | Passionate about {specs[0]} & {specs[1] if len(specs) > 1 else 'innovation'}",
            ],
            "creative": [
                f"Turning {specs[0]} into business outcomes | {role}",
                f"{specs[0]} nerd → {role} | Building what's next",
                f"I make {specs[0]} make sense | {role}",
            ],
            "bold": [
                f"{role} who actually ships 🚀 | {' | '.join(specs[:2])}",
                f"Not your average {role} | {specs[0]} × {specs[1] if len(specs) > 1 else 'Strategy'}",
                f"{role} | {specs[0]} obsessed | Let's build something great",
            ],
        }

        options = headlines.get(style, headlines["professional"])
        return f"LinkedIn Headline Options ({style}):\n\n" + "\n".join(
            [f"{i+1}. {h}" for i, h in enumerate(options)]
        )

    @mcp.tool()
    def audit_about_section(current_about: str) -> str:
        """
        Audit your LinkedIn About section and provide improvement suggestions.
        
        Args:
            current_about: Your current About/Summary section text
        """
        word_count = len(current_about.split())
        has_hook = current_about[0].isupper() and len(current_about.split(".")[0].split()) < 15
        has_cta = any(word in current_about.lower() for word in ["reach out", "connect", "email", "message", "contact"])
        has_metrics = any(char.isdigit() for char in current_about)

        audit = "📝 About Section Audit:\n\n"
        audit += f"Word count: {word_count} "
        audit += "✅\n" if 150 <= word_count <= 400 else "⚠️ (aim for 150-400 words)\n"
        audit += f"Strong hook: {'✅' if has_hook else '❌ Start with a compelling first sentence'}\n"
        audit += f"Call to action: {'✅' if has_cta else '❌ Add a CTA at the end'}\n"
        audit += f"Metrics/numbers: {'✅' if has_metrics else '❌ Add quantifiable achievements'}\n"

        audit += "\n💡 Pro tips:\n"
        audit += "• First 3 lines are visible before 'See more' — make them count\n"
        audit += "• Use short paragraphs and white space\n"
        audit += "• Include industry keywords for SEO\n"
        audit += "• Tell a story, don't just list accomplishments"

        return audit

    @mcp.tool()
    def content_calendar(niche: str, weeks: int = 4) -> str:
        """
        Generate a LinkedIn content calendar for consistent posting.
        
        Args:
            niche: Your professional niche/topic area
            weeks: Number of weeks to plan (default: 4)
        """
        post_types = [
            ("Monday", "💡 Insight", f"Share a lesson learned about {niche}"),
            ("Wednesday", "📊 Data/Case Study", f"Share results, metrics, or a case study in {niche}"),
            ("Friday", "🤔 Question/Poll", f"Ask your network a thought-provoking question about {niche}"),
        ]

        calendar = f"📅 {weeks}-Week LinkedIn Content Calendar — {niche}\n\n"

        for week in range(1, weeks + 1):
            calendar += f"--- Week {week} ---\n"
            for day, post_type, description in post_types:
                calendar += f"  {day}: {post_type}\n    → {description}\n"
            calendar += "\n"

        calendar += "🎯 Tips:\n"
        calendar += "• Post between 8-10 AM your timezone\n"
        calendar += "• Engage with 5 posts before and after publishing\n"
        calendar += "• Repurpose top-performing posts every 6 weeks"

        return calendar
