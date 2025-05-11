# Explorer APIs - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/tutorials/blockchain-indexing/explorer-apis/](https://docs.ergoplatform.com/dev/tutorials/blockchain-indexing/explorer-apis/)
Generated: 2025-05-11

## Summary
One of the simplest ways to access indexed Ergo blockchain data for your dApp or service is by utilizing the public APIs provided by blockchain explorers. This approach avoids the need to run your own node or indexer but comes with trade-offs regarding control, performance, and flexibility. Public explorers like explorer.ergoplatform.com, ergexplorer.com, and sigmaspace.io maintain their own indexed databases of the Ergo blockchain. They expose this data through public APIs, often RESTful, allowing developers to query for information programmatically. Below are examples of common endpoints available from the main Ergo Explorer API (api.ergoplatform.com).

## Keywords
ergo, blockchain, datum, dapp, service, explorer, approach, need, node, indexer, trade, control, performance, flexibility, explorer.ergoplatform.com, sigmaspace.io, database, developer, information, below

## Content
## Indexing Strategy: Using Public Explorer APIs#
One of the simplest ways to access indexed Ergo blockchain data for your dApp or service is by utilizing the public APIs provided by blockchain explorers. This approach avoids the need to run your own node or indexer but comes with trade-offs regarding control, performance, and flexibility.

### Concept#
Public explorers like explorer.ergoplatform.com, ergexplorer.com, and sigmaspace.io maintain their own indexed databases of the Ergo blockchain. They expose this data through public APIs, often RESTful, allowing developers to query for information programmatically.

### How It Works#
Identify Explorer & API Docs: Choose an explorer whose API provides the endpoints you need. Review their API documentation carefully to understand available queries, request/response formats, authentication (if any), and usage limitations (especially rate limits).
Ergo Explorer API Docs: api.ergoplatform.com/api/v1/docs/
ErgExplorer API Docs: ergexplorer.com/api/v1/docs/


Make API Requests: Your application makes standard HTTP requests (GET, POST, etc.) to the explorer's API endpoints using libraries like axios (JS/TS), requests (Python), or built-in fetch functions.
Process Response: Your application parses the JSON (or other format) response from the API and uses the data. Implement robust error handling for network issues, API errors (like 404 Not Found or 429 Too Many Requests), and unexpected response formats.

### Common API Endpoints#
Below are examples of common endpoints available from the main Ergo Explorer API (api.ergoplatform.com). Other explorers often provide similar functionality, but check their specific documentation.

#### Ergo Explorer API (api.ergoplatform.com)#
Endpoint
Description
Example URL




/api/v1/addresses/{address}
Get address summary info
https://api.ergoplatform.com/api/v1/addresses/9iMoHi8FUVh2RdFv3YD6xjjfxZ6nPqEjQbmxQzHbpBFE6hWxouq


/api/v1/addresses/{address}/transactions
Get address transactions
https://api.ergoplatform.com/api/v1/addresses/9iMoHi8FUVh2RdFv3YD6xjjfxZ6nPqEjQbmxQzHbpBFE6hWxouq/transactions


/api/v1/addresses/{address}/balance/confirmed
Get confirmed balance
https://api.ergoplatform.com/api/v1/addresses/9iMoHi8FUVh2RdFv3YD6xjjfxZ6nPqEjQbmxQzHbpBFE6hWxouq/balance/confirmed


/api/v1/boxes/unspent/byAddress/{address}
Get unspent boxes by address
https://api.ergoplatform.com/api/v1/boxes/unspent/byAddress/9iMoHi8FUVh2RdFv3YD6xjjfxZ6nPqEjQbmxQzHbpBFE6hWxouq


/api/v1/boxes/unspent/byErgoTree/{ergoTree}
Get unspent boxes by ErgoTree
https://api.ergoplatform.com/api/v1/boxes/unspent/byErgoTree/{ergoTreeHex}


/api/v1/boxes/unspent/byTokenId/{tokenId}
Get unspent boxes containing token
https://api.ergoplatform.com/api/v1/boxes/unspent/byTokenId/03faf2cb329f2e90d6d23b58d91bbb6c046aa143261cc21f52fbe2824bfcbf04


/api/v1/boxes/{boxId}
Get box by ID
https://api.ergoplatform.com/api/v1/boxes/851dd1bdd06a0f0f8e7a0e0a8e7a0e0a8e7a0e0a8e7a0e0a8e7a0e0a8e7a0e0a


/api/v1/transactions/{txId}
Get transaction by ID
https://api.ergoplatform.com/api/v1/transactions/851dd1bdd06a0f0f8e7a0e0a8e7a0e0a8e7a0e0a8e7a0e0a8e7a0e0a8e7a0e0a


/api/v1/tokens/{tokenId}
Get token information
https://api.ergoplatform.com/api/v1/tokens/03faf2cb329f2e90d6d23b58d91bbb6c046aa143261cc21f52fbe2824bfcbf04


/api/v1/blocks/{blockId}
Get block by ID
https://api.ergoplatform.com/api/v1/blocks/851dd1bdd06a0f0f8e7a0e0a8e7a0e0a8e7a0e0a8e7a0e0a8e7a0e0a8e7a0e0a


/api/v1/info
Get blockchain info
https://api.ergoplatform.com/api/v1/info
(Note: Replace placeholders like {address}, {ergoTreeHex}, {tokenId}, {boxId}, {txId}, {blockId} with actual values.)

