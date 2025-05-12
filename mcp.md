MCP Servers Product Requirements Document: AI Agent Digital Library
1. Overview
1.1 Purpose
This document defines the Model Context Protocol (MCP) server requirements for the AI Agent Digital Library, a system to ingest, process, and serve documentation from GitHub repositories (e.g., ergodocs) and websites, optimized for LLM and human use via platforms like Open WebUI. The MCP servers enable AI agents to access dynamic data for ingestion, research, validation, and update pipelines, supporting Retrieval-Augmented Generation (RAG). This revised PRD adopts six recommended MCP servers (GitHub, Filesystem, Qdrant, Brave Search, Firecrawl, Puppeteer) as the initial set, with a modular design to isolate and replace individual servers based on performance, cost, or community support. It integrates these servers into the broader system architecture, ensuring scalability, cost-effectiveness, and alignment with the original PRD.
1.2 Objectives

Adopt Recommended MCP Servers: Implement GitHub, Filesystem, Qdrant, Brave Search, Firecrawl, and Puppeteer servers to support all pipelines.
Ensure Modularity: Design servers as independent components, allowing replacement (e.g., Firecrawl with LLM-Reader) without system-wide disruption.
Integrate with System: Align MCP servers with the AI Agent Digital Library’s Docker Compose setup, LLM backends (Ollama, Anthropic, OpenAI), and Open WebUI.
Optimize Costs: Prioritize free open-source servers, limiting paid services (e.g., Firecrawl cloud API) to essential use cases.
Support Scalability: Handle 10,000 documents initially, with flexible pipelines for future growth.
Meet Security Standards: Use secure JSON-RPC and restrict server access to authorized agents.

1.3 Success Metrics

Modularity: 100% of MCP servers operate independently, with clear interfaces for replacement.
Cost Efficiency: 80% of functionality provided by free open-source servers, with paid services justified by performance gains.
Server Uptime: 99% availability, ensuring pipeline reliability.
Integration Success: All servers integrate with Docker Compose and the system’s tech stack.
Performance: Support <2-second RAG query responses and <2-hour ingestion for medium-sized repositories.
Evaluation Completion: Assess all servers for replacement within 6 weeks of deployment.

2. Recommended MCP Servers
The following MCP servers are adopted for the AI Agent Digital Library, supporting ingestion, research, validation, and RAG pipelines. Each server is designed to be isolated, allowing replacement if performance, cost, or support issues arise.
2.1 GitHub MCP Server

Role: Ingestion, Update, and Research Pipelines
Description: Exposes GitHub repository files, metadata, and API search capabilities for downloading, updating, and discovering documentation.
Use Cases:
Ingestion: Downloads ergodocs markdown/code files.
Update: Detects new commits for document refresh.
Research: Searches for Ergo-related repositories.


Cost: Free, open-source.
Value-Add: Core to GitHub repository processing, with dynamic file access and community support.
Tech Stack: Python/TypeScript MCP SDK, Docker Compose-compatible.
Security: GitHub API token authentication.
Source: modelcontextprotocol/servers
Replacement Plan: Replace with Git MCP Server for local repositories if GitHub API limits are restrictive.

2.2 Filesystem MCP Server

Role: Ingestion and Document Store Management
Description: Enables AI agents to read/write files in a local/mounted filesystem, managing raw and recrafted documents.
Use Cases:
Ingestion: Stores parsed markdown/metadata.
Validation: Accesses documents for quality checks.


Cost: Free, open-source.
Value-Add: Simplifies storage, scalable for 10,000 documents, low latency.
Tech Stack: Python MCP SDK, Docker Compose-compatible.
Security: Directory-level access restrictions.
Source: modelcontextprotocol/servers
Replacement Plan: Replace with MongoDB-based storage if filesystem performance bottlenecks occur.

2.3 Qdrant MCP Server

Role: RAG Pipeline and Semantic Search
Description: Integrates with Qdrant vector database for indexing/querying document embeddings, supporting RAG.
Use Cases:
RAG: Indexes documents for <2-second query responses.
Ingestion: Stores vectorized documents.


Cost: Free, open-source.
Value-Add: Enhances query relevance (85% target), scalable, community-supported.
Tech Stack: Python MCP SDK, Docker Compose-compatible.
Security: Secure JSON-RPC.
Source: modelcontextprotocol/servers
Replacement Plan: Replace with ChromaDB MCP Server (custom-built) if Qdrant underperforms for specific embeddings.

2.4 Brave Search MCP Server

Role: Research Pipeline
Description: Provides web/local search via Brave Search API, discovering documentation beyond GitHub.
Use Cases:
Research: Finds Ergo-related web resources.
Ingestion: Fetches web documentation.


