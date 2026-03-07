# NexusLink AI

**AI-Powered LinkedIn Intelligence** — A remote MCP connector for Claude.

![NexusLink AI](https://img.shields.io/badge/MCP-Connector-00D4FF?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge) ![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## What is NexusLink AI?

NexusLink AI is a Model Context Protocol (MCP) connector that brings LinkedIn intelligence directly into Claude. It enables AI-powered profile analysis, content creation, job matching, network outreach, and personal branding — all through natural conversation.

## Features

### 🧑‍💼 Profile Intelligence
- Fetch and analyze your LinkedIn profile
- Profile strength scoring with actionable suggestions

### ✍️ Content Creation
- Publish posts directly to LinkedIn
- Generate engaging post ideas and article outlines
- AI-powered content calendar

### 🎯 Job Matching
- Keyword gap analysis between job descriptions and your resume
- Cover letter outline generator

### 🤝 Network Automation
- Draft personalized connection requests (within LinkedIn's 300-char limit)
- Follow-up message templates
- Strategic outreach planning

### 💎 Personal Branding
- LinkedIn headline generator (professional, creative, bold styles)
- About section audit with improvement suggestions
- Content calendar for consistent posting

## Tech Stack

- **Python 3.10+** with FastMCP
- **LinkedIn OAuth 2.0** for secure authentication
- **SSE Transport** for real-time communication
- **Deployed on Render** as a remote MCP server

## Setup

1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/nexuslink-ai.git
cd nexuslink-ai
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Configure environment
```bash
cp .env.example .env
# Fill in your LinkedIn API credentials
```

4. Run OAuth setup
```bash
python nexuslink-oauth.py
```

5. Start the server
```bash
python server.py
```

## Adding to Claude

1. Deploy to Render (or any hosting platform)
2. Go to Claude → Settings → Connectors → Add Custom Connector
3. Paste your server URL
4. Start using NexusLink AI in any conversation!

## Architecture

```
nexuslink-ai/
├── server.py              # MCP server entry point
├── auth/
│   └── linkedin_auth.py   # OAuth 2.0 + API helpers
├── tools/
│   ├── profile.py         # Profile analysis tools
│   ├── content.py         # Content creation & publishing
│   ├── jobs.py            # Job matching & career tools
│   ├── network.py         # Network & outreach automation
│   └── branding.py        # Personal branding tools
├── requirements.txt
├── render.yaml            # Render deployment config
└── .env.example
```

## License

MIT

---

Built by **Krishna Sharma** — *AI-Powered LinkedIn Intelligence*