#### JavaScript/TypeScript (with Axios)#
import axios from 'axios';

// Configuration
const explorerBaseUrl = 'https://api.ergoplatform.com/api/v1';

// Create a reusable client with error handling
const explorerClient = axios.create({
  baseURL: explorerBaseUrl,
  timeout: 10000, // 10 second timeout
  headers: {
    'Accept': 'application/json',
  }
});

// Add response interceptor for detailed error logging
explorerClient.interceptors.response.use(
  response => response,
  error => {
    if (error.response) {
      // Request made and server responded with a status code outside 2xx range
      console.error('Explorer API Error:', error.response.status, error.response.data);
    } else if (error.request) {
      // Request made but no response received
      console.error('Explorer API No Response:', error.request);
    } else {
      // Error setting up the request
      console.error('Explorer API Request Setup Error:', error.message);
    }
    return Promise.reject(error); // Propagate the error
  }
);

// Get address information
async function getAddressInfo(address: string) {
  try {
    const response = await explorerClient.get(`/addresses/${address}`);
    return response.data;
  } catch (error) {
    console.error(`Failed to get info for address ${address}`);
    // Optionally return null or a default object instead of throwing
    return null; 
  }
}

// Get address balance (confirmed)
async function getAddressBalance(address: string) {
  try {
    const response = await explorerClient.get(`/addresses/${address}/balance/confirmed`);
    return response.data;
  } catch (error) {
    console.error(`Failed to get balance for address ${address}`);
    return null;
  }
}

// Get unspent boxes for an address (first page)
async function getUnspentBoxes(address: string, limit: number = 50) {
  try {
    // API might use 'items' array and 'total' count for pagination
    const response = await explorerClient.get(`/boxes/unspent/byAddress/${address}`, { params: { limit } });
    return response.data.ite...

#### Python Example#
import requests
import time
from typing import Dict, List, Any, Optional

class ErgoExplorerClient:
    """A simple client for interacting with the Ergo Explorer API v1."""

    def __init__(self, base_url: str = "https://api.ergoplatform.com/api/v1"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/json",
            "User-Agent": "ErgoDocsPythonClient/1.0" # Good practice to identify your client
        })

    def _request(self, method: str, endpoint: str, **kwargs) -> Optional[Dict[str, Any]]:
        """Internal method to handle API requests with retries and error logging."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        max_retries = 3
        retry_delay = 1  # seconds

        for attempt in range(max_retries):
            try:
                response = self.session.request(method, url, timeout=10, **kwargs) # 10 second timeout
                response.raise_for_status() # Raises HTTPError for bad responses (4xx or 5xx)
                return response.json()
            except requests.exceptions.HTTPError as e:
                print(f"HTTP Error: {e.response.status_code} for URL {url}. Response: {e.response.text}")
                if e.response.status_code == 429: # Rate limited
                    retry_after = int(e.response.headers.get('Retry-After', retry_delay))
                    print(f"Rate limited. Retrying after {retry_after} seconds...")
                    time.sleep(retry_after)
                    retry_delay = retry_after + 1 # Add buffer
                elif attempt < max_retries - 1:
                    print(f"Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                    retry_delay *= 2 # Exponential backoff
                else:
                    print(f"Request failed after {max_retries} attempts.")
                    return None # Return None on final failure
            exc...

### Rate Limiting and Best Practices#
Public APIs are shared resources. To ensure reliable operation and avoid being blocked, follow these best practices:
Understand Rate Limits: Check the API documentation or community resources for stated rate limits (e.g., requests per second per IP). The main Ergo Explorer API often has limits around 10-20 req/sec. Exceeding limits can lead to 429 Too Many Requests errors or temporary IP bans.
Implement Caching: Avoid fetching the same data repeatedly. Cache responses locally (in memory for short durations, or using persistent stores like Redis for longer) with appropriate Time-To-Live (TTL) values. Re-fetch only when the cache expires or specific events indicate data might have changed.
    // Simple in-memory cache concept (JS)
const cache = new Map();
const CACHE_TTL = 60000; // 1 minute

async function getCachedData(url) {
  const now = Date.now();
  if (cache.has(url) && (now - cache.get(url).timestamp < CACHE_TTL)) {
    return cache.get(url).data;
  }
  // Fetch fresh data if not cached or expired
  const response = await fetch(url); // Use fetchWithRetry here
  if (!response.ok) throw new Error(`API Error: ${response.status}`);
  const data = await response.json();
  cache.set(url, { data, timestamp: now });
  return data;
}

Use Retry Logic with Exponential Backoff: If a request fails (especially due to rate limiting or transient network issues), don't immediately retry. Wait for a short period and increase the delay exponentially for subsequent retries. Respect the Retry-After header if provided in a 429 response.
    # Conceptual retry logic within the Python client's _request method (see above)
# Handles retries with increasing delay for transient errors and respects Retry-After

Be Specific: Request only the data you need. Use API parameters (limit, offset, specific endpoints) to narrow down results instead of fetching large datasets and filtering client-side.
Identify Your Client: Use a descriptive User-Agent header in your requests so API providers ca...

### Pros & Cons Summary#
Pros: Simple to start, convenient endpoints.
Cons: Third-party reliance, rate limits, limited query flexibility, potential latency, centralization risk.

### When to Use#
Simple applications, prototypes, low-volume tools.
When reliance on a third party is acceptable.
When required data fits well with available API endpoints.
While convenient, the limitations often lead developers towards more robust solutions for production applications.