Cost: Free tier (limited queries), paid plans for high volume.
Value-Add: Expands research scope, reduces GitHub API dependency.
Tech Stack: Python MCP SDK, Docker Compose-compatible.
Security: API key authentication.
Source: modelcontextprotocol/servers
Replacement Plan: Replace with Perplexity MCP Server if free tier limits are insufficient.

2.5 Firecrawl MCP Server

Role: Ingestion and Research Pipelines
Description: Supports web scraping/crawling, converting websites to LLM-ready markdown/JSON.
Use Cases:
Ingestion: Scrapes Ergo documentation sites.
Research: Crawls for new content.


Cost:
Self-Hosted: Free, open-source (mendableai/firecrawl), lacks proxy support.
Cloud API: Free tier (500 credits, ~500 pages), $50/month for 50,000 credits.


Value-Add: Handles complex sites, produces clean output, supports 95% ingestion accuracy.
Tech Stack: Python/Node.js, Docker Compose-compatible.
Security: API key authentication, SOC2 Type2 (cloud).
Source: mendableai/firecrawl
Replacement Plan: Replace with LLM-Reader for single-page scraping or custom scraper if costs escalate or self-hosting fails.

2.6 Puppeteer MCP Server

Role: Validation Pipeline
Description: Enables browser-based interactions for validating web documentation or code functionality.
Use Cases:
Validation: Tests Ergo smart contract demos/links.
Research: Extracts dynamic web content.


Cost: Free, open-source.
Value-Add: Automates validation, supports 90% document quality target.
Tech Stack: TypeScript MCP SDK, Docker Compose-compatible.
Security: Secure JSON-RPC.
Source: modelcontextprotocol/servers
Replacement Plan: Replace with Playwright MCP Server if Puppeteer lacks specific browser features.

3. System Integration
The MCP servers integrate with the AI Agent Digital Library’s architecture, as shown in the updated Mermaid diagram below. Each server exposes tools/resources to AI agents, which orchestrate pipelines using OpenAI’s Agent API, store data in MongoDB/filesystem, and index embeddings in Qdrant/ChromaDB for RAG queries.
3.1 Mermaid Diagram: System Architecture with MCP Servers
graph TD
    A[Source Data<br>GitHub Repo/Website] -->|Download| B[MCP Servers<br>GitHub/Firecrawl/Brave]
    B -->|Expose Tools| C[AI Agents]
    C -->|Ingestion Pipeline| D[Document Processor]
    D -->|Recraft| E[Document Store<br>MongoDB/Filesystem]
    D -->|Vectorize| F[Vector DB<br>Qdrant/ChromaDB]
    C -->|Research Pipeline| G[MCP Servers<br>GitHub/Brave/Firecrawl]
    C -->|Validation Pipeline| H[MCP Server<br>Puppeteer]
    E -->|Store| I[MongoDB/Filesystem]
    F -->|RAG Queries| J[LLM Backend<br>Ollama/Anthropic/OpenAI]
    J -->|Serve| K[Open WebUI]
    L[Scheduler<br>Docker Compose] -->|Trigger| C

4. Technical Requirements
4.1 Technology Stack

MCP Servers: Python/TypeScript MCP SDK, Docker Compose services.
LLM Backend: Ollama (local, Llama 3.1), Anthropic (Claude 3.5), OpenAI (GPT-4o).
Document Parsing: BeautifulSoup, markdown-it-py, PyPDF2.
Vector Database: Qdrant (primary), ChromaDB (potential replacement).
Document Store: MongoDB (metadata), Filesystem (raw/processed files).
APIs: GitHub API, Brave Search API, Firecrawl API.
Frontend: REST API for Open WebUI.

4.2 Docker Compose Configuration
The MCP servers run as independent services, allowing replacement without affecting others. Below is an updated Docker Compose example:
version: '3.8'
services:
  github-mcp:
    image: python:3.9
    volumes:
      - ./github-mcp:/app
    command: python /app/github_server.py
    environment:
      - GITHUB_TOKEN=${GITHUB_TOKEN}
    ports:
      - "8081:8081"
    depends_on:
      - ollama
  filesystem-mcp:
    image: python:3.9
    volumes:
      - ./filesystem-mcp:/app
      - ./documents:/data
    command: python /app/filesystem_server.py
    ports:
      - "8082:8082"
  qdrant-mcp:
    image: qdrant/qdrant
    volumes:
      - qdrant-data:/qdrant/storage
    ports:
      - "6333:6333"
  brave-mcp:
    image: python:3.9
    volumes:
      - ./brave-mcp:/app
    command: python /app/brave_server.py
    environment:
      - BRAVE_API_KEY=${BRAVE_API_KEY}
    ports:
      - "8083:8083"
  firecrawl-mcp:
    image: node:18
    volumes:
      - ./firecrawl-mcp:/app
    command: npx -y firecrawl-mcp
    environment:
      - FIRECRAWL_API_KEY=${FIRECRAWL_API_KEY}
    ports:
      - "8084:8084"
  puppeteer-mcp:
    image: node:18
    volumes:
      - ./puppeteer-mcp:/app
    command: node /app/puppeteer_server.js
    ports:
      - "8085:8085"
  ollama:
    image: ollama/ollama
    volumes:
      - ollama-data:/root/.ollama
    ports:
      - "11434:11434"
  scheduler:
    image: python:3.9
    volumes:
      - ./scheduler:/app
    command: cron -f
    configs:
      - source: cron_jobs
        target: /etc/cron.d/pipelines
