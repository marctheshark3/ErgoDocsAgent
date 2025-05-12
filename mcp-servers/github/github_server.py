#!/usr/bin/env python3

import os
import json
import logging
import requests
from typing import Dict, List, Any, Optional
from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('github-mcp-server')

# Get GitHub token from environment
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
if not GITHUB_TOKEN:
    logger.warning("GITHUB_TOKEN not found in environment variables. Some operations may fail.")

# Server port
PORT = int(os.environ.get('PORT', '8081'))

# Create FastAPI app
app = FastAPI(title="GitHub MCP Server")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GitHub API base URL
GITHUB_API = "https://api.github.com"

# Get GitHub headers with auth token
def get_headers() -> Dict[str, str]:
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "GitHub-MCP-Server"
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    return headers

# Define MCP JSON-RPC models
class JsonRpcRequest(BaseModel):
    jsonrpc: str
    id: Any
    method: str
    params: Optional[Dict[str, Any]] = None

class JsonRpcResponse(BaseModel):
    jsonrpc: str = "2.0"
    id: Any
    result: Optional[Any] = None
    error: Optional[Dict[str, Any]] = None

# Define MCP methods
methods = {}

def mcp_method(func):
    """Decorator to register an MCP method"""
    methods[func.__name__] = func
    return func

# GitHub MCP methods
@mcp_method
async def listRepository(params: Dict[str, Any]) -> Dict[str, Any]:
    """List files in a GitHub repository"""
    owner = params.get("owner")
    repo = params.get("repo")
    path = params.get("path", "")
    ref = params.get("ref", "main")
    
    if not owner or not repo:
        return {"error": "Owner and repo are required parameters"}
    
    url = f"{GITHUB_API}/repos/{owner}/{repo}/contents/{path}"
    response = requests.get(url, headers=get_headers(), params={"ref": ref})
    
    if response.status_code != 200:
        return {"error": f"GitHub API error: {response.status_code} {response.text}"}
    
    content = response.json()
    if isinstance(content, dict):
        # Single file
        return {"type": "file", "content": content}
    else:
        # Directory
        return {"type": "directory", "items": content}

@mcp_method
async def getFileContent(params: Dict[str, Any]) -> Dict[str, Any]:
    """Get content of a file in a GitHub repository"""
    owner = params.get("owner")
    repo = params.get("repo")
    path = params.get("path")
    ref = params.get("ref", "main")
    
    if not owner or not repo or not path:
        return {"error": "Owner, repo, and path are required parameters"}
    
    url = f"{GITHUB_API}/repos/{owner}/{repo}/contents/{path}"
    response = requests.get(url, headers=get_headers(), params={"ref": ref})
    
    if response.status_code != 200:
        return {"error": f"GitHub API error: {response.status_code} {response.text}"}
    
    content = response.json()
    if "content" not in content:
        return {"error": "No content found"}
    
    import base64
    decoded_content = base64.b64decode(content["content"]).decode("utf-8")
    return {
        "content": decoded_content,
        "sha": content.get("sha"),
        "size": content.get("size"),
        "name": content.get("name"),
        "path": content.get("path"),
        "url": content.get("html_url")
    }

@mcp_method
async def searchRepositories(params: Dict[str, Any]) -> Dict[str, Any]:
    """Search GitHub repositories"""
    query = params.get("query")
    sort = params.get("sort", "updated")
    order = params.get("order", "desc")
    per_page = params.get("per_page", 30)
    page = params.get("page", 1)
    
    if not query:
        return {"error": "Query is a required parameter"}
    
    url = f"{GITHUB_API}/search/repositories"
    response = requests.get(
        url, 
        headers=get_headers(), 
        params={
            "q": query,
            "sort": sort,
            "order": order,
            "per_page": per_page,
            "page": page
        }
    )
    
    if response.status_code != 200:
        return {"error": f"GitHub API error: {response.status_code} {response.text}"}
    
    data = response.json()
    return {
        "total_count": data.get("total_count", 0),
        "items": data.get("items", [])
    }

@mcp_method
async def getRepository(params: Dict[str, Any]) -> Dict[str, Any]:
    """Get information about a GitHub repository"""
    owner = params.get("owner")
    repo = params.get("repo")
    
    if not owner or not repo:
        return {"error": "Owner and repo are required parameters"}
    
    url = f"{GITHUB_API}/repos/{owner}/{repo}"
    response = requests.get(url, headers=get_headers())
    
    if response.status_code != 200:
        return {"error": f"GitHub API error: {response.status_code} {response.text}"}
    
    return response.json()

@mcp_method
async def getCommits(params: Dict[str, Any]) -> Dict[str, Any]:
    """Get commits for a repository"""
    owner = params.get("owner")
    repo = params.get("repo")
    path = params.get("path")
    since = params.get("since")
    until = params.get("until")
    per_page = params.get("per_page", 30)
    page = params.get("page", 1)
    
    if not owner or not repo:
        return {"error": "Owner and repo are required parameters"}
    
    url = f"{GITHUB_API}/repos/{owner}/{repo}/commits"
    query_params = {"per_page": per_page, "page": page}
    
    if path:
        query_params["path"] = path
    if since:
        query_params["since"] = since
    if until:
        query_params["until"] = until
    
    response = requests.get(url, headers=get_headers(), params=query_params)
    
    if response.status_code != 200:
        return {"error": f"GitHub API error: {response.status_code} {response.text}"}
    
    return {"commits": response.json()}

# MCP JSON-RPC endpoint
@app.post("/api/request")
async def handle_request(request_data: JsonRpcRequest) -> JsonRpcResponse:
    """Handle an MCP JSON-RPC request"""
    method_name = request_data.method
    
    if method_name not in methods:
        logger.error(f"Method not found: {method_name}")
        return JsonRpcResponse(
            id=request_data.id,
            error={"code": -32601, "message": f"Method not found: {method_name}"}
        )
    
    try:
        logger.info(f"Executing method: {method_name}")
        result = await methods[method_name](request_data.params or {})
        return JsonRpcResponse(id=request_data.id, result=result)
    except Exception as e:
        logger.exception(f"Error in method {method_name}: {str(e)}")
        return JsonRpcResponse(
            id=request_data.id,
            error={"code": -32000, "message": f"Server error: {str(e)}"}
        )

# MCP Server info endpoint
@app.get("/")
async def get_server_info():
    """Return information about this MCP server"""
    return {
        "name": "GitHub MCP Server",
        "version": "1.0.0",
        "description": "MCP Server for GitHub API access",
        "methods": list(methods.keys())
    }

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok"}

# Run the server
if __name__ == "__main__":
    import uvicorn
    logger.info(f"Starting GitHub MCP Server on port {PORT}")
    uvicorn.run(app, host="0.0.0.0", port=PORT) 