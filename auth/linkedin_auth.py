"""
LinkedIn OAuth 2.0 Authentication Helper
"""

import os
import urllib.parse
import json
from http.client import HTTPSConnection

CLIENT_ID = os.getenv("LINKEDIN_CLIENT_ID", "")
CLIENT_SECRET = os.getenv("LINKEDIN_CLIENT_SECRET", "")
ACCESS_TOKEN = os.getenv("LINKEDIN_ACCESS_TOKEN", "")
REDIRECT_URI = os.getenv("REDIRECT_URI", "http://localhost:8000/callback")
SCOPES = "openid profile email w_member_social"


def get_auth_url():
    """Generate LinkedIn OAuth authorization URL"""
    params = urllib.parse.urlencode({
        "response_type": "code",
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPES,
    })
    return f"https://www.linkedin.com/oauth/v2/authorization?{params}"


def exchange_code_for_token(code):
    """Exchange authorization code for access token"""
    conn = HTTPSConnection("www.linkedin.com")
    params = urllib.parse.urlencode({
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    })
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    conn.request("POST", "/oauth/v2/accessToken", params, headers)
    response = conn.getresponse()
    return json.loads(response.read().decode())


def get_headers():
    """Return authorization headers for LinkedIn API calls"""
    return {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0",
    }


def linkedin_api_get(endpoint):
    """Make a GET request to LinkedIn API"""
    conn = HTTPSConnection("api.linkedin.com")
    conn.request("GET", endpoint, headers=get_headers())
    response = conn.getresponse()
    return json.loads(response.read().decode())


def linkedin_api_post(endpoint, data):
    """Make a POST request to LinkedIn API"""
    conn = HTTPSConnection("api.linkedin.com")
    conn.request("POST", endpoint, json.dumps(data), get_headers())
    response = conn.getresponse()
    return json.loads(response.read().decode())
