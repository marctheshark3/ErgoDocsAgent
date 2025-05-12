# MCP Servers Setup Guide

This guide provides detailed instructions for setting up the Model Context Protocol (MCP) servers required for the AI Agent Digital Library.

## Table of Contents
1. [GitHub MCP Server](#github-mcp-server)
2. [Filesystem MCP Server](#filesystem-mcp-server)
3. [Qdrant MCP Server](#qdrant-mcp-server)
4. [Brave Search MCP Server](#brave-search-mcp-server)
5. [Firecrawl MCP Server](#firecrawl-mcp-server)
6. [Running All Servers](#running-all-servers)

## Prerequisites

- Node.js 18+ and NPM
- Python 3.9+
- Docker and Docker Compose (optional for containerized setup)
- Git

## Initial Setup

First, create the necessary directory structure:

```bash
mkdir -p mcp-servers/{github,filesystem,qdrant,brave}
mkdir -p documents
```

## GitHub MCP Server

The GitHub MCP Server provides access to GitHub repositories for ingestion, updates, and research.

### Setup Instructions

1. **Create a GitHub Personal Access Token (PAT)**:
   - Go to [GitHub Developer Settings](https://github.com/settings/tokens)
   - Click "Generate new token" → "Generate new token (classic)"
   - Select at minimum the following scopes: `repo`, `read:packages`
   - Copy the generated token

2. **Server Installation**:
   ```bash
   cd mcp-servers/github
   pip install mcp-sdk requests
   ```

3. **Create Server Script**:
   Create `github_server.py` with the implementation from the MCP SDK examples or the modelcontextprotocol/servers repository.

4. **Configuration**:
   - Update `.cursor/mcp.json` with your GitHub token:
   ```json
   "github-mcp": {
     "env": {
       "GITHUB_TOKEN": "YOUR_GITHUB_TOKEN_HERE"
     }
   }
   ```

### Testing

To test the GitHub MCP Server:
```bash
python mcp-servers/github/github_server.py
```

The server should start on port 8081. You can test with a simple curl command:
```bash
curl -X POST http://localhost:8081/api/request -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","id":1,"method":"listRepository","params":{"owner":"ergoplatform","repo":"ergodocs"}}'
```

## Filesystem MCP Server

The Filesystem MCP Server enables reading and writing files, essential for document storage and management.

### Setup Instructions

1. **Server Installation**:
   ```bash
   cd mcp-servers/filesystem
   pip install mcp-sdk
   ```

2. **Create Server Script**:
   Create `filesystem_server.py` with the implementation from the MCP SDK examples.

3. **Configuration**:
   - Ensure the data directory exists:
   ```bash
   mkdir -p documents
   ```
   
   - Update `.cursor/mcp.json` to specify the data directory:
   ```json
   "filesystem-mcp": {
     "env": {
       "DATA_DIR": "./documents"
     }
   }
   ```

### Testing

To test the Filesystem MCP Server:
```bash
python mcp-servers/filesystem/filesystem_server.py
```

## Qdrant MCP Server

The Qdrant MCP Server integrates with the Qdrant vector database for RAG capabilities.

### Setup Instructions

1. **Install Qdrant**:
   
   Using Docker:
   ```bash
   docker pull qdrant/qdrant
   docker run -d -p 6333:6333 -p 6334:6334 -v $(pwd)/qdrant_data:/qdrant/storage qdrant/qdrant
   ```
   
   Or follow the [official installation guide](https://qdrant.tech/documentation/guides/installation/).

2. **Server Installation**:
   ```bash
   cd mcp-servers/qdrant
   pip install mcp-sdk qdrant-client
   ```

3. **Create Server Script**:
   Create `qdrant_server.py` with the implementation for connecting to Qdrant.

4. **Configuration**:
   - Update `.cursor/mcp.json` with Qdrant connection details:
   ```json
   "qdrant-mcp": {
     "env": {
       "QDRANT_HOST": "localhost",
       "QDRANT_PORT": "6333"
     }
   }
   ```

### Testing

To test the Qdrant MCP Server:
```bash
python mcp-servers/qdrant/qdrant_server.py
```

## Brave Search MCP Server

The Brave Search MCP Server provides web search capabilities via the Brave Search API.

### Setup Instructions

1. **Get a Brave Search API Key**:
   - Go to [Brave Search API](https://brave.com/search/api/)
   - Sign up for the API access
   - Generate and copy your API key

2. **Server Installation**:
   ```bash
   cd mcp-servers/brave
   pip install mcp-sdk requests
   ```

3. **Create Server Script**:
   Create `brave_server.py` with the implementation to connect to Brave Search API.

4. **Configuration**:
   - Update `.cursor/mcp.json` with your Brave API key:
   ```json
   "brave-mcp": {
     "env": {
       "BRAVE_API_KEY": "YOUR_BRAVE_API_KEY_HERE"
     }
   }
   ```

### Testing

To test the Brave Search MCP Server:
```bash
python mcp-servers/brave/brave_server.py
```

## Firecrawl MCP Server

The Firecrawl MCP Server provides web scraping and crawling capabilities, with both self-hosted and cloud API options.

### Setup Instructions

#### Option 1: Using the Cloud API (Recommended for Beginners)

1. **Get a Firecrawl API Key**:
   - Sign up at [Firecrawl](https://firecrawl.dev/)
   - Generate and copy your API key
   - Note: Free tier includes 500 credits (~500 pages)

2. **Server Installation**:
   ```bash
   npm install -g firecrawl-mcp
   ```

3. **Configuration**:
   - Update `.cursor/mcp.json` with your Firecrawl API key:
   ```json
   "firecrawl-mcp": {
     "env": {
       "FIRECRAWL_API_KEY": "YOUR_FIRECRAWL_API_KEY_HERE"
     }
   }
   ```

#### Option 2: Self-Hosted Firecrawl (Advanced)

1. **Clone and Install Firecrawl**:
   ```bash
   git clone https://github.com/mendableai/firecrawl.git
   cd firecrawl
   npm install
   ```

2. **Build and Configure**:
   Follow the self-hosting instructions in the repository README.

### Testing

To test the Firecrawl MCP Server (cloud API):
```bash
npx firecrawl-mcp
```

## Running All Servers

### Option A: Manual Start

You can start each server in separate terminal windows:

```bash
# Terminal 1
python mcp-servers/github/github_server.py

# Terminal 2
python mcp-servers/filesystem/filesystem_server.py

# Terminal 3
python mcp-servers/qdrant/qdrant_server.py

# Terminal 4
python mcp-servers/brave/brave_server.py

# Terminal 5
npx firecrawl-mcp
```

### Option B: Using Docker Compose

For a containerized setup, create a `docker-compose.yml` file:

```yaml
version: '3.8'
services:
  github-mcp:
    image: python:3.9
    volumes:
      - ./mcp-servers/github:/app
    command: python /app/github_server.py
    environment:
      - GITHUB_TOKEN=${GITHUB_TOKEN}
    ports:
      - "8081:8081"

  filesystem-mcp:
    image: python:3.9
    volumes:
      - ./mcp-servers/filesystem:/app
      - ./documents:/data
    command: python /app/filesystem_server.py
    ports:
      - "8082:8082"
    environment:
      - DATA_DIR=/data

  qdrant-mcp:
    image: python:3.9
    volumes:
      - ./mcp-servers/qdrant:/app
    command: python /app/qdrant_server.py
    ports:
      - "8083:8083"
    depends_on:
      - qdrant
    environment:
      - QDRANT_HOST=qdrant
      - QDRANT_PORT=6333

  qdrant:
    image: qdrant/qdrant
    volumes:
      - qdrant-data:/qdrant/storage
    ports:
      - "6333:6333"

  brave-mcp:
    image: python:3.9
    volumes:
      - ./mcp-servers/brave:/app
    command: python /app/brave_server.py
    environment:
      - BRAVE_API_KEY=${BRAVE_API_KEY}
    ports:
      - "8084:8084"

  firecrawl-mcp:
    image: node:18
    volumes:
      - ./firecrawl-mcp:/app
    command: npx -y firecrawl-mcp
    environment:
      - FIRECRAWL_API_KEY=${FIRECRAWL_API_KEY}
    ports:
      - "8085:8085"

volumes:
  qdrant-data:
```

Start all services:
```bash
docker-compose up -d
```

## Troubleshooting

### Common Issues

1. **Port Conflicts**:
   - If a port is already in use, change the port number in both the server configuration and the `.cursor/mcp.json` file.

2. **API Rate Limits**:
   - GitHub and Brave Search have rate limits. If you hit them, implement caching or stagger your requests.

3. **Missing Dependencies**:
   - Ensure all Python and Node.js dependencies are installed.

4. **Docker Issues**:
   - If using Docker, ensure the service has proper network access and volume mounts.

### Getting Help

- Refer to the [Model Context Protocol documentation](https://github.com/anthropics/anthropic-cookbook/tree/main/model_context_protocol)
- Check server-specific repositories for more detailed setup instructions 