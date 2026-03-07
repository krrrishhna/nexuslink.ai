"""
NexusLink AI — Network & Outreach Tools
"""


def register_network_tools(mcp):

    @mcp.tool()
    def draft_connection_request(name: str, context: str, goal: str) -> str:
        """
        Draft a personalized LinkedIn connection request message (under 300 chars).
        
        Args:
            name: Person's first name
            context: How you know them or why you're reaching out
            goal: What you hope to get from connecting
        """
        templates = [
            f"Hi {name}, {context}. I'd love to connect and learn more about your work. {goal}",
            f"Hey {name}! {context}. Would be great to connect — {goal.lower()}.",
            f"{name}, {context}. I think we could have some great conversations. {goal}",
        ]

        # Return shortest one that fits LinkedIn's 300 char limit
        for t in sorted(templates, key=len):
            if len(t) <= 300:
                return f"Connection Request Draft ({len(t)} chars):\n\n{t}"

        return f"⚠️ Message too long. Try shorter context/goal.\n\nBest attempt ({len(templates[1])} chars):\n{templates[1]}"

    @mcp.tool()
    def draft_follow_up_message(name: str, previous_interaction: str, next_step: str) -> str:
        """
        Draft a follow-up message after an initial interaction.
        
        Args:
            name: Person's first name
            previous_interaction: What you discussed or where you met
            next_step: What you'd like to happen next
        """
        message = f"""Hi {name},

Great connecting with you! {previous_interaction}

I've been thinking about our conversation and wanted to follow up. {next_step}

Would love to continue the discussion — let me know what works for you.

Best regards"""

        return f"Follow-Up Draft:\n\n{message}"

    @mcp.tool()
    def outreach_strategy(target_role: str, industry: str, count: int = 5) -> str:
        """
        Generate a networking outreach strategy for reaching specific professionals.
        
        Args:
            target_role: The role/title of people you want to connect with
            industry: Target industry
            count: Number of outreach approaches to suggest
        """
        strategies = [
            f"1. Comment thoughtfully on posts by {target_role}s in {industry} for 2 weeks before connecting",
            f"2. Join LinkedIn groups focused on {industry} — engage first, connect second",
            f"3. Share original content about {industry} trends to attract inbound connections",
            f"4. Ask mutual connections for warm introductions to {target_role}s",
            f"5. Attend virtual {industry} events and reference them in connection requests",
            f"6. Write a LinkedIn article tagging {target_role}s whose work you admire",
            f"7. Engage with {industry} company pages to get on their radar",
        ]

        return f"🎯 Outreach Strategy for {target_role}s in {industry}:\n\n" + "\n\n".join(strategies[:count])
