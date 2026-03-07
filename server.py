"""
NexusLink AI — AI-Powered LinkedIn Intelligence
A remote MCP connector for Claude that integrates with LinkedIn's API.
"""

import os
import json
import logging
import uvicorn
from mcp.server.fastmcp import FastMCP

# Initialize MCP Server
mcp = FastMCP("NexusLink AI")

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

app = mcp.sse_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    logger.info(f"🚀 NexusLink AI MCP Server starting on 0.0.0.0:{port}...")
    uvicorn.run(app, host="0.0.0.0", port=port)
```

Also add `uvicorn` to the requirements. Go to **requirements.txt** → edit, and replace with:
```
mcp[cli]>=1.0.0
python-dotenv>=1.0.0
httpx>=0.25.0
uvicorn>=0.30.0
starlette
