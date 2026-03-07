import os
import logging
import uvicorn
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("NexusLink AI")

from tools.profile import register_profile_tools
from tools.content import register_content_tools
from tools.jobs import register_jobs_tools
from tools.network import register_network_tools
from tools.branding import register_branding_tools

register_profile_tools(mcp)
register_content_tools(mcp)
register_jobs_tools(mcp)
register_network_tools(mcp)
register_branding_tools(mcp)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("nexuslink")

app = mcp.sse_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    logger.info(f"NexusLink AI MCP Server starting on 0.0.0.0:{port}")
    uvicorn.run(app, host="0.0.0.0", port=port)
