import os
import logging
from mcp.server.fastmcp import FastMCP

port = int(os.environ.get("PORT", 8000))

mcp = FastMCP("NexusLink AI", host="0.0.0.0", port=port)

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

if __name__ == "__main__":
    logger.info(f"NexusLink AI MCP Server starting on 0.0.0.0:{port}")
    mcp.run(transport="sse")
```

Key changes: `host` and `port` moved into `FastMCP()` constructor, removed uvicorn. Also update **requirements.txt** — remove uvicorn and starlette:
```
mcp[cli]>=1.0.0
python-dotenv>=1.0.0
httpx>=0.25.0