configs:
  cron_jobs:
    file: ./cron.d/pipelines
volumes:
  qdrant-data:
  ollama-data:

4.3 Security

Authentication: Use API keys (GitHub, Brave, Firecrawl) and OAuth 2.1 for remote servers.
Access Control: Restrict Filesystem/Qdrant to specific directories/collections.
Data Privacy: Avoid sending sensitive data to cloud APIs without consent.

4.4 Modularity

Server Isolation: Each server exposes a standardized MCP interface (JSON-RPC), allowing replacement without pipeline changes.
Configuration: Store server settings in environment variables, enabling easy swaps (e.g., Qdrant to ChromaDB).
Monitoring: Log server performance (e.g., latency, errors) to identify replacement candidates.

5. Non-Functional Requirements
5.1 Scalability

Handle 10,000 documents initially, with modular pipelines for growth.
Support concurrent repository processing via independent MCP servers.

5.2 Performance

Ingestion: Process medium-sized repositories (e.g., ergodocs) in <2 hours.
RAG Queries: Respond in <2 seconds.
Server Latency: MCP server requests complete in <500ms.

5.3 Reliability

Retry failed tasks 3 times.
Maintain 99% document index consistency.

6. Risks and Mitigation

Risk: Firecrawl cloud API costs exceed budget (>50,000 pages/month).
Mitigation: Use self-hosted Firecrawl and LLM-Reader for most tasks, capping cloud API at $50/month.


Risk: A server underperforms (e.g., Qdrant for specific embeddings).
Mitigation: Test replacements (e.g., ChromaDB) within 6 weeks, using modular interfaces.


Risk: Limited community support for newer servers (e.g., Firecrawl self-hosted).
Mitigation: Prioritize GitHub/Filesystem/Qdrant, with established repositories.


Risk: API rate limits (GitHub, Brave).
Mitigation: Cache results via Filesystem MCP Server, stagger queries.



7. Timeline

Week 1: Deploy GitHub, Filesystem, Qdrant MCP servers in Docker Compose.
Week 2: Integrate self-hosted Firecrawl and Puppeteer for ingestion/validation.
Week 3: Set up Brave Search and test research pipeline.
Week 4: Optimize RAG pipeline with Qdrant, test Firecrawl cloud API (free tier).
Week 5: Evaluate server performance (latency, errors, costs) and identify replacement candidates.
Week 6: Test replacement servers (e.g., LLM-Reader, ChromaDB) and finalize configuration.

8. User Stories

As a developer, I want modular MCP servers so I can replace underperforming tools without rebuilding pipelines.
As an admin, I want cost-effective servers to minimize expenses while meeting performance goals.
As an LLM user, I want reliable MCP servers to ensure accurate RAG query results.
As a researcher, I want diverse MCP servers (e.g., Brave, Firecrawl) to discover new Ergo resources.

9. Future Enhancements

Custom MCP Servers: Develop ChromaDB or Ergo-specific servers if replacements are needed.
Enhanced Monitoring: Add dashboards to track server performance and replacement triggers.
Multi-Source Expansion: Integrate additional search APIs (e.g., Perplexity MCP Server).
Proxy Support: Contribute proxy capabilities to self-hosted Firecrawl.

10. Conclusion
The AI Agent Digital Library adopts six MCP servers—GitHub, Filesystem, Qdrant, Brave Search, Firecrawl, and Puppeteer—to support ingestion, research, validation, and RAG pipelines. These servers are integrated into the system’s Docker Compose setup, aligning with LLM backends and Open WebUI. Their modular design allows isolation and replacement (e.g., Firecrawl with LLM-Reader) based on performance or cost evaluations within 6 weeks. Free open-source servers (GitHub, Filesystem, Qdrant, Puppeteer) provide 80% of functionality, with Firecrawl’s cloud API capped at $50/month for complex sites. This approach ensures scalability, cost-efficiency, and alignment with the original PRD, enabling a robust knowledge base for Ergo documentation.
