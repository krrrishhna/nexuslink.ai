"""
NexusLink AI — AI-Powered LinkedIn Intelligence
A remote MCP connector for Claude that integrates with LinkedIn's API.
"""

import os
import json
import logging
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

# Initialize MCP Server
mcp = FastMCP(
    "NexusLink AI",
    description="AI-Powered LinkedIn Intelligence — profile analysis, content generation, job matching, and network automation.",
)

# Import tool modules
from tools.profile import register_profile_tools
from tools.content import register_content_tools
from tools.jobs import register_jobs_tools
from tools.network import register_network_tools
from tools.branding import register_branding_tools

# Register all tools
register_profile_tools(mcp)
register_content_tools(mcp)
register_jobs_tools(mcp)
register_network_tools(mcp)
register_branding_tools(mcp)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("nexuslink")

if __name__ == "__main__":
    logger.info("🚀 NexusLink AI MCP Server starting...")
    mcp.run(transport="sse")
