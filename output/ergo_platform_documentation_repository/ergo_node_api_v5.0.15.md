# Ergo Node API v5.0.15
Source: docs/node/swagger/openapi.md
Generated: 2025-05-11

## Summary
# Ergo Node API v5.0.15


/// admonition | Getting Started! API docs for Ergo Node. Scroll down for code samples, example requests and responses
///



Base URLs: * <a href="http://213.239.193.208:9053">http://213.239.193.208:9053</a>

## Authentication

* API Key (ApiKeyAuth)
    - Parameter Name: **api_key**, in: header. ## UTXO

### getSnapshotsInfo

>

## Keywords
ergo, node, admonition, code, sample, example, request, response, base, href="http://213.239.193.208:9053">http://213.239.193.208:9053</a, authentication, apikeyauth, parameter, name, header, utxo, wget, curl, default, getsnapshotsinfo

## Content
## Ergo Node API v5.0.15
/// admonition | Getting Started!
API docs for Ergo Node. Scroll down for code samples, example requests and responses
///
Base URLs:
http://213.239.193.208:9053

### Authentication
API Key (ApiKeyAuth)
Parameter Name: api_key, in: header.

#### getSnapshotsInfo
Code samples
=== "shell"
```shell
## You can also use wget
curl -X DEFAULT /utxo/getSnapshotsInfo
```
=== "http"
```http
DEFAULT /utxo/getSnapshotsInfo HTTP/1.1
```
=== "javascript"
```javascript

fetch('/utxo/getSnapshotsInfo',
{
  method: 'DEFAULT'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

result = RestClient.default '/utxo/getSnapshotsInfo',
  params: {
  }

p JSON.parse(result)
```
=== "python"
```python
import requests

r = requests.default('/utxo/getSnapshotsInfo')

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('DEFAULT','/utxo/getSnapshotsInfo', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/utxo/getSnapshotsInfo");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DEFAULT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("DEFAULT", "/utxo/getSnapshotsInfo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```
DEFAULT /utxo/getSnapshotsInfo
Error

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
This operation does not require authentication

#### getHeaderIds
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /blocks \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /blocks HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/blocks',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/blocks',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/blocks', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/blocks', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/blocks");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := ...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|limit|query|integer(int32)|false|The number of items in list to return|
|offset|query|integer(int32)|false|The first block height to include in the list|
Example responses
200 Response
=== "json"
```json
[
  "8b7ae20a4acd23e3f1bf38671ce97103ad96d8f1c780b5e5e865e4873ae16337"
]
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Array of header ids|Inline|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
Array of header ids
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
This operation does not require authentication

#### sendMinedBlock
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /blocks \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'
```
=== "http"
```http
POST /blocks HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '{
  "header": {
    "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "timestamp": 1524143059077,
    "version": 2,
    "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "nBits": 19857408,
    "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "powSolutions": {
      "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
      "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
      "n": "0000000000000000",
      "d": 987654321
    },
    "height": 667,
    "difficulty": "9575989248",
    "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "votes": "000000",
    "size": 0,
    "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
  },
  "blockTransactions": {
    "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "transactions": [
      {
        "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "inputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "spendingProof": {
              "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|FullBlock|true|none|
Example responses
default Response
=== "json"
```json
{
  "error": 500,
  "reason": "Internal server error",
  "detail": "string"
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Block is valid|None|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getFullBlockAt
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /blocks/at/{blockHeight} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /blocks/at/{blockHeight} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/blocks/at/{blockHeight}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/blocks/at/{blockHeight}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/blocks/at/{blockHeight}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/blocks/at/{blockHeight}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/blocks/at/{blockHeight}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"
       "net/http"
)
...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|blockHeight|path|integer(int32)|true|Height of a block to retrieve header ids|
Example responses
200 Response
=== "json"
```json
[
  "8b7ae20a4acd23e3f1bf38671ce97103ad96d8f1c780b5e5e865e4873ae16337"
]
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Array of header ids|Inline|
|404|Not Found|Blocks at this height doesn't exist|ApiError|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
Array of header ids
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
This operation does not require authentication

#### getChainSlice
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /blocks/chainSlice \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /blocks/chainSlice HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/blocks/chainSlice',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/blocks/chainSlice',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/blocks/chainSlice', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/blocks/chainSlice', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/blocks/chainSlice");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string]...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|fromHeight|query|integer(int32)|false|Min header height (start of the range)|
|toHeight|query|integer(int32)|false|Max header height of the range (last header height then omitted)|
Example responses
200 Response
=== "json"
```json
[
  {
    "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "timestamp": 1524143059077,
    "version": 2,
    "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "nBits": 19857408,
    "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "powSolutions": {
      "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
      "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
      "n": "0000000000000000",
      "d": 987654321
    },
    "height": 667,
    "difficulty": "9575989248",
    "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "votes": "000000",
    "size": 0,
    "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
  }
]
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Array of headers|Inline|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
Array of headers
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[BlockHeader]|false|none|Array of headers|
|» id|ModifierId(base16)|true|none|Base16-encoded 32 byte modifier id|
|» timestamp|Timestamp(int64)|true|none|Basic timestamp definition|
|» version|Version(int8)|true|none|Ergo blockchain protocol version|
|» adProofsRoot|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|» stateRoot|ADDigest(base16)|true|none|Base16-encoded 33 byte digest - digest with extra byte with tree height|
|» transactionsRoot|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|» nBits|integer(int64)|true|none|Proof-of-work target (difficulty encoded)|
|» extensionHash|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|» powSolutions|PowSolutions|true|none|An object containing all components of pow solution|
|»» pk|string|true|none|Base16-encoded public key|
|»» w|string|true|none|none|
|»» n|string|true|none|none|
|»» d|number|true|none|none|
|» height|integer(int32)|true|none|Height of the block (genesis block height == 1)|
|» difficulty|string|true|none|none|
|» parentId|ModifierId(base16)|true|none|Base16-encoded 32 byte modifier id|
|» votes|Votes(base16)|true|none|Base16-encoded votes for a soft-fork and parameters|
|» size|integer(int32)|false|none|Size of the header in bytes|
|» extensionId|ModifierId(base16)|false|none|Base16-encoded 32 byte modifier id|
|» transactionsId|ModifierId(base16)|false|none|Base16-encoded 32 byte modifier id|
|» adProofsId|ModifierId(base16)|false|none|Base16-encoded 32 byte modifier id|
This operation does not require authentication

#### getFullBlockById
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /blocks/{headerId} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /blocks/{headerId} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/blocks/{headerId}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/blocks/{headerId}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/blocks/{headerId}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/blocks/{headerId}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/blocks/{headerId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string]...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|headerId|path|string|true|ID of the header the wanted block|
Example responses
200 Response
=== "json"
```json
{
  "header": {
    "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "timestamp": 1524143059077,
    "version": 2,
    "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "nBits": 19857408,
    "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "powSolutions": {
      "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
      "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
      "n": "0000000000000000",
      "d": 987654321
    },
    "height": 667,
    "difficulty": "9575989248",
    "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "votes": "000000",
    "size": 0,
    "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
  },
  "blockTransactions": {
    "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "transactions": [
      {
        "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "inputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "spendingProof": {
              "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "extension":...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Block object representing the full block data|FullBlock|
|404|Not Found|Block with this id doesn't exist|ApiError|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getFullBlockByIds
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /blocks/headerIds \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'
```
=== "http"
```http
POST /blocks/headerIds HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '[
  "string"
]';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/blocks/headerIds',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/blocks/headerIds',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/blocks/headerIds', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/blocks/headerIds', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/blocks/headerIds");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer re...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|array[string]|true|none|
Example responses
200 Response
=== "json"
```json
[
  {
    "header": {
      "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "timestamp": 1524143059077,
      "version": 2,
      "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "nBits": 19857408,
      "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "powSolutions": {
        "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
        "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
        "n": "0000000000000000",
        "d": 987654321
      },
      "height": 667,
      "difficulty": "9575989248",
      "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "votes": "000000",
      "size": 0,
      "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    },
    "blockTransactions": {
      "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "transactions": [
        {
          "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "inputs": [
            {
              "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "spendingProof": {
                "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Full blocks corresponding to ids provided|Inline|
|404|Not Found|No block exist for every id provided|ApiError|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[FullBlock]|false|none|[Block with header and transactions]|
|» header|BlockHeader|true|none|Header of a block. It authenticates link to a previous block, other block sections (transactions, UTXO set transformation proofs, extension), UTXO set, votes for blockchain parameters to be changed and proof-of-work related data.|
|»» id|ModifierId(base16)|true|none|Base16-encoded 32 byte modifier id|
|»» timestamp|Timestamp(int64)|true|none|Basic timestamp definition|
|»» version|Version(int8)|true|none|Ergo blockchain protocol version|
|»» adProofsRoot|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|»» stateRoot|ADDigest(base16)|true|none|Base16-encoded 33 byte digest - digest with extra byte with tree height|
|»» transactionsRoot|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|»» nBits|integer(int64)|true|none|Proof-of-work target (difficulty encoded)|
|»» extensionHash|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|»» powSolutions|PowSolutions|true|none|An object containing all components of pow solution|
|»»» pk|string|true|none|Base16-encoded public key|
|»»» w|string|true|none|none|
|»»» n|string|true|none|none|
|»»» d|number|true|none|none|
|»» height|integer(int32)|true|none|Height of the block (genesis block height == 1)|
|»» difficulty|string|true|none|none|
|»» parentId|ModifierId(base16)|true|none|Base16-encoded 32 byte modifier id|
|»» votes|Votes(base16)|true|none|Base16-encoded votes for a soft-fork and parameters|
|»» size|integer(int32)|false|none|Size of the header in bytes|
|»» extensionId|ModifierId(base16)|false|none|Base16-encoded 32 byte modifier id|
|»» transactionsId|ModifierId(base16)|false|none|Base16-encoded 32 byte modifier id|
|»» adProofsId|ModifierId(base16)|false|none|Base16-encoded 32 byte modifier id|
|» blockTransactions|BlockTransactions|true|none|Section of a block which contains transactions.|
|»» headerId|Mo...

#### getBlockHeaderById
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /blocks/{headerId}/header \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /blocks/{headerId}/header HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/blocks/{headerId}/header',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/blocks/{headerId}/header',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/blocks/{headerId}/header', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/blocks/{headerId}/header', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/blocks/{headerId}/header");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"
       "net/h...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|headerId|path|string|true|ID of a wanted block header|
Example responses
200 Response
=== "json"
```json
{
  "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "timestamp": 1524143059077,
  "version": 2,
  "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "nBits": 19857408,
  "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "powSolutions": {
    "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
    "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
    "n": "0000000000000000",
    "d": 987654321
  },
  "height": 667,
  "difficulty": "9575989248",
  "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "votes": "000000",
  "size": 0,
  "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Block header object|BlockHeader|
|404|Not Found|Block with this id doesn't exist|ApiError|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getBlockTransactionsById
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /blocks/{headerId}/transactions \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /blocks/{headerId}/transactions HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/blocks/{headerId}/transactions',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/blocks/{headerId}/transactions',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/blocks/{headerId}/transactions', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/blocks/{headerId}/transactions', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/blocks/{headerId}/transactions");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package m...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|headerId|path|string|true|ID of a wanted block transactions|
Example responses
200 Response
=== "json"
```json
{
  "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "transactions": [
    {
      "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "inputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "spendingProof": {
            "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extension": {
              "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
            }
          }
        }
      ],
      "dataInputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        }
      ],
      "outputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0
        }
      ],
      "size": 0
    }
  ],
  "size": 0
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Block transaction object|BlockTransactions|
|404|Not Found|Block with this id doesn't exist|ApiError|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getProofForTx
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /blocks/{headerId}/proofFor/{txId} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /blocks/{headerId}/proofFor/{txId} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/blocks/{headerId}/proofFor/{txId}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/blocks/{headerId}/proofFor/{txId}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/blocks/{headerId}/proofFor/{txId}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/blocks/{headerId}/proofFor/{txId}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/blocks/{headerId}/proofFor/{txId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
===...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|headerId|path|string|true|ID of a wanted block transactions|
|txId|path|string|true|ID of a wanted transaction|
Example responses
200 Response
=== "json"
```json
{
  "leaf": "cd665e49c834b0c25574fcb19a158d836f3f2aad8e91ac195f972534c25449b3",
  "levels": [
    [
      "018b7ae20a4acd23e3f1bf38671ce97103ad96d8f1c780b5e5e865e4873ae16337",
      0
    ]
  ]
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Merkle proof object|MerkleProof|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getLastHeaders
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /blocks/lastHeaders/{count} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /blocks/lastHeaders/{count} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/blocks/lastHeaders/{count}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/blocks/lastHeaders/{count}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/blocks/lastHeaders/{count}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/blocks/lastHeaders/{count}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/blocks/lastHeaders/{count}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|count|path|number|true|a number of block headers to return|
Example responses
200 Response
=== "json"
```json
[
  {
    "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "timestamp": 1524143059077,
    "version": 2,
    "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "nBits": 19857408,
    "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "powSolutions": {
      "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
      "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
      "n": "0000000000000000",
      "d": 987654321
    },
    "height": 667,
    "difficulty": "9575989248",
    "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "votes": "000000",
    "size": 0,
    "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
  }
]
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Array of block headers|Inline|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[BlockHeader]|false|none|[Header of a block. It authenticates link to a previous block, other block sections (transactions, UTXO set transformation proofs, extension), UTXO set, votes for blockchain parameters to be changed and proof-of-work related data.]|
|» id|ModifierId(base16)|true|none|Base16-encoded 32 byte modifier id|
|» timestamp|Timestamp(int64)|true|none|Basic timestamp definition|
|» version|Version(int8)|true|none|Ergo blockchain protocol version|
|» adProofsRoot|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|» stateRoot|ADDigest(base16)|true|none|Base16-encoded 33 byte digest - digest with extra byte with tree height|
|» transactionsRoot|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|» nBits|integer(int64)|true|none|Proof-of-work target (difficulty encoded)|
|» extensionHash|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|» powSolutions|PowSolutions|true|none|An object containing all components of pow solution|
|»» pk|string|true|none|Base16-encoded public key|
|»» w|string|true|none|none|
|»» n|string|true|none|none|
|»» d|number|true|none|none|
|» height|integer(int32)|true|none|Height of the block (genesis block height == 1)|
|» difficulty|string|true|none|none|
|» parentId|ModifierId(base16)|true|none|Base16-encoded 32 byte modifier id|
|» votes|Votes(base16)|true|none|Base16-encoded votes for a soft-fork and parameters|
|» size|integer(int32)|false|none|Size of the header in bytes|
|» extensionId|ModifierId(base16)|false|none|Base16-encoded 32 byte modifier id|
|» transactionsId|ModifierId(base16)|false|none|Base16-encoded 32 byte modifier id|
|» adProofsId|ModifierId(base16)|false|none|Base16-encoded 32 byte modifier id|
This operation does not require authentication

#### getModifierById
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /blocks/modifier/{modifierId} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /blocks/modifier/{modifierId} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/blocks/modifier/{modifierId}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/blocks/modifier/{modifierId}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/blocks/modifier/{modifierId}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/blocks/modifier/{modifierId}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/blocks/modifier/{modifierId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|modifierId|path|string|true|ID of a wanted modifier|
Example responses
404 Response
=== "json"
```json
{
  "error": 500,
  "reason": "Internal server error",
  "detail": "string"
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Persistent modifier object|None|
|404|Not Found|Modifier with this id doesn't exist|ApiError|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getPopowHeaderById
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /nipopow/popowHeaderById/{headerId} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /nipopow/popowHeaderById/{headerId} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/nipopow/popowHeaderById/{headerId}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/nipopow/popowHeaderById/{headerId}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/nipopow/popowHeaderById/{headerId}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/nipopow/popowHeaderById/{headerId}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/nipopow/popowHeaderById/{headerId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|headerId|path|string|true|ID of wanted header|
Example responses
200 Response
=== "json"
```json
{
  "header": {
    "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "timestamp": 1524143059077,
    "version": 2,
    "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "nBits": 19857408,
    "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "powSolutions": {
      "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
      "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
      "n": "0000000000000000",
      "d": 987654321
    },
    "height": 667,
    "difficulty": "9575989248",
    "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "votes": "000000",
    "size": 0,
    "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
  },
  "interlinks": [
    "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
  ]
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|PoPow header object|PopowHeader|
|404|Not Found|Header of extension of a corresponding block are not available|ApiError|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getPopowHeaderByHeight
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /nipopow/popowHeaderByHeight/{height} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /nipopow/popowHeaderByHeight/{height} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/nipopow/popowHeaderByHeight/{height}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/nipopow/popowHeaderByHeight/{height}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/nipopow/popowHeaderByHeight/{height}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/nipopow/popowHeaderByHeight/{height}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/nipopow/popowHeaderByHeight/{height}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|height|path|integer(int32)|true|Height of a wanted header|
Example responses
200 Response
=== "json"
```json
{
  "header": {
    "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "timestamp": 1524143059077,
    "version": 2,
    "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "nBits": 19857408,
    "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "powSolutions": {
      "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
      "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
      "n": "0000000000000000",
      "d": 987654321
    },
    "height": 667,
    "difficulty": "9575989248",
    "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "votes": "000000",
    "size": 0,
    "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
  },
  "interlinks": [
    "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
  ]
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|PoPow header object|PopowHeader|
|404|Not Found|Header of extension of a corresponding block are not available|ApiError|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getPopowProof
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /nipopow/proof/{minChainLength}/{suffixLength} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /nipopow/proof/{minChainLength}/{suffixLength} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/nipopow/proof/{minChainLength}/{suffixLength}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/nipopow/proof/{minChainLength}/{suffixLength}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/nipopow/proof/{minChainLength}/{suffixLength}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/nipopow/proof/{minChainLength}/{suffixLength}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/nipopow/proof/{minChainLength}/{suffixLength}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    respon...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|minChainLength|path|number|true|Minimal superchain length|
|suffixLength|path|number|true|Suffix length|
Example responses
200 Response
=== "json"
```json
{
  "m": 0,
  "k": 0,
  "prefix": [
    {
      "header": {
        "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "timestamp": 1524143059077,
        "version": 2,
        "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "nBits": 19857408,
        "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "powSolutions": {
          "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
          "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
          "n": "0000000000000000",
          "d": 987654321
        },
        "height": 667,
        "difficulty": "9575989248",
        "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "votes": "000000",
        "size": 0,
        "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      },
      "interlinks": [
        "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      ]
    }
  ],
  "suffixHead": {
    "header": {
      "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "timestamp": 1524143059077,
      "version": 2,
      "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Nipopow proof object|NipopowProof|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getPopowProofByHeaderId
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /nipopow/proof/{minChainLength}/{suffixLength}/{headerId} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /nipopow/proof/{minChainLength}/{suffixLength}/{headerId} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/nipopow/proof/{minChainLength}/{suffixLength}/{headerId}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/nipopow/proof/{minChainLength}/{suffixLength}/{headerId}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/nipopow/proof/{minChainLength}/{suffixLength}/{headerId}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/nipopow/proof/{minChainLength}/{suffixLength}/{headerId}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/nipopow/proof/{minChainLength}/{suffixLength}/{headerId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response =...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|minChainLength|path|number|true|Minimal superchain length|
|suffixLength|path|number|true|Suffix length|
|headerId|path|string|true|ID of wanted header|
Example responses
200 Response
=== "json"
```json
{
  "m": 0,
  "k": 0,
  "prefix": [
    {
      "header": {
        "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "timestamp": 1524143059077,
        "version": 2,
        "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "nBits": 19857408,
        "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "powSolutions": {
          "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
          "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
          "n": "0000000000000000",
          "d": 987654321
        },
        "height": 667,
        "difficulty": "9575989248",
        "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "votes": "000000",
        "size": 0,
        "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      },
      "interlinks": [
        "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      ]
    }
  ],
  "suffixHead": {
    "header": {
      "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "timestamp": 1524143059077,
      "version": 2,
      "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "stateRoot": "3...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Nipopow proof object|NipopowProof|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getNodeInfo
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /info \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /info HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/info',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/info',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/info', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/info', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/info");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"},
    }

    data := bytes.NewBuffe...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Node info object|NodeInfo|
|default|Default|Error|ApiError|
This operation does not require authentication

#### sendTransaction
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /transactions \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'
```
=== "http"
```http
POST /transactions HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '{
  "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "inputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "spendingProof": {
        "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "extension": {
          "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
        }
      }
    }
  ],
  "dataInputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    }
  ],
  "outputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0
    }
  ],
  "size": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/transactions',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
   ...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|ErgoTransaction|true|none|
Example responses
200 Response
=== "json"
```json
"2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|JSON with ID of the new transaction|TransactionId|
|default|Default|Error|ApiError|
This operation does not require authentication

#### sendTransactionAsBytes
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /transactions/bytes \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'
```
=== "http"
```http
POST /transactions/bytes HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '"02c9e71790399816b3e40b2207e9ade19a9b7fe0600186cfb8e2b115bfdb34b57f38cd3c9f2890d11720eb3bb993993f00ededf812a590d2993df094a7ca4f0213e4820e1ab831eed5dc5c72665396d3a01d2a12900f1c3ab77700b284ae24fa8e8f7754f86f2282c795db6b0b17df1c29cc0552e59d01f7d777c638a813333277271c2f8b4d99d01ff0e6ee8695697bdd5b568089395620d7198c6093ce8bc59b928611b1b12452c05addaa42f4beff6a0a6fe90000000380d0dbc3f40210090402040005c801040205c8010500040004000e2003faf2cb329f2e90d6d23b58d91bbb6c046aa143261cc21f52fbe2824bfcbf04d807d601e4c6a70408d602b2a5730000d603e4c6a70601d604e4c6a7080ed605e4c6a70505d606e4c6a70705d60795720399c1a7c1720299c17202c1a7eb027201d1ededededededededed93c27202c2a793e4c672020408720193e4c6720205059572039d9c72057eb272047301000573029d9c72057eb2720473030005730494e4c672020601720393e4c672020705720693e4c67202080e720493e4c67202090ec5a79572039072079c720672059272079c72067205917207730595ef720393b1db630872027306d801d608b2db63087202730700ed938c7208017308938c7208027206c8df35000508cd030c8f9c4dc08f3c006fa85a47c9156dedbede000a8b764c6e374fd097e873ba0405c8a8c105010105dc8b020e0266608cdea8baf0380008cd030c8f9c4dc08f3c006fa85a47c9156dedbede000a8b764c6e374fd097e873ba04c8df350000c0843d1005040004000e36100204a00b08cd0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798ea02d192a39a8cc7a701730073011001020402d19683030193a38cc7b2a57300000193c2b2a57301007473027303830108cdeeac93b1a57304c8df350000"';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/transactions/bytes',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|string|true|none|
Example responses
200 Response
=== "json"
```json
"2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|JSON with ID of the new transaction|TransactionId|
|default|Default|Error|ApiError|
This operation does not require authentication

#### checkTransaction
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /transactions/check \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'
```
=== "http"
```http
POST /transactions/check HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '{
  "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "inputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "spendingProof": {
        "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "extension": {
          "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
        }
      }
    }
  ],
  "dataInputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    }
  ],
  "outputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0
    }
  ],
  "size": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/transactions/check',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(fu...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|ErgoTransaction|true|none|
Example responses
200 Response
=== "json"
```json
"2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|JSON with ID of the new transaction|TransactionId|
|default|Default|Error|ApiError|
This operation does not require authentication

#### checkTransactionAsBytes
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /transactions/checkBytes \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'
```
=== "http"
```http
POST /transactions/checkBytes HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '"02c9e71790399816b3e40b2207e9ade19a9b7fe0600186cfb8e2b115bfdb34b57f38cd3c9f2890d11720eb3bb993993f00ededf812a590d2993df094a7ca4f0213e4820e1ab831eed5dc5c72665396d3a01d2a12900f1c3ab77700b284ae24fa8e8f7754f86f2282c795db6b0b17df1c29cc0552e59d01f7d777c638a813333277271c2f8b4d99d01ff0e6ee8695697bdd5b568089395620d7198c6093ce8bc59b928611b1b12452c05addaa42f4beff6a0a6fe90000000380d0dbc3f40210090402040005c801040205c8010500040004000e2003faf2cb329f2e90d6d23b58d91bbb6c046aa143261cc21f52fbe2824bfcbf04d807d601e4c6a70408d602b2a5730000d603e4c6a70601d604e4c6a7080ed605e4c6a70505d606e4c6a70705d60795720399c1a7c1720299c17202c1a7eb027201d1ededededededededed93c27202c2a793e4c672020408720193e4c6720205059572039d9c72057eb272047301000573029d9c72057eb2720473030005730494e4c672020601720393e4c672020705720693e4c67202080e720493e4c67202090ec5a79572039072079c720672059272079c72067205917207730595ef720393b1db630872027306d801d608b2db63087202730700ed938c7208017308938c7208027206c8df35000508cd030c8f9c4dc08f3c006fa85a47c9156dedbede000a8b764c6e374fd097e873ba0405c8a8c105010105dc8b020e0266608cdea8baf0380008cd030c8f9c4dc08f3c006fa85a47c9156dedbede000a8b764c6e374fd097e873ba04c8df350000c0843d1005040004000e36100204a00b08cd0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798ea02d192a39a8cc7a701730073011001020402d19683030193a38cc7b2a57300000193c2b2a57301007473027303830108cdeeac93b1a57304c8df350000"';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/transactions/checkBytes',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body)...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|string|true|none|
Example responses
200 Response
=== "json"
```json
"2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|JSON with ID of the new transaction|TransactionId|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getUnconfirmedTransactions
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /transactions/unconfirmed \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /transactions/unconfirmed HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/transactions/unconfirmed',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/transactions/unconfirmed',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/transactions/unconfirmed', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/transactions/unconfirmed', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/transactions/unconfirmed");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"
       "net/h...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|limit|query|integer(int32)|false|The number of items in list to return|
|offset|query|integer(int32)|false|The number of items in list to skip|
Example responses
200 Response
=== "json"
```json
[
  {
    "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "inputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "spendingProof": {
          "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "extension": {
            "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
          }
        }
      }
    ],
    "dataInputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      }
    ],
    "outputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "value": 147,
        "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
        "creationHeight": 9149,
        "assets": [
          {
            "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 1000
          }
        ],
        "additionalRegisters": {
          "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
        },
        "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "index": 0
      }
    ],
    "size": 0
  }
]
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Array with Ergo transactions|Transactions|
|default|Default|Error|ApiError|
This operation does not require authentication

#### checkUnconfirmedTransaction
Code samples
=== "shell"
```shell
## You can also use wget
curl -X HEAD /transactions/unconfirmed/{txId}
```
=== "http"
```http
HEAD /transactions/unconfirmed/{txId} HTTP/1.1
```
=== "javascript"
```javascript

fetch('/transactions/unconfirmed/{txId}',
{
  method: 'HEAD'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

result = RestClient.head '/transactions/unconfirmed/{txId}',
  params: {
  }

p JSON.parse(result)
```
=== "python"
```python
import requests

r = requests.head('/transactions/unconfirmed/{txId}')

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('HEAD','/transactions/unconfirmed/{txId}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/transactions/unconfirmed/{txId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("HEAD");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("HEAD", "/transactions/unconfirmed/{txId}", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```
HEAD /tran...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|txId|path|string|true|ID of a transaction in question|

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Transaction is in pool|None|
|404|Not Found|Transaction is not in pool|None|
This operation does not require authentication

#### getUnconfirmedTransactionById
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /transactions/unconfirmed/byTransactionId/{txId} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /transactions/unconfirmed/byTransactionId/{txId} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/transactions/unconfirmed/byTransactionId/{txId}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/transactions/unconfirmed/byTransactionId/{txId}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/transactions/unconfirmed/byTransactionId/{txId}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/transactions/unconfirmed/byTransactionId/{txId}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/transactions/unconfirmed/byTransactionId/{txId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|txId|path|string|true|ID of a transaction in question|
Example responses
200 Response
=== "json"
```json
{
  "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "inputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "spendingProof": {
        "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "extension": {
          "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
        }
      }
    }
  ],
  "dataInputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    }
  ],
  "outputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0
    }
  ],
  "size": 0
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Ergo transaction|ErgoTransaction|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getUnconfirmedTransactionsByErgoTree
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /transactions/unconfirmed/byErgoTree \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'
```
=== "http"
```http
POST /transactions/unconfirmed/byErgoTree HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '"100204a00b08cd021cf943317b0fdb50f60892a46b9132b9ced337c7de79248b104b293d9f1f078eea02d192a39a8cc7a70173007301"';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/transactions/unconfirmed/byErgoTree',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/transactions/unconfirmed/byErgoTree',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/transactions/unconfirmed/byErgoTree', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/transactions/unconfirmed/byErgoTree', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/transactions/unconfirmed/byErgoTree");
HttpURLConnection con = (HttpURL...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|string|true|none|
|limit|query|integer(int32)|false|The number of items in list to return|
|offset|query|integer(int32)|false|The number of items in list to skip|
Example responses
200 Response
=== "json"
```json
[
  {
    "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "inputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "spendingProof": {
          "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "extension": {
            "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
          }
        }
      }
    ],
    "dataInputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      }
    ],
    "outputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "value": 147,
        "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
        "creationHeight": 9149,
        "assets": [
          {
            "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 1000
          }
        ],
        "additionalRegisters": {
          "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
        },
        "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "index": 0
      }
    ],
    "size": 0
  }
]
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Ergo transaction|Transactions|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getFeeHistogram
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /transactions/poolHistogram \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /transactions/poolHistogram HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/transactions/poolHistogram',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/transactions/poolHistogram',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/transactions/poolHistogram', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/transactions/poolHistogram', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/transactions/poolHistogram");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|bins|query|integer(int32)|false|The number of bins in histogram|
|maxtime|query|integer(int64)|false|Maximal wait time in milliseconds|
Example responses
200 Response
=== "json"
```json
[
  {
    "nTxns": 0,
    "totalFee": 0
  }
]
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Array with fee histogram|FeeHistogram|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getRecommendedFee
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /transactions/getFee?waitTime=1&txSize=100 \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /transactions/getFee?waitTime=1&txSize=100 HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/transactions/getFee?waitTime=1&txSize=100',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/transactions/getFee',
  params: {
  'waitTime' => 'integer(int32)',
'txSize' => 'integer(int32)'
}, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/transactions/getFee', params={
  'waitTime': '1',  'txSize': '100'
}, headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/transactions/getFee', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/transactions/getFee?waitTime=1&txSize=100");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != nul...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|waitTime|query|integer(int32)|true|Maximum transaction wait time in minutes|
|txSize|query|integer(int32)|true|Transaction size|
Example responses
200 Response
=== "json"
```json
0
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Recommended fee for the transaction (in nanoErgs)|integer|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getExpectedWaitTime
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /transactions/waitTime?fee=1&txSize=100 \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /transactions/waitTime?fee=1&txSize=100 HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/transactions/waitTime?fee=1&txSize=100',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/transactions/waitTime',
  params: {
  'fee' => 'integer(int32)',
'txSize' => 'integer(int32)'
}, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/transactions/waitTime', params={
  'fee': '1',  'txSize': '100'
}, headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/transactions/waitTime', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/transactions/waitTime?fee=1&txSize=100");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    respons...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|fee|query|integer(int32)|true|Transaction fee (in nanoErgs)|
|txSize|query|integer(int32)|true|Transaction size|
Example responses
200 Response
=== "json"
```json
0
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Expected wait time in milliseconds|integer|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getUnconfirmedTransactionInputBoxById
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /transactions/unconfirmed/inputs/byBoxId/{boxId} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /transactions/unconfirmed/inputs/byBoxId/{boxId} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/transactions/unconfirmed/inputs/byBoxId/{boxId}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/transactions/unconfirmed/inputs/byBoxId/{boxId}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/transactions/unconfirmed/inputs/byBoxId/{boxId}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/transactions/unconfirmed/inputs/byBoxId/{boxId}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/transactions/unconfirmed/inputs/byBoxId/{boxId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|boxId|path|string|true|ID of an input box in question|
Example responses
200 Response
=== "json"
```json
{
  "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "value": 147,
  "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
  "creationHeight": 9149,
  "assets": [
    {
      "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "amount": 1000
    }
  ],
  "additionalRegisters": {
    "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
  },
  "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "index": 0
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Unspent Ergo Box that is to be used as Input in unconfirmed tx|ErgoTransactionOutput|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getUnconfirmedTransactionOutputBoxById
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /transactions/unconfirmed/outputs/byBoxId/{boxId} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /transactions/unconfirmed/outputs/byBoxId/{boxId} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/transactions/unconfirmed/outputs/byBoxId/{boxId}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/transactions/unconfirmed/outputs/byBoxId/{boxId}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/transactions/unconfirmed/outputs/byBoxId/{boxId}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/transactions/unconfirmed/outputs/byBoxId/{boxId}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/transactions/unconfirmed/outputs/byBoxId/{boxId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) ...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|boxId|path|string|true|ID of an output box in question|
Example responses
200 Response
=== "json"
```json
{
  "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "value": 147,
  "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
  "creationHeight": 9149,
  "assets": [
    {
      "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "amount": 1000
    }
  ],
  "additionalRegisters": {
    "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
  },
  "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "index": 0
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Unspent Ergo Box that is to be created by unconfirmed tx|ErgoTransactionOutput|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getUnconfirmedTransactionOutputBoxesByErgoTree
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /transactions/unconfirmed/outputs/byErgoTree \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'
```
=== "http"
```http
POST /transactions/unconfirmed/outputs/byErgoTree HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '"100204a00b08cd021cf943317b0fdb50f60892a46b9132b9ced337c7de79248b104b293d9f1f078eea02d192a39a8cc7a70173007301"';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/transactions/unconfirmed/outputs/byErgoTree',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/transactions/unconfirmed/outputs/byErgoTree',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/transactions/unconfirmed/outputs/byErgoTree', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/transactions/unconfirmed/outputs/byErgoTree', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/transactions/unconfirme...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|string|true|none|
|limit|query|integer(int32)|false|The number of items in list to return|
|offset|query|integer(int32)|false|The number of items in list to skip|
Example responses
200 Response
=== "json"
```json
[
  {
    "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "value": 147,
    "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
    "creationHeight": 9149,
    "assets": [
      {
        "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "amount": 1000
      }
    ],
    "additionalRegisters": {
      "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
    },
    "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "index": 0
  }
]
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Unconfirmed transaction output boxes that correspond to given ErgoTree hex|Inline|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[ErgoTransactionOutput]|false|none|none|
|» boxId|TransactionBoxId(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|» value|integer(int64)|true|none|Amount of Ergo token|
|» ergoTree|ErgoTree(base16)|true|none|Base16-encoded ergo tree bytes|
|» creationHeight|integer(int32)|true|none|Height the output was created at|
|» assets|[Asset]|false|none|Assets list in the transaction|
|»» tokenId|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|»» amount|integer(int64)|true|none|Amount of the token|
|» additionalRegisters|Registers|true|none|Ergo box registers|
|»» additionalProperties|SValue(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|» transactionId|TransactionId(base16)|false|none|Base16-encoded transaction id bytes|
|» index|integer(int32)|false|none|Index in the transaction outputs|
This operation does not require authentication

#### getUnconfirmedTransactionOutputBoxesByTokenId
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /transactions/unconfirmed/outputs/byTokenId/{tokenId} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /transactions/unconfirmed/outputs/byTokenId/{tokenId} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/transactions/unconfirmed/outputs/byTokenId/{tokenId}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/transactions/unconfirmed/outputs/byTokenId/{tokenId}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/transactions/unconfirmed/outputs/byTokenId/{tokenId}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/transactions/unconfirmed/outputs/byTokenId/{tokenId}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/transactions/unconfirmed/outputs/byTokenId/{tokenId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while (...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|tokenId|path|string|true|ID of a token in question|
Example responses
200 Response
=== "json"
```json
[
  {
    "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "value": 147,
    "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
    "creationHeight": 9149,
    "assets": [
      {
        "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "amount": 1000
      }
    ],
    "additionalRegisters": {
      "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
    },
    "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "index": 0
  }
]
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Unspent Ergo Boxes that are to be created by unconfirmed tx and contain given token|Inline|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[ErgoTransactionOutput]|false|none|none|
|» boxId|TransactionBoxId(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|» value|integer(int64)|true|none|Amount of Ergo token|
|» ergoTree|ErgoTree(base16)|true|none|Base16-encoded ergo tree bytes|
|» creationHeight|integer(int32)|true|none|Height the output was created at|
|» assets|[Asset]|false|none|Assets list in the transaction|
|»» tokenId|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|»» amount|integer(int64)|true|none|Amount of the token|
|» additionalRegisters|Registers|true|none|Ergo box registers|
|»» additionalProperties|SValue(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|» transactionId|TransactionId(base16)|false|none|Base16-encoded transaction id bytes|
|» index|integer(int32)|false|none|Index in the transaction outputs|
This operation does not require authentication

#### getUnconfirmedTransactionOutputBoxesByRegisters
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /transactions/unconfirmed/outputs/byRegisters \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'
```
=== "http"
```http
POST /transactions/unconfirmed/outputs/byRegisters HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '{
  "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/transactions/unconfirmed/outputs/byRegisters',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/transactions/unconfirmed/outputs/byRegisters',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/transactions/unconfirmed/outputs/byRegisters', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/transactions/unconfirmed/outputs/byRegisters', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/trans...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|Registers|true|none|
|limit|query|integer(int32)|false|The number of items in list to return|
|offset|query|integer(int32)|false|The number of items in list to skip|
Example responses
200 Response
=== "json"
```json
[
  {
    "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "value": 147,
    "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
    "creationHeight": 9149,
    "assets": [
      {
        "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "amount": 1000
      }
    ],
    "additionalRegisters": {
      "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
    },
    "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "index": 0
  }
]
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Unconfirmed transaction output boxes that contain given registers|Inline|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[ErgoTransactionOutput]|false|none|none|
|» boxId|TransactionBoxId(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|» value|integer(int64)|true|none|Amount of Ergo token|
|» ergoTree|ErgoTree(base16)|true|none|Base16-encoded ergo tree bytes|
|» creationHeight|integer(int32)|true|none|Height the output was created at|
|» assets|[Asset]|false|none|Assets list in the transaction|
|»» tokenId|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|»» amount|integer(int64)|true|none|Amount of the token|
|» additionalRegisters|Registers|true|none|Ergo box registers|
|»» additionalProperties|SValue(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|» transactionId|TransactionId(base16)|false|none|Base16-encoded transaction id bytes|
|» index|integer(int32)|false|none|Index in the transaction outputs|
This operation does not require authentication

#### getAllPeers
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /peers/all \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /peers/all HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/peers/all',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/peers/all',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/peers/all', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/peers/all', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/peers/all");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application/json"}...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Array of peer objects|Inline|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[Peer]|false|none|none|
|» address|string|true|none|none|
|» restApiUrl|string¦null|false|none|none|
|» name|string¦null|false|none|none|
|» lastSeen|Timestamp(int64)|false|none|Basic timestamp definition|
|» connectionType|string¦null|false|none|none|

###### Enumerated Values
|Property|Value|
|---|---|
|connectionType|Incoming|
|connectionType|Outgoing|
This operation does not require authentication

#### getConnectedPeers
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /peers/connected \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /peers/connected HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/peers/connected',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/peers/connected',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/peers/connected', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/peers/connected', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/peers/connected");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
    ...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Array of peer objects|Inline|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[Peer]|false|none|none|
|» address|string|true|none|none|
|» restApiUrl|string¦null|false|none|none|
|» name|string¦null|false|none|none|
|» lastSeen|Timestamp(int64)|false|none|Basic timestamp definition|
|» connectionType|string¦null|false|none|none|

###### Enumerated Values
|Property|Value|
|---|---|
|connectionType|Incoming|
|connectionType|Outgoing|
This operation does not require authentication

#### connectToPeer
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /peers/connect \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /peers/connect HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '"127.0.0.1:5673"';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/peers/connect',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.post '/peers/connect',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.post('/peers/connect', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/peers/connect', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/peers/connect");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader ...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|string|true|none|
Example responses
default Response
=== "json"
```json
{
  "error": 500,
  "reason": "Internal server error",
  "detail": "string"
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Attempt to connect to the peer|None|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### getBlacklistedPeers
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /peers/blacklisted \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /peers/blacklisted HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/peers/blacklisted',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/peers/blacklisted',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/peers/blacklisted', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/peers/blacklisted', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/peers/blacklisted");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string]...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Array of the addresses|BlacklistedPeers|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getPeersStatus
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /peers/status \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /peers/status HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/peers/status',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/peers/status',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/peers/status', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/peers/status', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/peers/status");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []strin...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Network status|Inline|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[PeersStatus]|false|none|none|
|» lastIncomingMessage|Timestamp(int64)|true|none|Basic timestamp definition|
|» currentNetworkTime|Timestamp(int64)|true|none|Basic timestamp definition|
This operation does not require authentication

#### getPeersSyncInfo
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /peers/syncInfo \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /peers/syncInfo HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/peers/syncInfo',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/peers/syncInfo',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/peers/syncInfo', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/peers/syncInfo', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/peers/syncInfo");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Ac...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Network status|Inline|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[SyncInfo]|false|none|none|
|» address|string|true|none|none|
|» mode|PeerMode|true|none|none|
|»» state|string|true|none|none|
|»» verifyingTransactions|boolean|true|none|none|
|»» fullBlocksSuffix|integer|true|none|none|
|» version|string|true|none|none|
|» status|string|true|none|none|
|» height|integer|true|none|none|
This operation does not require authentication

#### getPeersTrackInfo
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /peers/trackInfo \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /peers/trackInfo HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/peers/trackInfo',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/peers/trackInfo',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/peers/trackInfo', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/peers/trackInfo', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/peers/trackInfo");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
    ...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Network status|Inline|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[TrackInfo]|false|none|none|
|» invalidModifierApproxSize|integer|true|none|none|
|» requested|object|true|none|Currently requested modifiers|
|»» additionalProperties|RequestedInfoByModifierId|false|none|none|
|»»» additionalProperties|RequestedInfo|false|none|none|
|»»»» address|string|false|none|none|
|»»»» version|string|false|none|none|
|»»»» checks|integer|true|none|How many times we checked for modifier delivery status|
|» received|object|true|none|Received modifiers|
|»» additionalProperties|ConnectedPeerByModifierId|false|none|none|
|»»» additionalProperties|ConnectedPeer|false|none|none|
|»»»» address|string|true|none|none|
|»»»» version|string|false|none|none|
|»»»» lastMessage|Timestamp(int64)|false|none|Basic timestamp definition|
This operation does not require authentication

#### getRandomSeed
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /utils/seed \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /utils/seed HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/utils/seed',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/utils/seed',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/utils/seed', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/utils/seed', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/utils/seed");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []string{"application...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Base16-encoded 32 byte seed|string|
|default|Default|Error|ApiError|
This operation does not require authentication

#### CheckAddressValidityWithGet
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /utils/address/{address} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /utils/address/{address} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/utils/address/{address}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/utils/address/{address}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/utils/address/{address}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/utils/address/{address}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/utils/address/{address}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"
       "net/http"
)
...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|address|path|ErgoAddress|true|address to check|
Example responses
200 Response
=== "json"
```json
{
  "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
  "isValid": true,
  "error": "string"
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Address validity with validation error|AddressValidity|
|default|Default|Error|ApiError|
This operation does not require authentication

#### CheckAddressValidity
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /utils/address \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'
```
=== "http"
```http
POST /utils/address HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '"3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/utils/address',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/utils/address',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/utils/address', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/utils/address', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/utils/address");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLi...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|string|true|address to check|
Example responses
200 Response
=== "json"
```json
{
  "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
  "isValid": true,
  "error": "string"
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Address validity with validation error|AddressValidity|
|default|Default|Error|ApiError|
This operation does not require authentication

#### AddressToRaw
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /utils/addressToRaw/{address} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /utils/addressToRaw/{address} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/utils/addressToRaw/{address}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/utils/addressToRaw/{address}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/utils/addressToRaw/{address}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/utils/addressToRaw/{address}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/utils/addressToRaw/{address}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|address|path|ErgoAddress|true|address to extract public key from|
Example responses
200 Response
=== "json"
```json
"02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3"
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|hex-encoded public key (serialized secp256k1 element)|string|
|default|Default|Error|ApiError|
This operation does not require authentication

#### RawToAddress
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /utils/rawToAddress/{pubkeyHex} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /utils/rawToAddress/{pubkeyHex} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/utils/rawToAddress/{pubkeyHex}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/utils/rawToAddress/{pubkeyHex}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/utils/rawToAddress/{pubkeyHex}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/utils/rawToAddress/{pubkeyHex}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/utils/rawToAddress/{pubkeyHex}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package m...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|pubkeyHex|path|string|true|public key to get address from|
Example responses
200 Response
=== "json"
```json
"3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Pay-to-public-key (P2PK) address|ErgoAddress|
|default|Default|Error|ApiError|
This operation does not require authentication

#### ErgoTreeToAddressWithGet
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /utils/ergoTreeToAddress/{ergoTreeHex} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /utils/ergoTreeToAddress/{ergoTreeHex} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/utils/ergoTreeToAddress/{ergoTreeHex}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/utils/ergoTreeToAddress/{ergoTreeHex}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/utils/ergoTreeToAddress/{ergoTreeHex}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/utils/ergoTreeToAddress/{ergoTreeHex}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/utils/ergoTreeToAddress/{ergoTreeHex}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(r...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|ergoTreeHex|path|string|true|ErgoTree to derive an address from|
Example responses
200 Response
=== "json"
```json
"3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Ergo address|ErgoAddress|
|default|Default|Error|ApiError|
This operation does not require authentication

#### ErgoTreeToAddress
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /utils/ergoTreeToAddress \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'
```
=== "http"
```http
POST /utils/ergoTreeToAddress HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '"100204a00b08cd021cf943317b0fdb50f60892a46b9132b9ced337c7de79248b104b293d9f1f078eea02d192a39a8cc7a70173007301"';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/utils/ergoTreeToAddress',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/utils/ergoTreeToAddress',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/utils/ergoTreeToAddress', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/utils/ergoTreeToAddress', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/utils/ergoTreeToAddress");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = c...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|string|true|ErgoTree hex to derive an address from|
Example responses
200 Response
=== "json"
```json
"3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Ergo address|ErgoAddress|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getRandomSeedWithLength
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /utils/seed/{length} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /utils/seed/{length} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/utils/seed/{length}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/utils/seed/{length}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/utils/seed/{length}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/utils/seed/{length}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/utils/seed/{length}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers ...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|length|path|string|true|seed length in bytes|
Example responses
200 Response
=== "json"
```json
"\"83375fd213cfd7dfd984ce1901d62c302a1db53160b416674c8da1a393a6bbc316\""
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Base16-encoded N byte seed|string|
|default|Default|Error|ApiError|
This operation does not require authentication

#### hashBlake2b
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /utils/hash/blake2b \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'
```
=== "http"
```http
POST /utils/hash/blake2b HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '"7yaASMijGEGTbttYHg1MrXnWB8EbzjJnFLSWvmNoHrXV"';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/utils/hash/blake2b',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/utils/hash/blake2b',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/utils/hash/blake2b', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/utils/hash/blake2b', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/utils/hash/blake2b");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInpu...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|string|true|none|
Example responses
200 Response
=== "json"
```json
"\"6ed54addddaf10fe8fcda330bd443a57914fbce38a9fa27248b07e361cc76a41\""
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Base16-encoded 32 byte hash|string|
|default|Default|Error|ApiError|
This operation does not require authentication

#### walletInit
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /wallet/init \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /wallet/init HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '{
  "pass": "string",
  "mnemonicPass": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/wallet/init',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.post '/wallet/init',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.post('/wallet/init', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/wallet/init', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/wallet/init");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCod...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|InitWallet|true|none|
Example responses
200 Response
=== "json"
```json
{
  "mnemonic": "string"
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|New wallet with randomly generated seed created successfully|InitWalletResult|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### walletRestore
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /wallet/restore \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /wallet/restore HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '{
  "pass": "string",
  "mnemonic": "string",
  "mnemonicPass": "string",
  "usePre1627KeyDerivation": true
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/wallet/restore',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.post '/wallet/restore',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.post('/wallet/restore', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/wallet/restore', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/wallet/restore");
HttpURLConnection con = (HttpURLConnection) obj.openC...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|RestoreWallet|true|none|
Example responses
default Response
=== "json"
```json
{
  "error": 500,
  "reason": "Internal server error",
  "detail": "string"
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Wallet restored successfully|None|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### checkSeed
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /wallet/check \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /wallet/check HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '{
  "mnemonic": "string",
  "mnemonicPass": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/wallet/check',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.post '/wallet/check',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.post('/wallet/check', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/wallet/check', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/wallet/check");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.get...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|CheckWallet|true|none|
Example responses
200 Response
=== "json"
```json
{
  "matched": true
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Whether passphrase match wallet|PassphraseMatch|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### walletUnlock
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /wallet/unlock \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /wallet/unlock HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '{
  "pass": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/wallet/unlock',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.post '/wallet/unlock',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.post('/wallet/unlock', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/wallet/unlock', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/wallet/unlock");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedR...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|UnlockWallet|true|none|
Example responses
default Response
=== "json"
```json
{
  "error": 500,
  "reason": "Internal server error",
  "detail": "string"
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Wallet unlocked successfully|None|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### walletLock
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /wallet/lock \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
GET /wallet/lock HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/wallet/lock',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.get '/wallet/lock',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.get('/wallet/lock', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/wallet/lock', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/wallet/lock");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

i...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Wallet locked successfully|None|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### walletRescan
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /wallet/rescan \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /wallet/rescan HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '{
  "fromHeight": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/wallet/rescan',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.post '/wallet/rescan',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.post('/wallet/rescan', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/wallet/rescan', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/wallet/rescan");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedRe...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|false|none|
|» fromHeight|body|integer(int32)|true|none|
Example responses
default Response
=== "json"
```json
{
  "error": 500,
  "reason": "Internal server error",
  "detail": "string"
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Wallet rescanned|None|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### getWalletStatus
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /wallet/status \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
GET /wallet/status HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/wallet/status',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.get '/wallet/status',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.get('/wallet/status', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/wallet/status', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/wallet/status");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
p...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Wallet status|WalletStatus|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### walletUpdateChangeAddress
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /wallet/updateChangeAddress \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /wallet/updateChangeAddress HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/wallet/updateChangeAddress',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.post '/wallet/updateChangeAddress',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.post('/wallet/updateChangeAddress', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/wallet/updateChangeAddress', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/wallet/updateChangeAddress");
HttpURLConnection con = (H...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|ErgoAddress|true|none|
Example responses
default Response
=== "json"
```json
{
  "error": 500,
  "reason": "Internal server error",
  "detail": "string"
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Change address updated successfully|None|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### walletDeriveKey
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /wallet/deriveKey \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /wallet/deriveKey HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '{
  "derivationPath": "m/1/2"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/wallet/deriveKey',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.post '/wallet/deriveKey',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.post('/wallet/deriveKey', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/wallet/deriveKey', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/wallet/deriveKey");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = co...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|DeriveKey|true|none|
Example responses
200 Response
=== "json"
```json
{
  "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Resulted address|DeriveKeyResult|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### walletDeriveNextKey
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /wallet/deriveNextKey \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
GET /wallet/deriveNextKey HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/wallet/deriveNextKey',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.get '/wallet/deriveNextKey',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.get('/wallet/deriveNextKey', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/wallet/deriveNextKey', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/wallet/deriveNextKey");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.p...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Resulted secret path and address|DeriveNextKeyResult|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### walletBalances
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /wallet/balances \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
GET /wallet/balances HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/wallet/balances',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.get '/wallet/balances',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.get('/wallet/balances', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/wallet/balances', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/wallet/balances");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
==...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Get total amount of confirmed Ergo tokens and assets|BalancesSnapshot|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### walletTransactions
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /wallet/transactions \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
GET /wallet/transactions HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/wallet/transactions',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.get '/wallet/transactions',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.get('/wallet/transactions', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/wallet/transactions', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/wallet/transactions");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|minInclusionHeight|query|integer(int32)|false|Minimal tx inclusion height|
|maxInclusionHeight|query|integer(int32)|false|Maximal tx inclusion height|
|minConfirmations|query|integer(int32)|false|Minimal confirmations number|
|maxConfirmations|query|integer(int32)|false|Maximal confirmations number|
Example responses
200 Response
=== "json"
```json
[
  {
    "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "inputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "spendingProof": {
          "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "extension": {
            "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
          }
        }
      }
    ],
    "dataInputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      }
    ],
    "outputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "value": 147,
        "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
        "creationHeight": 9149,
        "assets": [
          {
            "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 1000
          }
        ],
        "additionalRegisters": {
          "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
        },
        "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "index": 0
      }
    ],
    "inclusionHeight": 20998,
    "numConfirmations": 20998,
    "scans": [
      1
    ],
    "si...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|A list of all wallet-related transactions|Inline|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[WalletTransaction]|false|none|[Transaction augmented with some useful information]|
|» id|TransactionId(base16)|false|none|Base16-encoded transaction id bytes|
|» inputs|[ErgoTransactionInput]|true|none|Transaction inputs|
|»» boxId|TransactionBoxId(base16)|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» spendingProof|SpendingProof|true|none|Spending proof for transaction input|
|»»» proofBytes|SpendingProofBytes(base16)|true|none|Base16-encoded spending proofs|
|»»» extension|object|true|none|Variables to be put into context|
|»»»» additionalProperties|SValue(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|» dataInputs|[ErgoTransactionDataInput]|true|none|Transaction data inputs|
|»» boxId|TransactionBoxId(base16)|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|» outputs|[ErgoTransactionOutput]|true|none|Transaction outputs|
|»» boxId|TransactionBoxId(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» value|integer(int64)|true|none|Amount of Ergo token|
|»» ergoTree|ErgoTree(base16)|true|none|Base16-encoded ergo tree bytes|
|»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»» assets|[Asset]|false|none|Assets list in the transaction|
|»»» tokenId|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|»»» amount|integer(int64)|true|none|Amount of the token|
|»» additionalRegisters|Registers|true|none|Ergo box registers|
|»»» additionalProperties|SValue(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»» transactionId|TransactionId(base16)|false|none|Base16-encoded transaction id bytes|
|»» index|integer(int32)|false|none|Index in the transaction outputs|
|» inclusionHeight|integer(int32)|true|none|Height of a block the transaction was included in|
|» numConfirmations|integer(int32)|true|none|Number of transac...

#### walletGetTransaction
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /wallet/transactionById?id=string \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
GET /wallet/transactionById?id=string HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/wallet/transactionById?id=string',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.get '/wallet/transactionById',
  params: {
  'id' => 'string'
}, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.get('/wallet/transactionById', params={
  'id': 'string'
}, headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/wallet/transactionById', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/wallet/transactionById?id=string");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
whil...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|query|string|true|Transaction id|
Example responses
200 Response
=== "json"
```json
[
  {
    "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "inputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "spendingProof": {
          "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "extension": {
            "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
          }
        }
      }
    ],
    "dataInputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      }
    ],
    "outputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "value": 147,
        "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
        "creationHeight": 9149,
        "assets": [
          {
            "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 1000
          }
        ],
        "additionalRegisters": {
          "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
        },
        "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "index": 0
      }
    ],
    "inclusionHeight": 20998,
    "numConfirmations": 20998,
    "scans": [
      1
    ],
    "size": 0
  }
]
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Wallet-related transaction|Inline|
|404|Not Found|Transaction with specified id not found in wallet|ApiError|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[WalletTransaction]|false|none|[Transaction augmented with some useful information]|
|» id|TransactionId(base16)|false|none|Base16-encoded transaction id bytes|
|» inputs|[ErgoTransactionInput]|true|none|Transaction inputs|
|»» boxId|TransactionBoxId(base16)|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» spendingProof|SpendingProof|true|none|Spending proof for transaction input|
|»»» proofBytes|SpendingProofBytes(base16)|true|none|Base16-encoded spending proofs|
|»»» extension|object|true|none|Variables to be put into context|
|»»»» additionalProperties|SValue(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|» dataInputs|[ErgoTransactionDataInput]|true|none|Transaction data inputs|
|»» boxId|TransactionBoxId(base16)|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|» outputs|[ErgoTransactionOutput]|true|none|Transaction outputs|
|»» boxId|TransactionBoxId(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» value|integer(int64)|true|none|Amount of Ergo token|
|»» ergoTree|ErgoTree(base16)|true|none|Base16-encoded ergo tree bytes|
|»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»» assets|[Asset]|false|none|Assets list in the transaction|
|»»» tokenId|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|»»» amount|integer(int64)|true|none|Amount of the token|
|»» additionalRegisters|Registers|true|none|Ergo box registers|
|»»» additionalProperties|SValue(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»» transactionId|TransactionId(base16)|false|none|Base16-encoded transaction id bytes|
|»» index|integer(int32)|false|none|Index in the transaction outputs|
|» inclusionHeight|integer(int32)|true|none|Height of a block the transaction was included in|
|» numConfirmations|integer(int32)|true|none|Number of transac...

#### walletTransactionsByScanId
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /wallet/transactionsByScanId/{scanId} \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
GET /wallet/transactionsByScanId/{scanId} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/wallet/transactionsByScanId/{scanId}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.get '/wallet/transactionsByScanId/{scanId}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.get('/wallet/transactionsByScanId/{scanId}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/wallet/transactionsByScanId/{scanId}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/wallet/transactionsByScanId/{scanId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBu...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scanId|path|integer(int32)|true|identifier of a scan|
|minInclusionHeight|query|integer(int32)|false|Minimal tx inclusion height|
|maxInclusionHeight|query|integer(int32)|false|Maximal tx inclusion height|
|minConfirmations|query|integer(int32)|false|Minimal confirmations number|
|maxConfirmations|query|integer(int32)|false|Maximal confirmations number|
|includeUnconfirmed|query|boolean|false|Include transactions from mempool|
Example responses
200 Response
=== "json"
```json
[
  {
    "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "inputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "spendingProof": {
          "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "extension": {
            "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
          }
        }
      }
    ],
    "dataInputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      }
    ],
    "outputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "value": 147,
        "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
        "creationHeight": 9149,
        "assets": [
          {
            "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 1000
          }
        ],
        "additionalRegisters": {
          "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
        },
        "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  ...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Scan-related transactions|Inline|
|404|Not Found|Transactions with related scan id not found in wallet|ApiError|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[WalletTransaction]|false|none|[Transaction augmented with some useful information]|
|» id|TransactionId(base16)|false|none|Base16-encoded transaction id bytes|
|» inputs|[ErgoTransactionInput]|true|none|Transaction inputs|
|»» boxId|TransactionBoxId(base16)|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» spendingProof|SpendingProof|true|none|Spending proof for transaction input|
|»»» proofBytes|SpendingProofBytes(base16)|true|none|Base16-encoded spending proofs|
|»»» extension|object|true|none|Variables to be put into context|
|»»»» additionalProperties|SValue(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|» dataInputs|[ErgoTransactionDataInput]|true|none|Transaction data inputs|
|»» boxId|TransactionBoxId(base16)|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|» outputs|[ErgoTransactionOutput]|true|none|Transaction outputs|
|»» boxId|TransactionBoxId(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» value|integer(int64)|true|none|Amount of Ergo token|
|»» ergoTree|ErgoTree(base16)|true|none|Base16-encoded ergo tree bytes|
|»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»» assets|[Asset]|false|none|Assets list in the transaction|
|»»» tokenId|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|»»» amount|integer(int64)|true|none|Amount of the token|
|»» additionalRegisters|Registers|true|none|Ergo box registers|
|»»» additionalProperties|SValue(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»» transactionId|TransactionId(base16)|false|none|Base16-encoded transaction id bytes|
|»» index|integer(int32)|false|none|Index in the transaction outputs|
|» inclusionHeight|integer(int32)|true|none|Height of a block the transaction was included in|
|» numConfirmations|integer(int32)|true|none|Number of transac...

#### walletBoxes
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /wallet/boxes \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
GET /wallet/boxes HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/wallet/boxes',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.get '/wallet/boxes',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.get('/wallet/boxes', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/wallet/boxes', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/wallet/boxes");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package ...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|minConfirmations|query|integer(int32)|false|Minimal number of confirmations, -1 means we consider unconfirmed|
|maxConfirmations|query|integer(int32)|false|Maximum number of confirmations, -1 means unlimited|
|minInclusionHeight|query|integer(int32)|false|Minimal box inclusion height|
|maxInclusionHeight|query|integer(int32)|false|Maximum box inclusion height, -1 means unlimited|
Example responses
200 Response
=== "json"
```json
[
  {
    "box": {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0
    },
    "confirmationsNum": 147,
    "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
    "creationTransaction": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "spendingTransaction": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "spendingHeight": 147,
    "inclusionHeight": 147,
    "onchain": true,
    "spent": false,
    "creationOutIndex": 2,
    "scans": [
      1
    ]
  }
]
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|A list of all wallet-related boxes|Inline|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[WalletBox]|false|none|none|
|» box|ErgoTransactionOutput|true|none|none|
|»» boxId|TransactionBoxId(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» value|integer(int64)|true|none|Amount of Ergo token|
|»» ergoTree|ErgoTree(base16)|true|none|Base16-encoded ergo tree bytes|
|»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»» assets|[Asset]|false|none|Assets list in the transaction|
|»»» tokenId|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|»»» amount|integer(int64)|true|none|Amount of the token|
|»» additionalRegisters|Registers|true|none|Ergo box registers|
|»»» additionalProperties|SValue(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»» transactionId|TransactionId(base16)|false|none|Base16-encoded transaction id bytes|
|»» index|integer(int32)|false|none|Index in the transaction outputs|
|» confirmationsNum|integer(int32)¦null|true|none|Number of confirmations, if the box is included into the blockchain|
|» address|ErgoAddress|true|none|Encoded Ergo Address|
|» creationTransaction|ModifierId(base16)|true|none|Base16-encoded 32 byte modifier id|
|» spendingTransaction|ModifierId(base16)|true|none|Base16-encoded 32 byte modifier id|
|» spendingHeight|integer(int32)¦null|true|none|The height the box was spent at|
|» inclusionHeight|integer(int32)|true|none|The height the transaction containing the box was included in a block at|
|» onchain|boolean|true|none|A flag signalling whether the box is created on main chain|
|» spent|boolean|true|none|A flag signalling whether the box was spent|
|» creationOutIndex|integer(int32)|true|none|An index of a box in the creating transaction|
|» scans|[integer]|true|none|Scan identifiers the box relates to|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### walletBoxesCollect
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /wallet/boxes/collect \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /wallet/boxes/collect HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '{
  "targetAssets": [
    [
      "string",
      "string"
    ]
  ],
  "targetBalance": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/wallet/boxes/collect',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.post '/wallet/boxes/collect',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.post('/wallet/boxes/collect', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/wallet/boxes/collect', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/wallet/boxes/collect");
HttpURLConnection con = (Htt...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|BoxesRequestHolder|true|This API method recieves balance and assets, according to which, it's collecting result|
Example responses
200 Response
=== "json"
```json
[
  {
    "box": {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0
    },
    "confirmationsNum": 147,
    "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
    "creationTransaction": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "spendingTransaction": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "spendingHeight": 147,
    "inclusionHeight": 147,
    "onchain": true,
    "spent": false,
    "creationOutIndex": 2,
    "scans": [
      1
    ]
  }
]
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|A list of all collected boxes|Inline|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[WalletBox]|false|none|none|
|» box|ErgoTransactionOutput|true|none|none|
|»» boxId|TransactionBoxId(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» value|integer(int64)|true|none|Amount of Ergo token|
|»» ergoTree|ErgoTree(base16)|true|none|Base16-encoded ergo tree bytes|
|»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»» assets|[Asset]|false|none|Assets list in the transaction|
|»»» tokenId|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|»»» amount|integer(int64)|true|none|Amount of the token|
|»» additionalRegisters|Registers|true|none|Ergo box registers|
|»»» additionalProperties|SValue(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»» transactionId|TransactionId(base16)|false|none|Base16-encoded transaction id bytes|
|»» index|integer(int32)|false|none|Index in the transaction outputs|
|» confirmationsNum|integer(int32)¦null|true|none|Number of confirmations, if the box is included into the blockchain|
|» address|ErgoAddress|true|none|Encoded Ergo Address|
|» creationTransaction|ModifierId(base16)|true|none|Base16-encoded 32 byte modifier id|
|» spendingTransaction|ModifierId(base16)|true|none|Base16-encoded 32 byte modifier id|
|» spendingHeight|integer(int32)¦null|true|none|The height the box was spent at|
|» inclusionHeight|integer(int32)|true|none|The height the transaction containing the box was included in a block at|
|» onchain|boolean|true|none|A flag signalling whether the box is created on main chain|
|» spent|boolean|true|none|A flag signalling whether the box was spent|
|» creationOutIndex|integer(int32)|true|none|An index of a box in the creating transaction|
|» scans|[integer]|true|none|Scan identifiers the box relates to|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### walletUnspentBoxes
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /wallet/boxes/unspent \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
GET /wallet/boxes/unspent HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/wallet/boxes/unspent',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.get '/wallet/boxes/unspent',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.get('/wallet/boxes/unspent', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/wallet/boxes/unspent', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/wallet/boxes/unspent");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.p...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|minConfirmations|query|integer(int32)|false|Minimal number of confirmations, -1 means we consider unconfirmed|
|maxConfirmations|query|integer(int32)|false|Maximum number of confirmations, -1 means unlimited|
|minInclusionHeight|query|integer(int32)|false|Minimal box inclusion height|
|maxInclusionHeight|query|integer(int32)|false|Maximum box inclusion height, -1 means unlimited|
Example responses
200 Response
=== "json"
```json
[
  {
    "box": {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0
    },
    "confirmationsNum": 147,
    "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
    "creationTransaction": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "spendingTransaction": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "spendingHeight": 147,
    "inclusionHeight": 147,
    "onchain": true,
    "spent": false,
    "creationOutIndex": 2,
    "scans": [
      1
    ]
  }
]
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|A list of unspent boxes|Inline|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[WalletBox]|false|none|none|
|» box|ErgoTransactionOutput|true|none|none|
|»» boxId|TransactionBoxId(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» value|integer(int64)|true|none|Amount of Ergo token|
|»» ergoTree|ErgoTree(base16)|true|none|Base16-encoded ergo tree bytes|
|»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»» assets|[Asset]|false|none|Assets list in the transaction|
|»»» tokenId|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|»»» amount|integer(int64)|true|none|Amount of the token|
|»» additionalRegisters|Registers|true|none|Ergo box registers|
|»»» additionalProperties|SValue(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»» transactionId|TransactionId(base16)|false|none|Base16-encoded transaction id bytes|
|»» index|integer(int32)|false|none|Index in the transaction outputs|
|» confirmationsNum|integer(int32)¦null|true|none|Number of confirmations, if the box is included into the blockchain|
|» address|ErgoAddress|true|none|Encoded Ergo Address|
|» creationTransaction|ModifierId(base16)|true|none|Base16-encoded 32 byte modifier id|
|» spendingTransaction|ModifierId(base16)|true|none|Base16-encoded 32 byte modifier id|
|» spendingHeight|integer(int32)¦null|true|none|The height the box was spent at|
|» inclusionHeight|integer(int32)|true|none|The height the transaction containing the box was included in a block at|
|» onchain|boolean|true|none|A flag signalling whether the box is created on main chain|
|» spent|boolean|true|none|A flag signalling whether the box was spent|
|» creationOutIndex|integer(int32)|true|none|An index of a box in the creating transaction|
|» scans|[integer]|true|none|Scan identifiers the box relates to|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### walletBalancesUnconfirmed
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /wallet/balances/withUnconfirmed \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
GET /wallet/balances/withUnconfirmed HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/wallet/balances/withUnconfirmed',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.get '/wallet/balances/withUnconfirmed',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.get('/wallet/balances/withUnconfirmed', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/wallet/balances/withUnconfirmed', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/wallet/balances/withUnconfirmed");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.read...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Get summary amount of confirmed plus unconfirmed Ergo tokens and assets|BalancesSnapshot|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### walletAddresses
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /wallet/addresses \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
GET /wallet/addresses HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/wallet/addresses',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.get '/wallet/addresses',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.get('/wallet/addresses', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/wallet/addresses', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/wallet/addresses");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|String with encoded wallet addresses|Inline|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[ErgoAddress]|false|none|[Encoded Ergo Address]|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### walletTransactionGenerate
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /wallet/transaction/generate \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /wallet/transaction/generate HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '{
  "requests": [
    {
      "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
      "value": 1,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "registers": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      }
    }
  ],
  "fee": 1000000,
  "inputsRaw": [
    "string"
  ],
  "dataInputsRaw": [
    "string"
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/wallet/transaction/generate',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.post '/wallet/transaction/generate',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.post('/wallet/transaction/generate', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request b...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|RequestsHolder|true|This API method receives a sequence of requests as an input. Each request will produce an output of the resulting transaction (with fee output created automatically). Currently supported types of requests are payment and asset issuance requests. An example for a transaction with requests of both kinds is provided below. Please note that for the payment request "assets" and "registers" fields are not needed. For asset issuance request, "registers" field is not needed.|

###### Detailed descriptions
body: This API method receives a sequence of requests as an input. Each request will produce an output of the resulting transaction (with fee output created automatically). Currently supported types of requests are payment and asset issuance requests. An example for a transaction with requests of both kinds is provided below. Please note that for the payment request "assets" and "registers" fields are not needed. For asset issuance request, "registers" field is not needed.
You may specify boxes to spend by providing them in "inputsRaw". Please note you need to have strict equality between input and output total amounts of Ergs in this case. If you want wallet to pick up the boxes, leave "inputsRaw" empty.
Example responses
200 Response
=== "json"
```json
{
  "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "inputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "spendingProof": {
        "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "extension": {
          "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
        }
      }
    }
  ],
  "dataInputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    }
  ],
  "outputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d1...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Generated Ergo transaction|ErgoTransaction|
|400|Bad Request|Bad transaction request|ApiError|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### walletUnsignedTransactionGenerate
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /wallet/transaction/generateUnsigned \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /wallet/transaction/generateUnsigned HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '{
  "requests": [
    {
      "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
      "value": 1,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "registers": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      }
    }
  ],
  "fee": 1000000,
  "inputsRaw": [
    "string"
  ],
  "dataInputsRaw": [
    "string"
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/wallet/transaction/generateUnsigned',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.post '/wallet/transaction/generateUnsigned',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.post('/wallet/transaction/generateUnsigned', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|RequestsHolder|true|The same as /wallet/transaction/generate but generates unsigned transaction.|
Example responses
200 Response
=== "json"
```json
{
  "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "inputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "extension": {
        "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
      }
    }
  ],
  "dataInputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    }
  ],
  "outputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0
    }
  ]
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Generated unsigned Ergo transaction|UnsignedErgoTransaction|
|400|Bad Request|Bad transaction request|ApiError|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### walletTransactionSign
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /wallet/transaction/sign \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /wallet/transaction/sign HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '{
  "tx": {
    "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "inputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "extension": {
          "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
        }
      }
    ],
    "dataInputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      }
    ],
    "outputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "value": 147,
        "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
        "creationHeight": 9149,
        "assets": [
          {
            "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 1000
          }
        ],
        "additionalRegisters": {
          "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
        },
        "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "index": 0
      }
    ]
  },
  "inputsRaw": [
    "string"
  ],
  "dataInputsRaw": [
    "string"
  ],
  "hints": {
    "secretHints": [
      {
        "01": [
          {
            "hint": "cmtWithSecret",
            "pubkey": {
              "op": -51,
              "h": "0327e65711a59378c59359c3e1d0f7abe906479eccb76094e50fe79d743ccc15e6"
            },
            "position": "0-1",
            "type": "dlog",...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|TransactionSigningRequest|true|With this API method an arbitrary unsigned transaction can be signed with secrets provided or stored in the wallet. Both DLOG and Diffie-Hellman tuple secrets are supported.|

###### Detailed descriptions
body: With this API method an arbitrary unsigned transaction can be signed with secrets provided or stored in the wallet. Both DLOG and Diffie-Hellman tuple secrets are supported.
Please note that the unsigned transaction contains only identifiers of inputs and data inputs. If the node holds UTXO set, it is able to extract boxes needed. Otherwise, input (and data-input) boxes can be provided in "inputsRaw" and "dataInputsRaw" fields.
Example responses
200 Response
=== "json"
```json
{
  "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "inputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "spendingProof": {
        "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "extension": {
          "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
        }
      }
    }
  ],
  "dataInputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    }
  ],
  "outputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0
    }
  ],
  "size": 0
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Generated Ergo transaction|ErgoTransaction|
|400|Bad Request|Bad transaction request|ApiError|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### walletTransactionGenerateAndSend
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /wallet/transaction/send \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /wallet/transaction/send HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '{
  "requests": [
    {
      "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
      "value": 1,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "registers": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      }
    }
  ],
  "fee": 1000000,
  "inputsRaw": [
    "string"
  ],
  "dataInputsRaw": [
    "string"
  ]
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/wallet/transaction/send',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.post '/wallet/transaction/send',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.post('/wallet/transaction/send', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body =...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|RequestsHolder|true|See description of /wallet/transaction/generate|
Example responses
200 Response
=== "json"
```json
"2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Identifier of an Ergo transaction generated|TransactionId|
|400|Bad Request|Bad transaction request|ApiError|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### walletPaymentTransactionGenerateAndSend
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /wallet/payment/send \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /wallet/payment/send HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '[
  {
    "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
    "value": 1,
    "assets": [
      {
        "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "amount": 1000
      }
    ],
    "registers": {
      "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
    }
  }
]';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/wallet/payment/send',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.post '/wallet/payment/send',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.post('/wallet/payment/send', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/wallet/payment/send', array(
        'headers' => $headers,
        'json' => $request_body,
      ...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|PaymentRequest|true|none|
Example responses
200 Response
=== "json"
```json
"2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Identifier of an Ergo transaction generated|TransactionId|
|400|Bad Request|Bad payment request|ApiError|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### walletGetPrivateKey
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /wallet/getPrivateKey \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /wallet/getPrivateKey HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/wallet/getPrivateKey',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.post '/wallet/getPrivateKey',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.post('/wallet/getPrivateKey', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/wallet/getPrivateKey', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/wallet/getPrivateKey");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
co...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|ErgoAddress|true|none|
Example responses
200 Response
=== "json"
```json
"433080ff80d0d52d7f8bfffff47f00807f44f680000949b800007f7f7ff1017f"
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Successfully retrieved secret key|DlogSecret|
|404|Not Found|Address not found in wallet database|ApiError|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### generateCommitments
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /wallet/generateCommitments \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /wallet/generateCommitments HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '{
  "tx": {
    "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "inputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "extension": {
          "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
        }
      }
    ],
    "dataInputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      }
    ],
    "outputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "value": 147,
        "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
        "creationHeight": 9149,
        "assets": [
          {
            "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 1000
          }
        ],
        "additionalRegisters": {
          "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
        },
        "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "index": 0
      }
    ]
  },
  "secrets": {
    "dlog": [
      "433080ff80d0d52d7f8bfffff47f00807f44f680000949b800007f7f7ff1017f"
    ],
    "dht": [
      {
        "secret": "433080ff80d0d52d7f8bfffff47f00807f44f680000949b800007f7f7ff1017f",
        "g": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
        "h": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
   ...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|GenerateCommitmentsRequest|true|none|
Example responses
200 Response
=== "json"
```json
{
  "secretHints": [
    {
      "01": [
        {
          "hint": "cmtWithSecret",
          "pubkey": {
            "op": -51,
            "h": "0327e65711a59378c59359c3e1d0f7abe906479eccb76094e50fe79d743ccc15e6"
          },
          "position": "0-1",
          "type": "dlog",
          "a": "02924d6274d1b9132fe028a0e3ac2fdbc503a1e52d1398932fa5f1bcf71909eb4b",
          "secret": "42a2a0ae6b98ee791ac9734252e8a7a08e691b92de085138e302f64a722a4300"
        }
      ]
    }
  ],
  "publicHints": [
    {
      "01": [
        {
          "hint": "cmtWithSecret",
          "pubkey": {
            "op": -51,
            "h": "0327e65711a59378c59359c3e1d0f7abe906479eccb76094e50fe79d743ccc15e6"
          },
          "position": "0-1",
          "type": "dlog",
          "a": "02924d6274d1b9132fe028a0e3ac2fdbc503a1e52d1398932fa5f1bcf71909eb4b",
          "secret": "42a2a0ae6b98ee791ac9734252e8a7a08e691b92de085138e302f64a722a4300"
        }
      ]
    }
  ]
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Transaction-related hints|TransactionHintsBag|
|400|Bad Request|Error|ApiError|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### extractHints
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /wallet/extractHints \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /wallet/extractHints HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '{
  "tx": {
    "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "inputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "spendingProof": {
          "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "extension": {
            "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
          }
        }
      }
    ],
    "dataInputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      }
    ],
    "outputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "value": 147,
        "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
        "creationHeight": 9149,
        "assets": [
          {
            "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 1000
          }
        ],
        "additionalRegisters": {
          "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
        },
        "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "index": 0
      }
    ],
    "size": 0
  },
  "real": [
    {
      "op": 0,
      "h": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "g"...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|HintExtractionRequest|true|none|
Example responses
200 Response
=== "json"
```json
{
  "secretHints": [
    {
      "01": [
        {
          "hint": "cmtWithSecret",
          "pubkey": {
            "op": -51,
            "h": "0327e65711a59378c59359c3e1d0f7abe906479eccb76094e50fe79d743ccc15e6"
          },
          "position": "0-1",
          "type": "dlog",
          "a": "02924d6274d1b9132fe028a0e3ac2fdbc503a1e52d1398932fa5f1bcf71909eb4b",
          "secret": "42a2a0ae6b98ee791ac9734252e8a7a08e691b92de085138e302f64a722a4300"
        }
      ]
    }
  ],
  "publicHints": [
    {
      "01": [
        {
          "hint": "cmtWithSecret",
          "pubkey": {
            "op": -51,
            "h": "0327e65711a59378c59359c3e1d0f7abe906479eccb76094e50fe79d743ccc15e6"
          },
          "position": "0-1",
          "type": "dlog",
          "a": "02924d6274d1b9132fe028a0e3ac2fdbc503a1e52d1398932fa5f1bcf71909eb4b",
          "secret": "42a2a0ae6b98ee791ac9734252e8a7a08e691b92de085138e302f64a722a4300"
        }
      ]
    }
  ]
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Hints for the transaction|TransactionHintsBag|
|400|Bad Request|Error|ApiError|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### miningRequestBlockCandidate
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /mining/candidate \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
GET /mining/candidate HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/mining/candidate',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.get '/mining/candidate',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.get('/mining/candidate', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/mining/candidate', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/mining/candidate");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|External candidate|WorkMessage|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### miningRequestBlockCandidateWithMandatoryTransactions
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /mining/candidateWithTxs \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /mining/candidateWithTxs HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '[
  {
    "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "inputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "spendingProof": {
          "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "extension": {
            "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
          }
        }
      }
    ],
    "dataInputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      }
    ],
    "outputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "value": 147,
        "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
        "creationHeight": 9149,
        "assets": [
          {
            "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 1000
          }
        ],
        "additionalRegisters": {
          "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
        },
        "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "index": 0
      }
    ],
    "size": 0
  }
]';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetc...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|Transactions|true|none|
Example responses
200 Response
=== "json"
```json
{
  "msg": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
  "b": 987654321,
  "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
  "proof": {
    "msgPreimage": "0112e03c6d39d32509855be7cee9b62ff921f7a0cf6883e232474bd5b54d816dd056f846980d34c3b23098bdcf41222f8cdee5219224aa67750055926c3a2310a483accc4f9153e7a760615ea972ac67911cff111f8c17f563d6147205f58f85133ae695d1d4157e4aecdbbb29952cfa42b75129db55bddfce3bc53b8fd5b5465f10d8be8ddda62ed3b86afb0497ff2d381ed884bdae5287d20667def224a28d2b6e3ebfc78709780702c70bd8df0e000000",
    "txProofs": [
      {
        "leaf": "cd665e49c834b0c25574fcb19a158d836f3f2aad8e91ac195f972534c25449b3",
        "levels": [
          [
            "018b7ae20a4acd23e3f1bf38671ce97103ad96d8f1c780b5e5e865e4873ae16337",
            0
          ]
        ]
      }
    ]
  }
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|External candidate|WorkMessage|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### miningReadMinerRewardAddress
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /mining/rewardAddress \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
GET /mining/rewardAddress HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/mining/rewardAddress',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.get '/mining/rewardAddress',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.get('/mining/rewardAddress', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/mining/rewardAddress', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/mining/rewardAddress");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.p...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Miner Reward Script (in P2S format)|RewardAddress|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### miningReadMinerRewardPubkey
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /mining/rewardPublicKey \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
GET /mining/rewardPublicKey HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/mining/rewardPublicKey',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.get '/mining/rewardPublicKey',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.get('/mining/rewardPublicKey', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/mining/rewardPublicKey', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/mining/rewardPublicKey");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close()...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Public key for miner rewards (as hex-encoded secp256k1 point)|RewardPubKey|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### miningSubmitSolution
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /mining/solution \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /mining/solution HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '{
  "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
  "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
  "n": "0000000000000000",
  "d": 987654321
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/mining/solution',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.post '/mining/solution',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.post('/mining/solution', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/mining/solution', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|PowSolutions|true|none|
Example responses
400 Response
=== "json"
```json
{
  "error": 500,
  "reason": "Internal server error",
  "detail": "string"
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Solution is valid|None|
|400|Bad Request|Solution is invalid|ApiError|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### getBoxesBinaryProof
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /utxo/getBoxesBinaryProof \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /utxo/getBoxesBinaryProof HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '[
  "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
]';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/utxo/getBoxesBinaryProof',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.post '/utxo/getBoxesBinaryProof',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.post('/utxo/getBoxesBinaryProof', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/utxo/getBoxesBinaryProof', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/utxo/getBoxesBinaryProof");
HttpURLConnection co...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|TransactionBoxId|true|none|
Example responses
200 Response
=== "json"
```json
"3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Serialized batch proof|SerializedAdProof|
|400|Bad Request|Prove error|ApiError|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### getBoxById
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /utxo/byId/{boxId} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /utxo/byId/{boxId} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/utxo/byId/{boxId}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/utxo/byId/{boxId}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/utxo/byId/{boxId}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/utxo/byId/{boxId}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/utxo/byId/{boxId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string]...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|boxId|path|string|true|ID of a wanted box|
Example responses
200 Response
=== "json"
```json
{
  "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "value": 147,
  "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
  "creationHeight": 9149,
  "assets": [
    {
      "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "amount": 1000
    }
  ],
  "additionalRegisters": {
    "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
  },
  "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "index": 0
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Box object|ErgoTransactionOutput|
|404|Not Found|Box with this id doesn't exist|ApiError|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getBoxByIdBinary
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /utxo/byIdBinary/{boxId} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /utxo/byIdBinary/{boxId} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/utxo/byIdBinary/{boxId}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/utxo/byIdBinary/{boxId}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/utxo/byIdBinary/{boxId}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/utxo/byIdBinary/{boxId}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/utxo/byIdBinary/{boxId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"
       "net/http"
)
...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|boxId|path|string|true|ID of a wanted box|
Example responses
200 Response
=== "json"
```json
{
  "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "bytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Json containing box identifier and hex-encoded box bytes|SerializedBox|
|404|Not Found|Box with this id doesn't exist|ApiError|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getBoxWithPoolById
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /utxo/withPool/byId/{boxId} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /utxo/withPool/byId/{boxId} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/utxo/withPool/byId/{boxId}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/utxo/withPool/byId/{boxId}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/utxo/withPool/byId/{boxId}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/utxo/withPool/byId/{boxId}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/utxo/withPool/byId/{boxId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|boxId|path|string|true|ID of a box to obtain|
Example responses
200 Response
=== "json"
```json
{
  "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "value": 147,
  "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
  "creationHeight": 9149,
  "assets": [
    {
      "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "amount": 1000
    }
  ],
  "additionalRegisters": {
    "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
  },
  "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "index": 0
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Box object|ErgoTransactionOutput|
|404|Not Found|Box with this id doesn't exist|ApiError|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getBoxWithPoolByIds
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /utxo/withPool/byIds \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'
```
=== "http"
```http
POST /utxo/withPool/byIds HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '[
  "string"
]';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/utxo/withPool/byIds',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/utxo/withPool/byIds',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/utxo/withPool/byIds', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/utxo/withPool/byIds', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/utxo/withPool/byIds");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String input...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|array[string]|true|none|
Example responses
200 Response
=== "json"
```json
[
  {
    "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "value": 147,
    "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
    "creationHeight": 9149,
    "assets": [
      {
        "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "amount": 1000
      }
    ],
    "additionalRegisters": {
      "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
    },
    "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "index": 0
  }
]
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Box object|Inline|
|404|Not Found|No any box exists for every id provided|ApiError|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[ErgoTransactionOutput]|false|none|none|
|» boxId|TransactionBoxId(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|» value|integer(int64)|true|none|Amount of Ergo token|
|» ergoTree|ErgoTree(base16)|true|none|Base16-encoded ergo tree bytes|
|» creationHeight|integer(int32)|true|none|Height the output was created at|
|» assets|[Asset]|false|none|Assets list in the transaction|
|»» tokenId|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|»» amount|integer(int64)|true|none|Amount of the token|
|» additionalRegisters|Registers|true|none|Ergo box registers|
|»» additionalProperties|SValue(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|» transactionId|TransactionId(base16)|false|none|Base16-encoded transaction id bytes|
|» index|integer(int32)|false|none|Index in the transaction outputs|
This operation does not require authentication

#### getBoxWithPoolByIdBinary
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /utxo/withPool/byIdBinary/{boxId} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /utxo/withPool/byIdBinary/{boxId} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/utxo/withPool/byIdBinary/{boxId}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/utxo/withPool/byIdBinary/{boxId}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/utxo/withPool/byIdBinary/{boxId}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/utxo/withPool/byIdBinary/{boxId}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/utxo/withPool/byIdBinary/{boxId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
`...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|boxId|path|string|true|ID of a wanted box|
Example responses
200 Response
=== "json"
```json
{
  "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "bytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Json containing box identifier and hex-encoded box bytes|SerializedBox|
|404|Not Found|Box with this id doesn't exist|ApiError|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getSnapshotsInfo
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /utxo/getSnapshotsInfo
```
=== "http"
```http
GET /utxo/getSnapshotsInfo HTTP/1.1
```
=== "javascript"
```javascript

fetch('/utxo/getSnapshotsInfo',
{
  method: 'GET'

})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

result = RestClient.get '/utxo/getSnapshotsInfo',
  params: {
  }

p JSON.parse(result)
```
=== "python"
```python
import requests

r = requests.get('/utxo/getSnapshotsInfo')

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/utxo/getSnapshotsInfo', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/utxo/getSnapshotsInfo");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    data := bytes.NewBuffer([]byte{jsonReq})
    req, err := http.NewRequest("GET", "/utxo/getSnapshotsInfo", data)
    req.Header = headers

    client := &http.Client{}
    resp, err := client.Do(req)
    // ...
}
```
GET /utxo/getSnapshotsInfo
Get information about locally stored UTXO snapshots

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|A list of saved snapshots|None|
This operation does not require authentication

#### genesisBoxes
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /utxo/genesis \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /utxo/genesis HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/utxo/genesis',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/utxo/genesis',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/utxo/genesis', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/utxo/genesis', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/utxo/genesis");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]string{
        "Accept": []strin...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|A list of all the genesis boxes|Inline|
|404|Not Found|Box with this id doesn't exist|ApiError|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[ErgoTransactionOutput]|false|none|none|
|» boxId|TransactionBoxId(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|» value|integer(int64)|true|none|Amount of Ergo token|
|» ergoTree|ErgoTree(base16)|true|none|Base16-encoded ergo tree bytes|
|» creationHeight|integer(int32)|true|none|Height the output was created at|
|» assets|[Asset]|false|none|Assets list in the transaction|
|»» tokenId|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|»» amount|integer(int64)|true|none|Amount of the token|
|» additionalRegisters|Registers|true|none|Ergo box registers|
|»» additionalProperties|SValue(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|» transactionId|TransactionId(base16)|false|none|Base16-encoded transaction id bytes|
|» index|integer(int32)|false|none|Index in the transaction outputs|
This operation does not require authentication

#### scriptP2SAddress
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /script/p2sAddress \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /script/p2sAddress HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '{
  "source": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/script/p2sAddress',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.post '/script/p2sAddress',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.post('/script/p2sAddress', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/script/p2sAddress', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/script/p2sAddress");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = co...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|SourceHolder|true|none|
Example responses
200 Response
=== "json"
```json
{
  "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Ergo address derived from source|AddressHolder|
|400|Bad Request|Bad source|ApiError|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### scriptP2SHAddress
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /script/p2shAddress \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /script/p2shAddress HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '{
  "source": "string"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/script/p2shAddress',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.post '/script/p2shAddress',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.post('/script/p2shAddress', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/script/p2shAddress', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/script/p2shAddress");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCo...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|SourceHolder|true|none|
Example responses
200 Response
=== "json"
```json
{
  "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|P2SH address derived from source|AddressHolder|
|400|Bad Request|Bad source|ApiError|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### addressToTree
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /script/addressToTree/{address} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /script/addressToTree/{address} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/script/addressToTree/{address}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/script/addressToTree/{address}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/script/addressToTree/{address}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/script/addressToTree/{address}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/script/addressToTree/{address}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package m...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|address|path|ErgoAddress|true|address to get a script from|
Example responses
200 Response
=== "json"
```json
{
  "tree": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3"
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Base16-encoded ErgoTree (script)|ErgoTreeObject|
|default|Default|Error|ApiError|
This operation does not require authentication

#### addressToBytes
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /script/addressToBytes/{address} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /script/addressToBytes/{address} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/script/addressToBytes/{address}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/script/addressToBytes/{address}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/script/addressToBytes/{address}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/script/addressToBytes/{address}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/script/addressToBytes/{address}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
pa...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|address|path|ErgoAddress|true|address to get a script from|
Example responses
200 Response
=== "json"
```json
{
  "bytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Base16-encoded Sigma byte array constant which contains script bytes|ScriptBytes|
|default|Default|Error|ApiError|
This operation does not require authentication

#### executeWithContext
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /script/executeWithContext \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /script/executeWithContext HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '{
  "script": "string",
  "namedConstants": {},
  "context": {
    "lastBlockUtxoRoot": {
      "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "treeFlags": 0,
      "keyLength": 0,
      "valueLength": 0
    },
    "headers": [
      {
        "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "timestamp": 1524143059077,
        "version": 2,
        "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "stateRoot": {
          "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "treeFlags": 0,
          "keyLength": 0,
          "valueLength": 0
        },
        "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "nBits": 19857408,
        "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "extensionRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "height": 667,
        "size": 667,
        "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "powSolutions": {
          "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
          "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
       ...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|ExecuteScript|true|none|
Example responses
200 Response
=== "json"
```json
{
  "value": {
    "op": -45,
    "condition": true
  },
  "cost": 10
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Result of reduceToCrypto|CryptoResult|
|400|Bad Request|Compiler error|ApiError|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### registerScan
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /scan/register \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /scan/register HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '{
  "scanName": "Assets Tracker",
  "walletInteraction": "off",
  "removeOffchain": true,
  "trackingRule": {
    "predicate": "containsAsset",
    "assetId": "02dada811a888cd0dc7a0a41739a3ad9b0f427741fe6ca19700cf1a51200c96bf7"
  }
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/scan/register',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.post '/scan/register',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.post('/scan/register', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/scan/register', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|ScanRequest|true|none|
Example responses
200 Response
=== "json"
```json
{
  "scanId": 0
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Identifier of a scan generated|ScanId|
|400|Bad Request|Bad request|ApiError|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### deregisterScan
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /scan/deregister \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /scan/deregister HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '{
  "scanId": 0
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/scan/deregister',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.post '/scan/deregister',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.post('/scan/deregister', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/scan/deregister', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/scan/deregister");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|ScanId|true|none|
Example responses
200 Response
=== "json"
```json
{
  "scanId": 0
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Identifier of a scan removed|ScanId|
|400|Bad Request|No scan found|ApiError|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### listAllScans
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /scan/listAll \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
GET /scan/listAll HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/scan/listAll',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.get '/scan/listAll',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.get('/scan/listAll', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/scan/listAll', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/scan/listAll");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package ...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|List of scans registered|Inline|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[Scan]|false|none|none|
|» scanName|string|false|none|none|
|» scanId|integer|false|none|none|
|» walletInteraction|string|false|none|none|
|» removeOffchain|boolean|false|none|none|
|» trackingRule|ScanningPredicate|false|none|none|
|»» predicate|string|true|none|none|

###### Enumerated Values
|Property|Value|
|---|---|
|walletInteraction|off|
|walletInteraction|shared|
|walletInteraction|forced|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### listUnspentScans
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /scan/unspentBoxes/{scanId} \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
GET /scan/unspentBoxes/{scanId} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/scan/unspentBoxes/{scanId}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.get '/scan/unspentBoxes/{scanId}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.get('/scan/unspentBoxes/{scanId}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/scan/unspentBoxes/{scanId}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/scan/unspentBoxes/{scanId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.app...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scanId|path|integer(int32)|true|identifier of a scan|
|minConfirmations|query|integer(int32)|false|Minimal number of confirmations, -1 means we consider unconfirmed|
|maxConfirmations|query|integer(int32)|false|Maximum number of confirmations, -1 means unlimited|
|minInclusionHeight|query|integer(int32)|false|Minimal box inclusion height|
|maxInclusionHeight|query|integer(int32)|false|Maximum box inclusion height, -1 means unlimited|
Example responses
200 Response
=== "json"
```json
[
  {
    "box": {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0
    },
    "confirmationsNum": 147,
    "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
    "creationTransaction": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "spendingTransaction": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "spendingHeight": 147,
    "inclusionHeight": 147,
    "onchain": true,
    "spent": false,
    "creationOutIndex": 2,
    "scans": [
      1
    ]
  }
]
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|List of unspent boxes|Inline|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[WalletBox]|false|none|none|
|» box|ErgoTransactionOutput|true|none|none|
|»» boxId|TransactionBoxId(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» value|integer(int64)|true|none|Amount of Ergo token|
|»» ergoTree|ErgoTree(base16)|true|none|Base16-encoded ergo tree bytes|
|»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»» assets|[Asset]|false|none|Assets list in the transaction|
|»»» tokenId|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|»»» amount|integer(int64)|true|none|Amount of the token|
|»» additionalRegisters|Registers|true|none|Ergo box registers|
|»»» additionalProperties|SValue(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»» transactionId|TransactionId(base16)|false|none|Base16-encoded transaction id bytes|
|»» index|integer(int32)|false|none|Index in the transaction outputs|
|» confirmationsNum|integer(int32)¦null|true|none|Number of confirmations, if the box is included into the blockchain|
|» address|ErgoAddress|true|none|Encoded Ergo Address|
|» creationTransaction|ModifierId(base16)|true|none|Base16-encoded 32 byte modifier id|
|» spendingTransaction|ModifierId(base16)|true|none|Base16-encoded 32 byte modifier id|
|» spendingHeight|integer(int32)¦null|true|none|The height the box was spent at|
|» inclusionHeight|integer(int32)|true|none|The height the transaction containing the box was included in a block at|
|» onchain|boolean|true|none|A flag signalling whether the box is created on main chain|
|» spent|boolean|true|none|A flag signalling whether the box was spent|
|» creationOutIndex|integer(int32)|true|none|An index of a box in the creating transaction|
|» scans|[integer]|true|none|Scan identifiers the box relates to|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### listSpentScans
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /scan/spentBoxes/{scanId} \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
GET /scan/spentBoxes/{scanId} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/scan/spentBoxes/{scanId}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.get '/scan/spentBoxes/{scanId}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.get('/scan/spentBoxes/{scanId}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/scan/spentBoxes/{scanId}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/scan/spentBoxes/{scanId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine)...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|scanId|path|integer(int32)|true|identifier of a scan|
|minConfirmations|query|integer(int32)|false|Minimal number of confirmations, -1 means we consider unconfirmed|
|maxConfirmations|query|integer(int32)|false|Maximum number of confirmations, -1 means unlimited|
|minInclusionHeight|query|integer(int32)|false|Minimal box inclusion height|
|maxInclusionHeight|query|integer(int32)|false|Maximum box inclusion height, -1 means unlimited|
Example responses
200 Response
=== "json"
```json
[
  {
    "box": {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0
    },
    "confirmationsNum": 147,
    "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
    "creationTransaction": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "spendingTransaction": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "spendingHeight": 147,
    "inclusionHeight": 147,
    "onchain": true,
    "spent": false,
    "creationOutIndex": 2,
    "scans": [
      1
    ]
  }
]
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|List of spent boxes|Inline|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[WalletBox]|false|none|none|
|» box|ErgoTransactionOutput|true|none|none|
|»» boxId|TransactionBoxId(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» value|integer(int64)|true|none|Amount of Ergo token|
|»» ergoTree|ErgoTree(base16)|true|none|Base16-encoded ergo tree bytes|
|»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»» assets|[Asset]|false|none|Assets list in the transaction|
|»»» tokenId|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|»»» amount|integer(int64)|true|none|Amount of the token|
|»» additionalRegisters|Registers|true|none|Ergo box registers|
|»»» additionalProperties|SValue(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»» transactionId|TransactionId(base16)|false|none|Base16-encoded transaction id bytes|
|»» index|integer(int32)|false|none|Index in the transaction outputs|
|» confirmationsNum|integer(int32)¦null|true|none|Number of confirmations, if the box is included into the blockchain|
|» address|ErgoAddress|true|none|Encoded Ergo Address|
|» creationTransaction|ModifierId(base16)|true|none|Base16-encoded 32 byte modifier id|
|» spendingTransaction|ModifierId(base16)|true|none|Base16-encoded 32 byte modifier id|
|» spendingHeight|integer(int32)¦null|true|none|The height the box was spent at|
|» inclusionHeight|integer(int32)|true|none|The height the transaction containing the box was included in a block at|
|» onchain|boolean|true|none|A flag signalling whether the box is created on main chain|
|» spent|boolean|true|none|A flag signalling whether the box was spent|
|» creationOutIndex|integer(int32)|true|none|An index of a box in the creating transaction|
|» scans|[integer]|true|none|Scan identifiers the box relates to|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### scanStopTracking
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /scan/stopTracking \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /scan/stopTracking HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '{
  "scanId": 0,
  "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/scan/stopTracking',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.post '/scan/stopTracking',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.post('/scan/stopTracking', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/scan/stopTracking', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/scan/stopTracking");
HttpURLConnection con = (HttpURLConnection) o...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|ScanIdBoxId|true|none|
Example responses
200 Response
=== "json"
```json
{
  "scanId": 0,
  "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|The box is not tracked anymore|ScanIdBoxId|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### scriptP2SRule
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /scan/p2sRule \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /scan/p2sRule HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '4MQyML64GnzMxZgm';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/scan/p2sRule',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.post '/scan/p2sRule',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.post('/scan/p2sRule', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/scan/p2sRule', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/scan/p2sRule");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = ne...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|string|true|none|
Example responses
200 Response
=== "json"
```json
{
  "scanId": 0
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Id of custom scan generated and registered|ScanId|
|400|Bad Request|Bad source|ApiError|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### addBox
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /scan/addBox \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /scan/addBox HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '{
  "scanIds": [
    0
  ],
  "box": {
    "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "value": 147,
    "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
    "creationHeight": 9149,
    "assets": [
      {
        "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "amount": 1000
      }
    ],
    "additionalRegisters": {
      "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
    },
    "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "index": 0
  }
}';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/scan/addBox',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.post '/scan/addBox',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.post('/scan/addBox', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$cl...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|ScanIdsBox|true|none|
Example responses
200 Response
=== "json"
```json
"2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|It the box is added successfully, then its id is returned|TransactionId|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### nodeShutdown
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /node/shutdown \
  -H 'Accept: application/json' \
  -H 'api_key: API_KEY'
```
=== "http"
```http
POST /node/shutdown HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json',
  'api_key':'API_KEY'
};

fetch('/node/shutdown',
{
  method: 'POST',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json',
  'api_key' => 'API_KEY'
}

result = RestClient.post '/node/shutdown',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json',
  'api_key': 'API_KEY'
}

r = requests.post('/node/shutdown', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
    'api_key' => 'API_KEY',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/node/shutdown', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/node/shutdown");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|The node will be shut down in 5 seconds|None|
|default|Default|Error|ApiError|
To perform this operation, you must be authenticated by means of one of the following methods:
ApiKeyAuth ( Scopes: api_key )

#### emissionAt
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /emission/at/{blockHeight} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /emission/at/{blockHeight} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/emission/at/{blockHeight}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/emission/at/{blockHeight}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/emission/at/{blockHeight}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/emission/at/{blockHeight}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/emission/at/{blockHeight}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"
      ...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|blockHeight|path|integer(int32)|true|Height to get emission data for|
Example responses
200 Response
=== "json"
```json
{
  "minerReward": 0,
  "totalCoinsIssued": 0,
  "totalRemainCoins": 0,
  "reemitted": 0
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Emission data|EmissionInfo|
|default|Default|Error|ApiError|
This operation does not require authentication

#### emissionScripts
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /emission/scripts \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /emission/scripts HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/emission/scripts',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/emission/scripts',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/emission/scripts', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/emission/scripts', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/emission/scripts");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    headers := map[string][]strin...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|Emission-related scripts|EmissionScripts|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getIndexedHeight
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /blockchain/indexedHeight \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /blockchain/indexedHeight HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/blockchain/indexedHeight',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/blockchain/indexedHeight',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/blockchain/indexedHeight', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/blockchain/indexedHeight', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/blockchain/indexedHeight");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"
       "net/h...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|height of the indexer and full height|Inline|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» indexedHeight|integer|false|none|number of blocks indexed|
|» fullHeight|integer|false|none|number of all known blocks|
This operation does not require authentication

#### getTxById
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /blockchain/transaction/byId/{txId} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /blockchain/transaction/byId/{txId} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/blockchain/transaction/byId/{txId}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/blockchain/transaction/byId/{txId}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/blockchain/transaction/byId/{txId}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/blockchain/transaction/byId/{txId}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/blockchain/transaction/byId/{txId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|txId|path|string|true|id of the wanted transaction|
Example responses
200 Response
=== "json"
```json
{
  "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "inputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "spendingProof": {
        "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "extension": {
          "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
        }
      }
    }
  ],
  "dataInputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    }
  ],
  "outputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0
    }
  ],
  "inclusionHeight": 20998,
  "numConfirmations": 20998,
  "blockId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "timestamp": 1524143059077,
  "index": 3,
  "globalIndex": 3565445,
  "size": 0
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|transaction with wanted id|IndexedErgoTransaction|
|404|Not Found|Transaction with this id doesn't exist|ApiError|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getTxByIndex
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /blockchain/transaction/byIndex/{txIndex} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /blockchain/transaction/byIndex/{txIndex} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/blockchain/transaction/byIndex/{txIndex}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/blockchain/transaction/byIndex/{txIndex}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/blockchain/transaction/byIndex/{txIndex}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/blockchain/transaction/byIndex/{txIndex}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/blockchain/transaction/byIndex/{txIndex}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|txIndex|path|number|true|index of the wanted transaction|
Example responses
200 Response
=== "json"
```json
{
  "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "inputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "spendingProof": {
        "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "extension": {
          "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
        }
      }
    }
  ],
  "dataInputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    }
  ],
  "outputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0
    }
  ],
  "inclusionHeight": 20998,
  "numConfirmations": 20998,
  "blockId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "timestamp": 1524143059077,
  "index": 3,
  "globalIndex": 3565445,
  "size": 0
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|transaction with wanted index|IndexedErgoTransaction|
|404|Not Found|Transaction with this index doesn't exist|ApiError|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getTxsByAddress
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /blockchain/transaction/byAddress \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'
```
=== "http"
```http
POST /blockchain/transaction/byAddress HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '"3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/blockchain/transaction/byAddress',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/blockchain/transaction/byAddress',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/blockchain/transaction/byAddress', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/blockchain/transaction/byAddress', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/blockchain/transaction/byAddress");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseC...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|offset|query|integer(int32)|false|amount of elements to skip from the start|
|limit|query|integer(int32)|false|amount of elements to retrieve|
|body|body|string|true|none|
Example responses
200 Response
=== "json"
```json
{
  "items": [
    {
      "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "inputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "spendingProof": {
            "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extension": {
              "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
            }
          }
        }
      ],
      "dataInputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        }
      ],
      "outputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0
        }
      ],
      "inclusionHeight": 20998,
      "numConfirmations": 20998,
      "blockId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40a...

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|transactions associated with wanted address|Inline|
|404|Not Found|No transactions found for wanted address|ApiError|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» items|[IndexedErgoTransaction]|false|none|Array of transactions|
|»» id|TransactionId(base16)|true|none|Base16-encoded transaction id bytes|
|»» inputs|[ErgoTransactionInput]|true|none|Transaction inputs|
|»»» boxId|TransactionBoxId(base16)|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»»» spendingProof|SpendingProof|true|none|Spending proof for transaction input|
|»»»» proofBytes|SpendingProofBytes(base16)|true|none|Base16-encoded spending proofs|
|»»»» extension|object|true|none|Variables to be put into context|
|»»»»» additionalProperties|SValue(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»» dataInputs|[ErgoTransactionDataInput]|true|none|Transaction data inputs|
|»»» boxId|TransactionBoxId(base16)|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» outputs|[ErgoTransactionOutput]|true|none|Transaction outputs|
|»»» boxId|TransactionBoxId(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»»» value|integer(int64)|true|none|Amount of Ergo token|
|»»» ergoTree|ErgoTree(base16)|true|none|Base16-encoded ergo tree bytes|
|»»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»»» assets|[Asset]|false|none|Assets list in the transaction|
|»»»» tokenId|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|»»»» amount|integer(int64)|true|none|Amount of the token|
|»»» additionalRegisters|Registers|true|none|Ergo box registers|
|»»»» additionalProperties|SValue(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»»» transactionId|TransactionId(base16)|false|none|Base16-encoded transaction id bytes|
|»»» index|integer(int32)|false|none|Index in the transaction outputs|
|»» inclusionHeight|integer(int32)|true|none|Height of a block the transaction was included in|
|»» numConfirmations|integer(int32)|true|none|Number of transaction c...

#### getTxRange
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /blockchain/transaction/range \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /blockchain/transaction/range HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/blockchain/transaction/range',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/blockchain/transaction/range',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/blockchain/transaction/range', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/blockchain/transaction/range', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/blockchain/transaction/range");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|offset|query|integer(int32)|false|amount of elements to skip from the start|
|limit|query|integer(int32)|false|amount of elements to retrieve|
Example responses
200 Response
=== "json"
```json
[
  "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
]
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|transactions ids in wanted range|Inline|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
Array of transaction ids
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[ModifierId]|false|none|Array of transaction ids|
This operation does not require authentication

#### getBoxById
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /blockchain/box/byId/{boxId} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /blockchain/box/byId/{boxId} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/blockchain/box/byId/{boxId}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/blockchain/box/byId/{boxId}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/blockchain/box/byId/{boxId}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/blockchain/box/byId/{boxId}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/blockchain/box/byId/{boxId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       ...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|boxId|path|string|true|id of the wanted box|
Example responses
200 Response
=== "json"
```json
{
  "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "value": 147,
  "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
  "creationHeight": 9149,
  "assets": [
    {
      "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "amount": 1000
    }
  ],
  "additionalRegisters": {
    "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
  },
  "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "index": 0,
  "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
  "spentTransactionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "spendingHeight": 147,
  "inclusionHeight": 147,
  "globalIndex": 83927
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|box with wanted id|IndexedErgoBox|
|404|Not Found|No box found with wanted id|ApiError|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getBoxByIndex
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /blockchain/box/byIndex/{boxIndex} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /blockchain/box/byIndex/{boxIndex} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/blockchain/box/byIndex/{boxIndex}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/blockchain/box/byIndex/{boxIndex}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/blockchain/box/byIndex/{boxIndex}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/blockchain/box/byIndex/{boxIndex}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/blockchain/box/byIndex/{boxIndex}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
===...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|boxIndex|path|number|true|index of the wanted box|
Example responses
200 Response
=== "json"
```json
{
  "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "value": 147,
  "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
  "creationHeight": 9149,
  "assets": [
    {
      "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "amount": 1000
    }
  ],
  "additionalRegisters": {
    "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
  },
  "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "index": 0,
  "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
  "spentTransactionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "spendingHeight": 147,
  "inclusionHeight": 147,
  "globalIndex": 83927
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|box with wanted index|IndexedErgoBox|
|404|Not Found|Box with this index doesn't exist|ApiError|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getBoxesByTokenId
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /blockchain/box/byTokenId/{tokenId} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /blockchain/box/byTokenId/{tokenId} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/blockchain/box/byTokenId/{tokenId}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/blockchain/box/byTokenId/{tokenId}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/blockchain/box/byTokenId/{tokenId}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/blockchain/box/byTokenId/{tokenId}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/blockchain/box/byTokenId/{tokenId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|tokenId|path|ModifierId|true|id of the token|
|offset|query|integer(int32)|false|amount of elements to skip from the start|
|limit|query|integer(int32)|false|amount of elements to retrieve|
Example responses
200 Response
=== "json"
```json
{
  "items": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0,
      "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
      "spentTransactionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "spendingHeight": 147,
      "inclusionHeight": 147,
      "globalIndex": 83927
    }
  ],
  "total": 0
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|boxes associated with wanted token|Inline|
|404|Not Found|No boxes found for wanted token|ApiError|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» items|[allOf]|false|none|Array of boxes|
allOf
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» anonymous|ErgoTransactionOutput|false|none|none|
|»»» boxId|TransactionBoxId(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»»» value|integer(int64)|true|none|Amount of Ergo token|
|»»» ergoTree|ErgoTree(base16)|true|none|Base16-encoded ergo tree bytes|
|»»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»»» assets|[Asset]|false|none|Assets list in the transaction|
|»»»» tokenId|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|»»»» amount|integer(int64)|true|none|Amount of the token|
|»»» additionalRegisters|Registers|true|none|Ergo box registers|
|»»»» additionalProperties|SValue(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»»» transactionId|TransactionId(base16)|false|none|Base16-encoded transaction id bytes|
|»»» index|integer(int32)|false|none|Index in the transaction outputs|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» anonymous|object|false|none|Box indexed with extra information|
|»»» address|ErgoAddress|true|none|Encoded Ergo Address|
|»»» spentTransactionId|ModifierId(base16)|true|none|Base16-encoded 32 byte modifier id|
|»»» spendingHeight|integer(int32)¦null|true|none|The height the box was spent at|
|»»» inclusionHeight|integer(int32)|true|none|The height the transaction containing the box was included in a block at|
|»»» globalIndex|integer(int64)|true|none|Global index of the output in the blockchain|
continued
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» total|integer|false|none|Total number of retreived boxes|
This operation does not require authentication

#### getBoxesByTokenIdUnspent
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /blockchain/box/unspent/byTokenId/{tokenId} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /blockchain/box/unspent/byTokenId/{tokenId} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/blockchain/box/unspent/byTokenId/{tokenId}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/blockchain/box/unspent/byTokenId/{tokenId}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/blockchain/box/unspent/byTokenId/{tokenId}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/blockchain/box/unspent/byTokenId/{tokenId}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/blockchain/box/unspent/byTokenId/{tokenId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|tokenId|path|ModifierId|true|id of the token|
|offset|query|integer(int32)|false|amount of elements to skip from the start|
|limit|query|integer(int32)|false|amount of elements to retrieve|
|sortDirection|query|string|false|desc = new boxes first ; asc = old boxes first|
|includeUnconfirmed|query|boolean|false|if true include unconfirmed transactions from mempool|
Example responses
200 Response
=== "json"
```json
[
  {
    "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "value": 147,
    "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
    "creationHeight": 9149,
    "assets": [
      {
        "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "amount": 1000
      }
    ],
    "additionalRegisters": {
      "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
    },
    "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "index": 0,
    "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
    "spentTransactionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "spendingHeight": 147,
    "inclusionHeight": 147,
    "globalIndex": 83927
  }
]
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|unspent boxes associated with wanted token|Inline|
|404|Not Found|No unspent boxes found for wanted token|ApiError|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
Array of boxes
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[allOf]|false|none|Array of boxes|
allOf
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» anonymous|ErgoTransactionOutput|false|none|none|
|»» boxId|TransactionBoxId(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» value|integer(int64)|true|none|Amount of Ergo token|
|»» ergoTree|ErgoTree(base16)|true|none|Base16-encoded ergo tree bytes|
|»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»» assets|[Asset]|false|none|Assets list in the transaction|
|»»» tokenId|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|»»» amount|integer(int64)|true|none|Amount of the token|
|»» additionalRegisters|Registers|true|none|Ergo box registers|
|»»» additionalProperties|SValue(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»» transactionId|TransactionId(base16)|false|none|Base16-encoded transaction id bytes|
|»» index|integer(int32)|false|none|Index in the transaction outputs|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» anonymous|object|false|none|Box indexed with extra information|
|»» address|ErgoAddress|true|none|Encoded Ergo Address|
|»» spentTransactionId|ModifierId(base16)|true|none|Base16-encoded 32 byte modifier id|
|»» spendingHeight|integer(int32)¦null|true|none|The height the box was spent at|
|»» inclusionHeight|integer(int32)|true|none|The height the transaction containing the box was included in a block at|
|»» globalIndex|integer(int64)|true|none|Global index of the output in the blockchain|
This operation does not require authentication

#### getBoxesByAddress
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /blockchain/box/byAddress \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'
```
=== "http"
```http
POST /blockchain/box/byAddress HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '"3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/blockchain/box/byAddress',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/blockchain/box/byAddress',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/blockchain/box/byAddress', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/blockchain/box/byAddress', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/blockchain/box/byAddress");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new Buf...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|offset|query|integer(int32)|false|amount of elements to skip from the start|
|limit|query|integer(int32)|false|amount of elements to retrieve|
|body|body|string|true|none|
Example responses
200 Response
=== "json"
```json
{
  "items": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0,
      "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
      "spentTransactionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "spendingHeight": 147,
      "inclusionHeight": 147,
      "globalIndex": 83927
    }
  ],
  "total": 0
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|boxes associated with wanted address|Inline|
|404|Not Found|No boxes found for wanted address|ApiError|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» items|[allOf]|false|none|Array of boxes|
allOf
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» anonymous|ErgoTransactionOutput|false|none|none|
|»»» boxId|TransactionBoxId(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»»» value|integer(int64)|true|none|Amount of Ergo token|
|»»» ergoTree|ErgoTree(base16)|true|none|Base16-encoded ergo tree bytes|
|»»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»»» assets|[Asset]|false|none|Assets list in the transaction|
|»»»» tokenId|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|»»»» amount|integer(int64)|true|none|Amount of the token|
|»»» additionalRegisters|Registers|true|none|Ergo box registers|
|»»»» additionalProperties|SValue(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»»» transactionId|TransactionId(base16)|false|none|Base16-encoded transaction id bytes|
|»»» index|integer(int32)|false|none|Index in the transaction outputs|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» anonymous|object|false|none|Box indexed with extra information|
|»»» address|ErgoAddress|true|none|Encoded Ergo Address|
|»»» spentTransactionId|ModifierId(base16)|true|none|Base16-encoded 32 byte modifier id|
|»»» spendingHeight|integer(int32)¦null|true|none|The height the box was spent at|
|»»» inclusionHeight|integer(int32)|true|none|The height the transaction containing the box was included in a block at|
|»»» globalIndex|integer(int64)|true|none|Global index of the output in the blockchain|
continued
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» total|integer|false|none|Total number of retreived boxes|
This operation does not require authentication

#### getBoxesByAddressUnspent
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /blockchain/box/unspent/byAddress \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'
```
=== "http"
```http
POST /blockchain/box/unspent/byAddress HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '"3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/blockchain/box/unspent/byAddress',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/blockchain/box/unspent/byAddress',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/blockchain/box/unspent/byAddress', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/blockchain/box/unspent/byAddress', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/blockchain/box/unspent/byAddress");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseC...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|offset|query|integer(int32)|false|amount of elements to skip from the start|
|limit|query|integer(int32)|false|amount of elements to retrieve|
|sortDirection|query|string|false|desc = new boxes first ; asc = old boxes first|
|includeUnconfirmed|query|boolean|false|if true include unconfirmed transactions from mempool|
|body|body|string|true|none|
Example responses
200 Response
=== "json"
```json
[
  {
    "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "value": 147,
    "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
    "creationHeight": 9149,
    "assets": [
      {
        "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "amount": 1000
      }
    ],
    "additionalRegisters": {
      "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
    },
    "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "index": 0,
    "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
    "spentTransactionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "spendingHeight": 147,
    "inclusionHeight": 147,
    "globalIndex": 83927
  }
]
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|unspent boxes associated with wanted address|Inline|
|404|Not Found|No unspent boxes found for wanted address|ApiError|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
Array of boxes
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[allOf]|false|none|Array of boxes|
allOf
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» anonymous|ErgoTransactionOutput|false|none|none|
|»» boxId|TransactionBoxId(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»» value|integer(int64)|true|none|Amount of Ergo token|
|»» ergoTree|ErgoTree(base16)|true|none|Base16-encoded ergo tree bytes|
|»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»» assets|[Asset]|false|none|Assets list in the transaction|
|»»» tokenId|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|»»» amount|integer(int64)|true|none|Amount of the token|
|»» additionalRegisters|Registers|true|none|Ergo box registers|
|»»» additionalProperties|SValue(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»» transactionId|TransactionId(base16)|false|none|Base16-encoded transaction id bytes|
|»» index|integer(int32)|false|none|Index in the transaction outputs|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» anonymous|object|false|none|Box indexed with extra information|
|»» address|ErgoAddress|true|none|Encoded Ergo Address|
|»» spentTransactionId|ModifierId(base16)|true|none|Base16-encoded 32 byte modifier id|
|»» spendingHeight|integer(int32)¦null|true|none|The height the box was spent at|
|»» inclusionHeight|integer(int32)|true|none|The height the transaction containing the box was included in a block at|
|»» globalIndex|integer(int64)|true|none|Global index of the output in the blockchain|
This operation does not require authentication

#### getBoxRange
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /blockchain/box/range \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /blockchain/box/range HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/blockchain/box/range',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/blockchain/box/range',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/blockchain/box/range', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/blockchain/box/range', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/blockchain/box/range");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
package main

import (
       "bytes"
       "net/http"
)

func main() {

    h...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|offset|query|integer(int32)|false|amount of elements to skip from the start|
|limit|query|integer(int32)|false|amount of elements to retrieve|
Example responses
200 Response
=== "json"
```json
[
  "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
]
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|box ids in wanted range|Inline|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
Array of box ids
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[ModifierId]|false|none|Array of box ids|
This operation does not require authentication

#### getBoxesByErgoTree
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /blockchain/box/byErgoTree \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'
```
=== "http"
```http
POST /blockchain/box/byErgoTree HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '"100204a00b08cd021cf943317b0fdb50f60892a46b9132b9ced337c7de79248b104b293d9f1f078eea02d192a39a8cc7a70173007301"';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/blockchain/box/byErgoTree',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/blockchain/box/byErgoTree',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/blockchain/box/byErgoTree', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/blockchain/box/byErgoTree', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/blockchain/box/byErgoTree");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int re...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|offset|query|integer(int32)|false|amount of elements to skip from the start|
|limit|query|integer(int32)|false|amount of elements to retrieve|
|body|body|string|true|none|
Example responses
200 Response
=== "json"
```json
{
  "items": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0,
      "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
      "spentTransactionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "spendingHeight": 147,
      "inclusionHeight": 147,
      "globalIndex": 83927
    }
  ],
  "total": 0
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|boxes with wanted ergotree|Inline|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» items|[allOf]|false|none|Array of boxes|
allOf
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» anonymous|ErgoTransactionOutput|false|none|none|
|»»» boxId|TransactionBoxId(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»»» value|integer(int64)|true|none|Amount of Ergo token|
|»»» ergoTree|ErgoTree(base16)|true|none|Base16-encoded ergo tree bytes|
|»»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»»» assets|[Asset]|false|none|Assets list in the transaction|
|»»»» tokenId|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|»»»» amount|integer(int64)|true|none|Amount of the token|
|»»» additionalRegisters|Registers|true|none|Ergo box registers|
|»»»» additionalProperties|SValue(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»»» transactionId|TransactionId(base16)|false|none|Base16-encoded transaction id bytes|
|»»» index|integer(int32)|false|none|Index in the transaction outputs|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» anonymous|object|false|none|Box indexed with extra information|
|»»» address|ErgoAddress|true|none|Encoded Ergo Address|
|»»» spentTransactionId|ModifierId(base16)|true|none|Base16-encoded 32 byte modifier id|
|»»» spendingHeight|integer(int32)¦null|true|none|The height the box was spent at|
|»»» inclusionHeight|integer(int32)|true|none|The height the transaction containing the box was included in a block at|
|»»» globalIndex|integer(int64)|true|none|Global index of the output in the blockchain|
continued
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» total|integer|false|none|Total number of retreived boxes|
This operation does not require authentication

#### getBoxesByErgoTreeUnspent
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /blockchain/box/unspent/byErgoTree \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'
```
=== "http"
```http
POST /blockchain/box/unspent/byErgoTree HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '"100204a00b08cd021cf943317b0fdb50f60892a46b9132b9ced337c7de79248b104b293d9f1f078eea02d192a39a8cc7a70173007301"';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/blockchain/box/unspent/byErgoTree',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/blockchain/box/unspent/byErgoTree',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/blockchain/box/unspent/byErgoTree', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/blockchain/box/unspent/byErgoTree', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/blockchain/box/unspent/byErgoTree");
HttpURLConnection con = (HttpURLConnection) ob...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|offset|query|integer(int32)|false|amount of elements to skip from the start|
|limit|query|integer(int32)|false|amount of elements to retrieve|
|sortDirection|query|string|false|desc = new boxes first ; asc = old boxes first|
|includeUnconfirmed|query|boolean|false|if true include unconfirmed transactions from mempool|
|body|body|string|true|none|
Example responses
200 Response
=== "json"
```json
{
  "items": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0,
      "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
      "spentTransactionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "spendingHeight": 147,
      "inclusionHeight": 147,
      "globalIndex": 83927
    }
  ],
  "total": 0
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|unspent boxes with wanted ergotree|Inline|
|404|Not Found|No unspent box found with wanted ergotree|ApiError|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» items|[allOf]|false|none|Array of boxes|
allOf
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» anonymous|ErgoTransactionOutput|false|none|none|
|»»» boxId|TransactionBoxId(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|»»» value|integer(int64)|true|none|Amount of Ergo token|
|»»» ergoTree|ErgoTree(base16)|true|none|Base16-encoded ergo tree bytes|
|»»» creationHeight|integer(int32)|true|none|Height the output was created at|
|»»» assets|[Asset]|false|none|Assets list in the transaction|
|»»»» tokenId|Digest32(base16)|true|none|Base16-encoded 32 byte digest|
|»»»» amount|integer(int64)|true|none|Amount of the token|
|»»» additionalRegisters|Registers|true|none|Ergo box registers|
|»»»» additionalProperties|SValue(base16)|false|none|Base-16 encoded serialized Sigma-state value|
|»»» transactionId|TransactionId(base16)|false|none|Base16-encoded transaction id bytes|
|»»» index|integer(int32)|false|none|Index in the transaction outputs|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|»» anonymous|object|false|none|Box indexed with extra information|
|»»» address|ErgoAddress|true|none|Encoded Ergo Address|
|»»» spentTransactionId|ModifierId(base16)|true|none|Base16-encoded 32 byte modifier id|
|»»» spendingHeight|integer(int32)¦null|true|none|The height the box was spent at|
|»»» inclusionHeight|integer(int32)|true|none|The height the transaction containing the box was included in a block at|
|»»» globalIndex|integer(int64)|true|none|Global index of the output in the blockchain|
continued
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» total|integer|false|none|Total number of retreived boxes|
This operation does not require authentication

#### getTokenById
Code samples
=== "shell"
```shell
## You can also use wget
curl -X GET /blockchain/token/byId/{tokenId} \
  -H 'Accept: application/json'
```
=== "http"
```http
GET /blockchain/token/byId/{tokenId} HTTP/1.1

Accept: application/json
```
=== "javascript"
```javascript

const headers = {
  'Accept':'application/json'
};

fetch('/blockchain/token/byId/{tokenId}',
{
  method: 'GET',

  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Accept' => 'application/json'
}

result = RestClient.get '/blockchain/token/byId/{tokenId}',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/blockchain/token/byId/{tokenId}', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('GET','/blockchain/token/byId/{tokenId}', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/blockchain/token/byId/{tokenId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());
```
=== "go"
```go
pa...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|tokenId|path|string|true|id of the wanted token|
Example responses
200 Response
=== "json"
```json
{
  "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "boxId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "emissionAmount": 3500000,
  "name": "string",
  "description": "string",
  "decimals": 8
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|token with wanted id|IndexedToken|
|404|Not Found|No token found with wanted id|ApiError|
|default|Default|Error|ApiError|
This operation does not require authentication

#### getAddressBalanceTotal
Code samples
=== "shell"
```shell
## You can also use wget
curl -X POST /blockchain/balance \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'
```
=== "http"
```http
POST /blockchain/balance HTTP/1.1

Content-Type: application/json
Accept: application/json
```
=== "javascript"
```javascript
const inputBody = '"3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"';
const headers = {
  'Content-Type':'application/json',
  'Accept':'application/json'
};

fetch('/blockchain/balance',
{
  method: 'POST',
  body: inputBody,
  headers: headers
})
.then(function(res) {
    return res.json();
}).then(function(body) {
    console.log(body);
});
```
=== "ruby"
```ruby
require 'rest-client'
require 'json'

headers = {
  'Content-Type' => 'application/json',
  'Accept' => 'application/json'
}

result = RestClient.post '/blockchain/balance',
  params: {
  }, headers: headers

p JSON.parse(result)
```
=== "python"
```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/blockchain/balance', headers = headers)

print(r.json())
```
=== "php"
```php
<?php

require 'vendor/autoload.php';

$headers = array(
    'Content-Type' => 'application/json',
    'Accept' => 'application/json',
);

$client = new \GuzzleHttp\Client();

// Define array of request body.
$request_body = array();

try {
    $response = $client->request('POST','/blockchain/balance', array(
        'headers' => $headers,
        'json' => $request_body,
       )
    );
    print_r($response->getBody()->getContents());
 }
 catch (\GuzzleHttp\Exception\BadResponseException $e) {
    // handle exception or api errors.
    print_r($e->getMessage());
 }

 // ...
```
=== "java"
```java
URL obj = new URL("/blockchain/balance");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con...

#### Parameters
|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|string|true|none|
Example responses
200 Response
=== "json"
```json
{
  "confirmed": {
    "nanoErgs": 0,
    "tokens": [
      {
        "tokenId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "amount": 0,
        "decimals": 0,
        "name": "string"
      }
    ]
  },
  "unconfirmed": {
    "nanoErgs": 0,
    "tokens": [
      {
        "tokenId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "amount": 0,
        "decimals": 0,
        "name": "string"
      }
    ]
  }
}
```

#### Responses
|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|OK|balance information|Inline|
|default|Default|Error|ApiError|

#### Response Schema
Status Code 200
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» confirmed|BalanceInfo|false|none|Balance information|
|»» nanoErgs|integer(int64)|true|none|Balance of nanoERGs|
|»» tokens|[object]|true|none|Balance of tokens|
|»»» tokenId|ModifierId(base16)|false|none|Base16-encoded 32 byte modifier id|
|»»» amount|integer(int64)|false|none|Amount of the token|
|»»» decimals|integer|false|none|Number of decimals of the token|
|»»» name|string|false|none|Name of the token, if any|
|» unconfirmed|BalanceInfo|false|none|Balance information|
This operation does not require authentication

#### ErgoTransactionInput
=== "json"
```json
{
  "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "spendingProof": {
    "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "extension": {
      "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
    }
  }
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|boxId|TransactionBoxId|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|spendingProof|SpendingProof|true|none|Spending proof for transaction input|

#### ErgoTransactionDataInput
=== "json"
```json
{
  "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|boxId|TransactionBoxId|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|

#### ErgoTransactionUnsignedInput
=== "json"
```json
{
  "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "extension": {
    "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
  }
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|boxId|TransactionBoxId|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|extension|object|false|none|none|
|» additionalProperties|SValue|false|none|Base-16 encoded serialized Sigma-state value|

#### SpendingProof
=== "json"
```json
{
  "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "extension": {
    "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
  }
}
```
Spending proof for transaction input

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|proofBytes|SpendingProofBytes|true|none|Base16-encoded spending proofs|
|extension|object|true|none|Variables to be put into context|
|» additionalProperties|SValue|false|none|Base-16 encoded serialized Sigma-state value|

#### SerializedBox
=== "json"
```json
{
  "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "bytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|boxId|TransactionBoxId|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|bytes|HexString|true|none|Base16-encoded bytes|

#### ScriptBytes
=== "json"
```json
{
  "bytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|bytes|HexString|true|none|Base16-encoded bytes|

#### SnapshotsInfo
=== "json"
```json
{
  "availableManifests": [
    {}
  ]
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|availableManifests|[object]|true|none|Map of available manifests height -> manifestId|

#### ErgoTransactionOutput
=== "json"
```json
{
  "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "value": 147,
  "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
  "creationHeight": 9149,
  "assets": [
    {
      "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "amount": 1000
    }
  ],
  "additionalRegisters": {
    "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
  },
  "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "index": 0
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|boxId|TransactionBoxId|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|
|value|integer(int64)|true|none|Amount of Ergo token|
|ergoTree|ErgoTree|true|none|Base16-encoded ergo tree bytes|
|creationHeight|integer(int32)|true|none|Height the output was created at|
|assets|[Asset]|false|none|Assets list in the transaction|
|additionalRegisters|Registers|true|none|Ergo box registers|
|transactionId|TransactionId|false|none|Base16-encoded transaction id bytes|
|index|integer(int32)|false|none|Index in the transaction outputs|

#### WalletBox
=== "json"
```json
{
  "box": {
    "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "value": 147,
    "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
    "creationHeight": 9149,
    "assets": [
      {
        "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "amount": 1000
      }
    ],
    "additionalRegisters": {
      "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
    },
    "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "index": 0
  },
  "confirmationsNum": 147,
  "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
  "creationTransaction": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "spendingTransaction": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "spendingHeight": 147,
  "inclusionHeight": 147,
  "onchain": true,
  "spent": false,
  "creationOutIndex": 2,
  "scans": [
    1
  ]
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|box|ErgoTransactionOutput|true|none|none|
|confirmationsNum|integer(int32)¦null|true|none|Number of confirmations, if the box is included into the blockchain|
|address|ErgoAddress|true|none|Encoded Ergo Address|
|creationTransaction|ModifierId|true|none|Transaction which created the box|
|spendingTransaction|ModifierId|true|none|Transaction which created the box|
|spendingHeight|integer(int32)¦null|true|none|The height the box was spent at|
|inclusionHeight|integer(int32)|true|none|The height the transaction containing the box was included in a block at|
|onchain|boolean|true|none|A flag signalling whether the box is created on main chain|
|spent|boolean|true|none|A flag signalling whether the box was spent|
|creationOutIndex|integer(int32)|true|none|An index of a box in the creating transaction|
|scans|[integer]|true|none|Scan identifiers the box relates to|

#### BalanceInfo
=== "json"
```json
{
  "nanoErgs": 0,
  "tokens": [
    {
      "tokenId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "amount": 0,
      "decimals": 0,
      "name": "string"
    }
  ]
}
```
Balance information

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|nanoErgs|integer(int64)|true|none|Balance of nanoERGs|
|tokens|[object]|true|none|Balance of tokens|
|» tokenId|ModifierId|false|none|Identifier of the token|
|» amount|integer(int64)|false|none|Amount of the token|
|» decimals|integer|false|none|Number of decimals of the token|
|» name|string|false|none|Name of the token, if any|

#### IndexedErgoBox
=== "json"
```json
{
  "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "value": 147,
  "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
  "creationHeight": 9149,
  "assets": [
    {
      "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "amount": 1000
    }
  ],
  "additionalRegisters": {
    "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
  },
  "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "index": 0,
  "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
  "spentTransactionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "spendingHeight": 147,
  "inclusionHeight": 147,
  "globalIndex": 83927
}
```

##### Properties
allOf
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|ErgoTransactionOutput|false|none|none|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|object|false|none|Box indexed with extra information|
|» address|ErgoAddress|true|none|Encoded Ergo Address|
|» spentTransactionId|ModifierId|true|none|Transaction which spent the box|
|» spendingHeight|integer(int32)¦null|true|none|The height the box was spent at|
|» inclusionHeight|integer(int32)|true|none|The height the transaction containing the box was included in a block at|
|» globalIndex|integer(int64)|true|none|Global index of the output in the blockchain|

#### IndexedToken
=== "json"
```json
{
  "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "boxId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "emissionAmount": 3500000,
  "name": "string",
  "description": "string",
  "decimals": 8
}
```
Token indexed with extra information

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|ModifierId|true|none|Id of the token|
|boxId|ModifierId|true|none|Id of the box that created the token|
|emissionAmount|integer(int64)|true|none|The total supply of the token|
|name|string|true|none|The name of the token|
|description|string|true|none|The description of the token|
|decimals|integer(int32)|true|none|The number of decimals the token supports|

#### UnsignedErgoTransaction
=== "json"
```json
{
  "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "inputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "extension": {
        "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
      }
    }
  ],
  "dataInputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    }
  ],
  "outputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0
    }
  ]
}
```
Unsigned Ergo transaction

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|TransactionId|false|none|Base16-encoded transaction id bytes|
|inputs|[ErgoTransactionUnsignedInput]|true|none|Unsigned inputs of the transaction|
|dataInputs|[ErgoTransactionDataInput]|true|none|Data inputs of the transaction|
|outputs|[ErgoTransactionOutput]|true|none|Outputs of the transaction|

#### ErgoTransaction
=== "json"
```json
{
  "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "inputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "spendingProof": {
        "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "extension": {
          "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
        }
      }
    }
  ],
  "dataInputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    }
  ],
  "outputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0
    }
  ],
  "size": 0
}
```
ErgoTransaction is an atomic operation which changes UTXO state.

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|TransactionId|false|none|Id of the transaction|
|inputs|[ErgoTransactionInput]|true|none|Inputs, that will be spent by this transaction|
|dataInputs|[ErgoTransactionDataInput]|true|none|Read-only inputs, that are not going to be spent by transaction.|
|outputs|[ErgoTransactionOutput]|true|none|Outputs of the transaction, i.e. box candidates to be created by this transaction.|
|size|integer(int32)|false|none|Size of ErgoTransaction in bytes|

#### WalletTransaction
=== "json"
```json
{
  "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "inputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "spendingProof": {
        "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "extension": {
          "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
        }
      }
    }
  ],
  "dataInputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    }
  ],
  "outputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0
    }
  ],
  "inclusionHeight": 20998,
  "numConfirmations": 20998,
  "scans": [
    1
  ],
  "size": 0
}
```
Transaction augmented with some useful information

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|TransactionId|false|none|Base16-encoded transaction id bytes|
|inputs|[ErgoTransactionInput]|true|none|Transaction inputs|
|dataInputs|[ErgoTransactionDataInput]|true|none|Transaction data inputs|
|outputs|[ErgoTransactionOutput]|true|none|Transaction outputs|
|inclusionHeight|integer(int32)|true|none|Height of a block the transaction was included in|
|numConfirmations|integer(int32)|true|none|Number of transaction confirmations|
|scans|[integer]|true|none|Scan identifiers the transaction relates to|
|size|integer(int32)|false|none|Size in bytes|

#### IndexedErgoTransaction
=== "json"
```json
{
  "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "inputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "spendingProof": {
        "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "extension": {
          "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
        }
      }
    }
  ],
  "dataInputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    }
  ],
  "outputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0
    }
  ],
  "inclusionHeight": 20998,
  "numConfirmations": 20998,
  "blockId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "timestamp": 1524143059077,
  "index": 3,
  "globalIndex": 3565445,
  "size": 0
}
```
Transaction indexed with extra information

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|TransactionId|true|none|Base16-encoded transaction id bytes|
|inputs|[ErgoTransactionInput]|true|none|Transaction inputs|
|dataInputs|[ErgoTransactionDataInput]|true|none|Transaction data inputs|
|outputs|[ErgoTransactionOutput]|true|none|Transaction outputs|
|inclusionHeight|integer(int32)|true|none|Height of a block the transaction was included in|
|numConfirmations|integer(int32)|true|none|Number of transaction confirmations|
|blockId|ModifierId|true|none|Id of the block the transaction was included in|
|timestamp|Timestamp|true|none|Basic timestamp definition|
|index|integer(int32)|true|none|index of the transaction in the block it was included in|
|globalIndex|integer(int64)|true|none|Global index of the transaction in the blockchain|
|size|integer(int32)|true|none|Size in bytes|

#### ErgoAddress
=== "json"
```json
"3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
```
Encoded Ergo Address

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|string|false|none|Encoded Ergo Address|

#### RewardAddress
=== "json"
```json
{
  "rewardAddress": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|rewardAddress|ErgoAddress|true|none|Encoded Ergo Address|

#### RewardPubKey
=== "json"
```json
{
  "rewardPubkey": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3"
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|rewardPubkey|string|true|none|none|

#### DlogSecret
=== "json"
```json
"433080ff80d0d52d7f8bfffff47f00807f44f680000949b800007f7f7ff1017f"
```
Hex-encoded big-endian 256-bits secret exponent

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|string|false|none|Hex-encoded big-endian 256-bits secret exponent|

#### DhtSecret
=== "json"
```json
{
  "secret": "433080ff80d0d52d7f8bfffff47f00807f44f680000949b800007f7f7ff1017f",
  "g": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
  "h": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
  "u": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
  "v": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3"
}
```
Hex-encoded big-endian 256-bits secret exponent "w" along with generators "g", "h", and group elements "u", "v", such as g^w = u, h^w = v

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|secret|string|true|none|Hex-encoded big-endian 256-bits secret exponent|
|g|string|true|none|Hex-encoded "g" generator for the Diffie-Hellman tuple (secp256k1 curve point)|
|h|string|true|none|Hex-encoded "h" generator for the Diffie-Hellman tuple (secp256k1 curve point)|
|u|string|true|none|Hex-encoded "u" group element of the Diffie-Hellman tuple (secp256k1 curve point)|
|v|string|true|none|Hex-encoded "v" group element of the Diffie-Hellman tuple (secp256k1 curve point)|

#### TransactionSigningRequest
=== "json"
```json
{
  "tx": {
    "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "inputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "extension": {
          "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
        }
      }
    ],
    "dataInputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      }
    ],
    "outputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "value": 147,
        "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
        "creationHeight": 9149,
        "assets": [
          {
            "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 1000
          }
        ],
        "additionalRegisters": {
          "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
        },
        "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "index": 0
      }
    ]
  },
  "inputsRaw": [
    "string"
  ],
  "dataInputsRaw": [
    "string"
  ],
  "hints": {
    "secretHints": [
      {
        "01": [
          {
            "hint": "cmtWithSecret",
            "pubkey": {
              "op": -51,
              "h": "0327e65711a59378c59359c3e1d0f7abe906479eccb76094e50fe79d743ccc15e6"
            },
            "position": "0-1",
            "type": "dlog",
            "a": "02924d6274d1b9132fe028a0e3ac2fdbc503a1e52d1398932fa5f1bcf71909eb4b",
            "secret": "42a2a0ae6b98ee791ac9734252e8a7a08e691b92de085138e302f64a722a4300"
          }
        ]
      }
    ],
    "publicHints": [
      {
        "01": [
          {
            "hint": "cmtWithSecret",
            "pubkey": {
              "op":...

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tx|UnsignedErgoTransaction|true|none|Unsigned transaction to sign|
|inputsRaw|[string]|false|none|Optional list of inputs to be used in serialized form|
|dataInputsRaw|[string]|false|none|Optional list of inputs to be used in serialized form|
|hints|TransactionHintsBag|false|none|Optional list of hints used for signing|
|secrets|object|true|none|Secrets used for signing|
|» dlog|[DlogSecret]|false|none|Sequence of secret exponents (DLOG secrets)|
|» dht|[DhtSecret]|false|none|Sequence of secret Diffie-Hellman tuple exponents (DHT secrets)|

#### AddressHolder
=== "json"
```json
{
  "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
}
```
Holds encoded ErgoAddress

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address|ErgoAddress|true|none|Encoded Ergo Address|

#### BoxesRequestHolder
=== "json"
```json
{
  "targetAssets": [
    [
      "string",
      "string"
    ]
  ],
  "targetBalance": 0
}
```
Holds request for wallet boxes

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|targetAssets|[array]|true|none|Target assets|
anyOf
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» anonymous|string|false|none|TokenId|
or
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» anonymous|integer|false|none|Long|
continued
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|targetBalance|integer(int64)|true|none|Target balance|

#### RequestsHolder
=== "json"
```json
{
  "requests": [
    {
      "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
      "value": 1,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "registers": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      }
    }
  ],
  "fee": 1000000,
  "inputsRaw": [
    "string"
  ],
  "dataInputsRaw": [
    "string"
  ]
}
```
Holds many transaction requests and transaction fee

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|requests|[anyOf]|true|none|Sequence of transaction requests|
anyOf
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» anonymous|PaymentRequest|false|none|Request for generation of payment transaction to a given address|
or
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» anonymous|BurnTokensRequest|false|none|Request for burning tokens in wallet|
or
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» anonymous|AssetIssueRequest|false|none|Request for generation of asset issue transaction|
continued
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|fee|integer(int64)|false|none|Transaction fee|
|inputsRaw|[string]|false|none|List of inputs to be used in serialized form|
|dataInputsRaw|[string]|false|none|List of data inputs to be used in serialized form|

#### SourceHolder
=== "json"
```json
{
  "source": "string"
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|source|string|true|none|Sigma source to be compiled|

#### ErgoLikeTransaction
=== "json"
```json
{
  "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "inputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "spendingProof": {
        "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "extension": {
          "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
        }
      }
    }
  ],
  "dataInputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    }
  ],
  "outputs": [
    {
      "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "value": 147,
      "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
      "creationHeight": 9149,
      "assets": [
        {
          "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "amount": 1000
        }
      ],
      "additionalRegisters": {
        "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
      },
      "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "index": 0
    }
  ]
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|ModifierId|true|none|Base16-encoded 32 byte modifier id|
|inputs|[ErgoTransactionInput]|true|none|none|
|dataInputs|[ErgoTransactionDataInput]|true|none|none|
|outputs|[ErgoTransactionOutput]|true|none|none|

#### SigmaHeader
=== "json"
```json
{
  "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "timestamp": 1524143059077,
  "version": 2,
  "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "stateRoot": {
    "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "treeFlags": 0,
    "keyLength": 0,
    "valueLength": 0
  },
  "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "nBits": 19857408,
  "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "extensionRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "height": 667,
  "size": 667,
  "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "powSolutions": {
    "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
    "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
    "n": "0000000000000000",
    "d": 987654321
  },
  "votes": "000000",
  "minerPk": "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "powOnetimePk": "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
  "powNonce": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "powDistance": 123456789
}
```
Block header format used for sigma ErgoLikeContext

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|ModifierId|false|none|Base16-encoded 32 byte modifier id|
|timestamp|Timestamp|true|none|Basic timestamp definition|
|version|Version|true|none|Ergo blockchain protocol version|
|adProofsRoot|Digest32|true|none|Base16-encoded 32 byte digest|
|adProofsId|ModifierId|false|none|Base16-encoded 32 byte modifier id|
|stateRoot|AvlTreeData|true|none|none|
|transactionsRoot|Digest32|true|none|Base16-encoded 32 byte digest|
|transactionsId|ModifierId|false|none|Base16-encoded 32 byte modifier id|
|nBits|integer(int64)|true|none|none|
|extensionHash|Digest32|true|none|Base16-encoded 32 byte digest|
|extensionRoot|Digest32|false|none|Base16-encoded 32 byte digest|
|extensionId|ModifierId|false|none|Base16-encoded 32 byte modifier id|
|height|integer(int32)|true|none|none|
|size|integer(int32)|false|none|none|
|parentId|ModifierId|true|none|Base16-encoded 32 byte modifier id|
|powSolutions|PowSolutions|false|none|An object containing all components of pow solution|
|votes|Votes|true|none|Base16-encoded votes for a soft-fork and parameters|
|minerPk|string|false|none|none|
|powOnetimePk|string|false|none|none|
|powNonce|Digest32|false|none|Base16-encoded 32 byte digest|
|powDistance|number|false|none|sigma.BigInt|

#### PreHeader
=== "json"
```json
{
  "timestamp": 1524143059077,
  "version": 2,
  "nBits": 19857408,
  "height": 667,
  "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "votes": "000000",
  "minerPk": "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798"
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|timestamp|Timestamp|true|none|Basic timestamp definition|
|version|Version|true|none|Ergo blockchain protocol version|
|nBits|integer(int64)|true|none|none|
|height|integer(int32)|true|none|none|
|parentId|ModifierId|true|none|Base16-encoded 32 byte modifier id|
|votes|Votes|true|none|Base16-encoded votes for a soft-fork and parameters|
|minerPk|string|false|none|none|

#### AvlTreeData
=== "json"
```json
{
  "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "treeFlags": 0,
  "keyLength": 0,
  "valueLength": 0
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|digest|Digest32|true|none|Base16-encoded 32 byte digest|
|treeFlags|integer(int32)|false|none|none|
|keyLength|integer(int32)|false|none|none|
|valueLength|integer(int32)¦null|false|none|none|

#### ErgoLikeContext
=== "json"
```json
{
  "lastBlockUtxoRoot": {
    "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "treeFlags": 0,
    "keyLength": 0,
    "valueLength": 0
  },
  "headers": [
    {
      "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "timestamp": 1524143059077,
      "version": 2,
      "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "stateRoot": {
        "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "treeFlags": 0,
        "keyLength": 0,
        "valueLength": 0
      },
      "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "nBits": 19857408,
      "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "extensionRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "height": 667,
      "size": 667,
      "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "powSolutions": {
        "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
        "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
        "n": "0000000000000000",
        "d": 987654321
      },
      "votes": "000000",
      "minerPk": "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
      "powOnetimePk": "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
      "powNonce": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "powDistance": 123456789
    }
  ],
  "preHeader": {
    "timestamp": 1524143059077,
    "version": 2,
    "nBits": 19857408...

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lastBlockUtxoRoot|AvlTreeData|true|none|state root before current block application|
|headers|[SigmaHeader]|true|none|fixed number of last block headers in descending order (first header is the newest one)|
|preHeader|PreHeader|true|none|fields of block header with the current spendingTransaction, that can be predicted by a miner before its formation|
|dataBoxes|[ErgoTransactionOutput]|true|none|boxes, that corresponds to id's of spendingTransaction.dataInputs|
|boxesToSpend|[ErgoTransactionOutput]|true|none|boxes, that corresponds to id's of spendingTransaction.inputs|
|spendingTransaction|ErgoLikeTransaction|true|none|transaction that contains self box|
|selfIndex|integer(int64)|true|none|index of the box in boxesToSpend that contains the script we're evaluating|
|extension|object|true|none|prover-defined key-value pairs, that may be used inside a script|
|validationSettings|string|true|none|validation parameters passed to Interpreter.verify to detect soft-fork conditions|
|costLimit|integer(int64)|true|none|hard limit on accumulated execution cost, if exceeded lead to CostLimitException to be thrown|
|initCost|integer(int64)|true|none|initial value of execution cost already accumulated before Interpreter.verify is called|

#### ExecuteScript
=== "json"
```json
{
  "script": "string",
  "namedConstants": {},
  "context": {
    "lastBlockUtxoRoot": {
      "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "treeFlags": 0,
      "keyLength": 0,
      "valueLength": 0
    },
    "headers": [
      {
        "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "timestamp": 1524143059077,
        "version": 2,
        "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "stateRoot": {
          "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "treeFlags": 0,
          "keyLength": 0,
          "valueLength": 0
        },
        "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "nBits": 19857408,
        "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "extensionRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "height": 667,
        "size": 667,
        "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "powSolutions": {
          "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
          "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
          "n": "0000000000000000",
          "d": 987654321
        },
        "votes": "000000",
        "minerPk": "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
        "powOnetimePk": "0279be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798",
        "powNonce": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abad...

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|script|string|true|none|Sigma script to be executed|
|namedConstants|object¦null|true|none|Environment for compiler|
|context|ErgoLikeContext|true|none|Interpreter context|

#### SigmaBoolean
=== "json"
```json
{
  "op": 0,
  "h": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "g": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "u": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "v": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "condition": true
}
```
Algebraic data type of sigma proposition expressions

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|op|integer(int8)|true|none|Sigma opCode|
|h|HexString|false|none|Base16-encoded bytes|
|g|HexString|false|none|Base16-encoded bytes|
|u|HexString|false|none|Base16-encoded bytes|
|v|HexString|false|none|Base16-encoded bytes|
|condition|boolean|false|none|none|

#### SigmaBooleanAndPredicate
=== "json"
```json
{
  "args": [
    {
      "op": 0,
      "h": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "g": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "u": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "v": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "condition": true
    }
  ]
}
```

##### Properties
allOf
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|SigmaBoolean|false|none|Algebraic data type of sigma proposition expressions|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|object|false|none|none|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|object|false|none|none|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|object|false|none|none|
|» args|[SigmaBoolean]|false|none|[Algebraic data type of sigma proposition expressions]|

#### SigmaBooleanOrPredicate
=== "json"
```json
{
  "args": [
    {
      "op": 0,
      "h": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "g": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "u": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "v": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "condition": true
    }
  ]
}
```

##### Properties
allOf
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|SigmaBoolean|false|none|Algebraic data type of sigma proposition expressions|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|object|false|none|none|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|object|false|none|none|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|object|false|none|none|
|» args|[SigmaBoolean]|false|none|[Algebraic data type of sigma proposition expressions]|

#### SigmaBooleanThresholdPredicate
=== "json"
```json
{
  "args": [
    {
      "op": 0,
      "h": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "g": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "u": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "v": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "condition": true
    }
  ]
}
```

##### Properties
allOf
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|SigmaBoolean|false|none|Algebraic data type of sigma proposition expressions|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|object|false|none|none|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|object|false|none|none|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|object|false|none|none|
|» args|[SigmaBoolean]|false|none|[Algebraic data type of sigma proposition expressions]|

#### CryptoResult
=== "json"
```json
{
  "value": {
    "op": -45,
    "condition": true
  },
  "cost": 10
}
```
Result of executeWithContext request (reduceToCrypto)

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|value|SigmaBoolean|true|none|value of SigmaProp type which represents a statement verifiable via sigma protocol|
|cost|integer(int64)|true|none|Estimated cost of contract execution|

#### ScanningPredicate
=== "json"
```json
{
  "predicate": "string"
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|predicate|string|true|none|none|

#### ContainsPredicate
=== "json"
```json
{
  "predicate": "string",
  "register": "string",
  "bytes": "string"
}
```

##### Properties
allOf
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|ScanningPredicate|false|none|none|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|object|false|none|none|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|object|false|none|none|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|object|false|none|none|
|» register|string|false|none|none|
|» bytes|string|false|none|none|

#### EqualsPredicate
=== "json"
```json
{
  "predicate": "string",
  "register": "string",
  "bytes": "string"
}
```

##### Properties
allOf
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|ScanningPredicate|false|none|none|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|object|false|none|none|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|object|false|none|none|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|object|false|none|none|
|» register|string|false|none|none|
|» bytes|string|false|none|none|

#### ContainsAssetPredicate
=== "json"
```json
{
  "predicate": "string",
  "assetId": "string"
}
```

##### Properties
allOf
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|ScanningPredicate|false|none|none|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|object|false|none|none|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|object|false|none|none|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|object|false|none|none|
|» assetId|string|false|none|none|

#### AndPredicate
=== "json"
```json
{
  "predicate": "string",
  "args": [
    {
      "predicate": "string"
    }
  ]
}
```

##### Properties
allOf
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|ScanningPredicate|false|none|none|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|object|false|none|none|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|object|false|none|none|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|object|false|none|none|
|» args|[ScanningPredicate]|false|none|none|

#### OrPredicate
=== "json"
```json
{
  "predicate": "string",
  "args": [
    {
      "predicate": "string"
    }
  ]
}
```

##### Properties
allOf
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|ScanningPredicate|false|none|none|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|object|false|none|none|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|object|false|none|none|
and
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|object|false|none|none|
|» args|[ScanningPredicate]|false|none|none|

#### ScanRequest
=== "json"
```json
{
  "scanName": "Assets Tracker",
  "walletInteraction": "off",
  "removeOffchain": true,
  "trackingRule": {
    "predicate": "containsAsset",
    "assetId": "02dada811a888cd0dc7a0a41739a3ad9b0f427741fe6ca19700cf1a51200c96bf7"
  }
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|scanName|string|false|none|none|
|removeOffchain|boolean|false|none|none|
|walletInteraction|string|false|none|none|
|trackingRule|ScanningPredicate|false|none|none|

###### Enumerated Values
|Property|Value|
|---|---|
|walletInteraction|off|
|walletInteraction|shared|
|walletInteraction|forced|

#### Scan
=== "json"
```json
{
  "scanId": 2,
  "scanName": "Assets Tracker",
  "walletInteraction": "off",
  "removeOffchain": true,
  "trackingRule": {
    "predicate": "containsAsset",
    "assetId": "02dada811a888cd0dc7a0a41739a3ad9b0f427741fe6ca19700cf1a51200c96bf7"
  }
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|scanName|string|false|none|none|
|scanId|integer|false|none|none|
|walletInteraction|string|false|none|none|
|removeOffchain|boolean|false|none|none|
|trackingRule|ScanningPredicate|false|none|none|

###### Enumerated Values
|Property|Value|
|---|---|
|walletInteraction|off|
|walletInteraction|shared|
|walletInteraction|forced|

#### ScanId
=== "json"
```json
{
  "scanId": 0
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|scanId|integer|false|none|none|

#### ScanIdBoxId
=== "json"
```json
{
  "scanId": 0,
  "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|scanId|integer|true|none|none|
|boxId|TransactionBoxId|true|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|

#### ScanIdsBox
=== "json"
```json
{
  "scanIds": [
    0
  ],
  "box": {
    "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "value": 147,
    "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
    "creationHeight": 9149,
    "assets": [
      {
        "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "amount": 1000
      }
    ],
    "additionalRegisters": {
      "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
    },
    "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "index": 0
  }
}
```
Ergo box with associated scans (their respective identifiers)

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|scanIds|[integer]|true|none|none|
|box|ErgoTransactionOutput|true|none|none|

#### DlogCommitment
=== "json"
```json
{
  "r": "433080ff80d0d52d7f8bfffff47f00807f44f680000949b800007f7f7ff1017f",
  "a": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3"
}
```
Randomness and commitment for the first step of the Schnorr protocol

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|r|string|true|none|Hex-encoded big-endian 256-bits secret exponent|
|a|string|true|none|Hex-encoded "g" generator for the Diffie-Hellman tuple (secp256k1 curve point)|

#### HintExtractionRequest
=== "json"
```json
{
  "tx": {
    "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "inputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "spendingProof": {
          "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "extension": {
            "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
          }
        }
      }
    ],
    "dataInputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      }
    ],
    "outputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "value": 147,
        "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
        "creationHeight": 9149,
        "assets": [
          {
            "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 1000
          }
        ],
        "additionalRegisters": {
          "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
        },
        "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "index": 0
      }
    ],
    "size": 0
  },
  "real": [
    {
      "op": 0,
      "h": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "g": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "u": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "v": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "condition": true
    }
  ],
  "simulated": [
    {
      "op": 0,
      "h": "4ab9da11fc216660e974842cc3b770...

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tx|ErgoTransaction|true|none|Transaction to extract prover hints from|
|real|[SigmaBoolean]|true|none|Real signers of the transaction|
|simulated|[SigmaBoolean]|true|none|Simulated signers of the transaction|
|inputsRaw|[string]|false|none|Optional list of inputs to be used in serialized form|
|dataInputsRaw|[string]|false|none|Optional list of inputs to be used in serialized form|

#### Commitment
=== "json"
```json
{
  "hint": "cmtWithSecret",
  "pubkey": {
    "op": 0,
    "h": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "g": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "u": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "v": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "condition": true
  },
  "position": "string",
  "type": "dlog",
  "a": "string",
  "b": "string"
}
```
basic trait for prover commitments

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hint|string|true|none|none|
|pubkey|SigmaBoolean|true|none|Algebraic data type of sigma proposition expressions|
|position|string|true|none|none|
|type|string|false|none|none|
|a|string|true|none|a group element of the commitment|
|b|string|false|none|b group element of the commitment (needed for DHT protocol only)|

###### Enumerated Values
|Property|Value|
|---|---|
|hint|cmtWithSecret|
|hint|cmtReal|
|hint|cmtSimulated|
|type|dlog|
|type|dht|

#### CommitmentWithSecret
=== "json"
```json
{
  "hint": "cmtWithSecret",
  "pubkey": {
    "op": 0,
    "h": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "g": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "u": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "v": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "condition": true
  },
  "position": "string",
  "type": "dlog",
  "a": "string",
  "b": "string"
}
```
commitment to secret along with secret (!) randomness

##### Properties
None

#### SecretProven
=== "json"
```json
{
  "hint": "proofReal",
  "challenge": "string",
  "pubkey": {
    "op": 0,
    "h": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "g": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "u": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "v": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "condition": true
  },
  "proof": "string",
  "position": "string"
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|hint|string|true|none|none|
|challenge|string|true|none|none|
|pubkey|SigmaBoolean|true|none|Algebraic data type of sigma proposition expressions|
|proof|string|true|none|none|
|position|string|true|none|none|

###### Enumerated Values
|Property|Value|
|---|---|
|hint|proofReal|
|hint|proofSimulated|

#### InputHints
=== "json"
```json
{
  "01": [
    {
      "hint": "cmtWithSecret",
      "pubkey": {
        "op": -51,
        "h": "0327e65711a59378c59359c3e1d0f7abe906479eccb76094e50fe79d743ccc15e6"
      },
      "position": "0-1",
      "type": "dlog",
      "a": "02924d6274d1b9132fe028a0e3ac2fdbc503a1e52d1398932fa5f1bcf71909eb4b",
      "secret": "42a2a0ae6b98ee791ac9734252e8a7a08e691b92de085138e302f64a722a4300"
    }
  ]
}
```
hints for inputs, key is input index, values is a set of hints for the input

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|additionalProperties|[oneOf]|false|none|none|
oneOf
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» anonymous|CommitmentWithSecret|false|none|commitment to secret along with secret (!) randomness|
xor
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» anonymous|Commitment|false|none|basic trait for prover commitments|
xor
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» anonymous|SecretProven|false|none|none|

#### TransactionHintsBag
=== "json"
```json
{
  "secretHints": [
    {
      "01": [
        {
          "hint": "cmtWithSecret",
          "pubkey": {
            "op": -51,
            "h": "0327e65711a59378c59359c3e1d0f7abe906479eccb76094e50fe79d743ccc15e6"
          },
          "position": "0-1",
          "type": "dlog",
          "a": "02924d6274d1b9132fe028a0e3ac2fdbc503a1e52d1398932fa5f1bcf71909eb4b",
          "secret": "42a2a0ae6b98ee791ac9734252e8a7a08e691b92de085138e302f64a722a4300"
        }
      ]
    }
  ],
  "publicHints": [
    {
      "01": [
        {
          "hint": "cmtWithSecret",
          "pubkey": {
            "op": -51,
            "h": "0327e65711a59378c59359c3e1d0f7abe906479eccb76094e50fe79d743ccc15e6"
          },
          "position": "0-1",
          "type": "dlog",
          "a": "02924d6274d1b9132fe028a0e3ac2fdbc503a1e52d1398932fa5f1bcf71909eb4b",
          "secret": "42a2a0ae6b98ee791ac9734252e8a7a08e691b92de085138e302f64a722a4300"
        }
      ]
    }
  ]
}
```
prover hints extracted from a transaction

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|secretHints|[InputHints]|false|none|Hints which contain secrets, do not share them!|
|publicHints|[InputHints]|false|none|Hints which contain public data only, share them freely!|

#### GenerateCommitmentsRequest
=== "json"
```json
{
  "tx": {
    "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "inputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "extension": {
          "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
        }
      }
    ],
    "dataInputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      }
    ],
    "outputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "value": 147,
        "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
        "creationHeight": 9149,
        "assets": [
          {
            "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 1000
          }
        ],
        "additionalRegisters": {
          "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
        },
        "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "index": 0
      }
    ]
  },
  "secrets": {
    "dlog": [
      "433080ff80d0d52d7f8bfffff47f00807f44f680000949b800007f7f7ff1017f"
    ],
    "dht": [
      {
        "secret": "433080ff80d0d52d7f8bfffff47f00807f44f680000949b800007f7f7ff1017f",
        "g": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
        "h": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
        "u": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3",
        "v": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3"
      }
    ]
  },
  "inputsRaw": [
    "string"
  ],
  "dataInputsRaw": [
    "string"
  ]
}
```
request to generate commitments to sign a transaction

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tx|UnsignedErgoTransaction|true|none|Unsigned transaction to sign|
|secrets|object|false|none|Optionally, external secrets used for signing|
|» dlog|[DlogSecret]|false|none|Sequence of secret exponents (DLOG secrets)|
|» dht|[DhtSecret]|false|none|Sequence of secret Diffie-Hellman tuple exponents (DHT secrets)|
|inputsRaw|[string]|false|none|Optional list of inputs to be used in serialized form|
|dataInputsRaw|[string]|false|none|Optional list of inputs to be used in serialized form|

#### PaymentRequest
=== "json"
```json
{
  "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
  "value": 1,
  "assets": [
    {
      "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "amount": 1000
    }
  ],
  "registers": {
    "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
  }
}
```
Request for generation of payment transaction to a given address

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address|ErgoAddress|true|none|Encoded Ergo Address|
|value|integer(int64)|true|none|Payment amount|
|assets|[Asset]|false|none|Assets list in the transaction|
|registers|Registers|false|none|Ergo box registers|

#### BurnTokensRequest
=== "json"
```json
{
  "assetsToBurn": [
    {
      "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "amount": 1000
    }
  ]
}
```
Request for burning tokens in wallet

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|assetsToBurn|[Asset]|true|none|Assets list to burn in the transaction|

#### AssetIssueRequest
=== "json"
```json
{
  "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
  "ergValue": 0,
  "amount": 1000000,
  "name": "TST",
  "description": "Test token",
  "decimals": 8,
  "registers": {
    "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
  }
}
```
Request for generation of asset issue transaction

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address|ErgoAddress|false|none|Optional, first address in the wallet will be used if not defined|
|ergValue|integer(int64)|false|none|Optional, amount of ergs to be put into box with issued assets|
|amount|integer(int64)|true|none|Supply amount|
|name|string|true|none|Assets name|
|description|string|true|none|Assets description|
|decimals|integer(int32)|true|none|Number of decimal places|
|registers|Registers|false|none|Optional, possible values for registers R7...R9|

#### FullBlock
=== "json"
```json
{
  "header": {
    "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "timestamp": 1524143059077,
    "version": 2,
    "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "nBits": 19857408,
    "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "powSolutions": {
      "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
      "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
      "n": "0000000000000000",
      "d": 987654321
    },
    "height": 667,
    "difficulty": "9575989248",
    "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "votes": "000000",
    "size": 0,
    "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
  },
  "blockTransactions": {
    "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "transactions": [
      {
        "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "inputs": [
          {
            "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "spendingProof": {
              "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "extension": {
                "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
            ...

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|header|BlockHeader|true|none|Header of a block. It authenticates link to a previous block, other block sections (transactions, UTXO set transformation proofs, extension), UTXO set, votes for blockchain parameters to be changed and proof-of-work related data.|
|blockTransactions|BlockTransactions|true|none|Section of a block which contains transactions.|
|adProofs|BlockADProofs|true|none|none|
|extension|Extension|true|none|Section of a block which contains extension data.|
|size|integer(int32)|true|none|Size in bytes|

#### PowSolutions
=== "json"
```json
{
  "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
  "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
  "n": "0000000000000000",
  "d": 987654321
}
```
An object containing all components of pow solution

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pk|string|true|none|Base16-encoded public key|
|w|string|true|none|none|
|n|string|true|none|none|
|d|number|true|none|none|

#### BlockHeaderWithoutPow
=== "json"
```json
{
  "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "timestamp": 1524143059077,
  "version": 2,
  "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "nBits": 19857408,
  "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "height": 667,
  "difficulty": 62,
  "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "votes": "000000",
  "size": 0,
  "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|ModifierId|true|none|Base16-encoded 32 byte modifier id|
|timestamp|Timestamp|true|none|Basic timestamp definition|
|version|Version|true|none|Ergo blockchain protocol version|
|adProofsRoot|Digest32|true|none|Base16-encoded 32 byte digest|
|stateRoot|ADDigest|true|none|Base16-encoded 33 byte digest - digest with extra byte with tree height|
|transactionsRoot|Digest32|true|none|Base16-encoded 32 byte digest|
|nBits|integer(int64)|true|none|none|
|extensionHash|Digest32|true|none|Base16-encoded 32 byte digest|
|height|integer(int32)|true|none|none|
|difficulty|integer(int32)|true|none|none|
|parentId|ModifierId|true|none|Base16-encoded 32 byte modifier id|
|votes|Votes|true|none|Base16-encoded votes for a soft-fork and parameters|
|size|integer(int32)|false|none|Size in bytes|
|extensionId|ModifierId|false|none|Base16-encoded 32 byte modifier id|
|transactionsId|ModifierId|false|none|Base16-encoded 32 byte modifier id|
|adProofsId|ModifierId|false|none|Base16-encoded 32 byte modifier id|

#### PopowHeader
=== "json"
```json
{
  "header": {
    "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "timestamp": 1524143059077,
    "version": 2,
    "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "nBits": 19857408,
    "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "powSolutions": {
      "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
      "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
      "n": "0000000000000000",
      "d": 987654321
    },
    "height": 667,
    "difficulty": "9575989248",
    "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "votes": "000000",
    "size": 0,
    "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
  },
  "interlinks": [
    "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
  ]
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|header|BlockHeader|true|none|Header of a block. It authenticates link to a previous block, other block sections (transactions, UTXO set transformation proofs, extension), UTXO set, votes for blockchain parameters to be changed and proof-of-work related data.|
|interlinks|[ModifierId]|true|none|Array of header interlinks|

#### NipopowProof
=== "json"
```json
{
  "m": 0,
  "k": 0,
  "prefix": [
    {
      "header": {
        "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "timestamp": 1524143059077,
        "version": 2,
        "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "nBits": 19857408,
        "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "powSolutions": {
          "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
          "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
          "n": "0000000000000000",
          "d": 987654321
        },
        "height": 667,
        "difficulty": "9575989248",
        "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "votes": "000000",
        "size": 0,
        "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      },
      "interlinks": [
        "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      ]
    }
  ],
  "suffixHead": {
    "header": {
      "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "timestamp": 1524143059077,
      "version": 2,
      "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "nBits": 19857408,
      "extensionHash": "4ab9da11fc216660e974842cc3b7705e...

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|m|number|true|none|security parameter (min μ-level superchain length)|
|k|number|true|none|security parameter (min suffix length, >= 1)|
|prefix|[PopowHeader]|true|none|proof prefix headers|
|suffixHead|PopowHeader|true|none|none|
|suffixTail|[BlockHeader]|true|none|tail of the proof suffix headers|

#### BlockHeader
=== "json"
```json
{
  "id": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "timestamp": 1524143059077,
  "version": 2,
  "adProofsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "transactionsRoot": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "nBits": 19857408,
  "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "powSolutions": {
    "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
    "w": "0366ea253123dfdb8d6d9ca2cb9ea98629e8f34015b1e4ba942b1d88badfcc6a12",
    "n": "0000000000000000",
    "d": 987654321
  },
  "height": 667,
  "difficulty": "9575989248",
  "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "votes": "000000",
  "size": 0,
  "extensionId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "transactionsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "adProofsId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
}
```
Header of a block. It authenticates link to a previous block, other block sections (transactions, UTXO set transformation proofs, extension), UTXO set, votes for blockchain parameters to be changed and proof-of-work related data.

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|ModifierId|true|none|Block id|
|timestamp|Timestamp|true|none|Block generation time reported by a miner|
|version|Version|true|none|Protocol version used to generate the block|
|adProofsRoot|Digest32|true|none|Digest of UTXO set transformation proofs|
|stateRoot|ADDigest|true|none|AVL+ tree digest of UTXO set (after the block is applied)|
|transactionsRoot|Digest32|true|none|Merkle tree digest of transactions in the block (BlockTransactions section)|
|nBits|integer(int64)|true|none|Proof-of-work target (difficulty encoded)|
|extensionHash|Digest32|true|none|Merkle tree digest of the extension section of the block|
|powSolutions|PowSolutions|true|none|Solution for the proof-of-work puzzle|
|height|integer(int32)|true|none|Height of the block (genesis block height == 1)|
|difficulty|string|true|none|none|
|parentId|ModifierId|true|none|Base16-encoded 32 byte modifier id|
|votes|Votes|true|none|Votes for changing system parameters|
|size|integer(int32)|false|none|Size of the header in bytes|
|extensionId|ModifierId|false|none|Hash of the extension section of the block == hash(modifier type id, header id, extensionHash)|
|transactionsId|ModifierId|false|none|Hash of the transactions section of the block == hash(modifier type id, header id, transactionsRoot)|
|adProofsId|ModifierId|false|none|Hash of the UTXO set transformation proofs section of the block == hash(modifier type id, header id, adProofsRoot)|

#### BlockTransactions
=== "json"
```json
{
  "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "transactions": [
    {
      "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "inputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "spendingProof": {
            "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extension": {
              "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
            }
          }
        }
      ],
      "dataInputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        }
      ],
      "outputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
          },
          "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "index": 0
        }
      ],
      "size": 0
    }
  ],
  "size": 0
}
```
Section of a block which contains transactions.

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|headerId|ModifierId|true|none|Identifier of a header of a corresponding block|
|transactions|Transactions|true|none|Transactions of the block|
|size|integer(int32)|true|none|Size in bytes of all block transactions|

#### BlockADProofs
=== "json"
```json
{
  "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "proofBytes": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "size": 0
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|headerId|ModifierId|true|none|Identifier of a header of the block which contains the proofs|
|proofBytes|SerializedAdProof|true|none|Serialized bytes of the authenticated dictionary proof|
|digest|Digest32|true|none|Hash of the proofBytes|
|size|integer(int32)|true|none|Size in bytes|

#### Extension
=== "json"
```json
{
  "headerId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "digest": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "fields": [
    [
      "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
    ]
  ]
}
```
Section of a block which contains extension data.

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|headerId|ModifierId|true|none|Identifier of a header of a corresponding block|
|digest|Digest32|true|none|Root hash (aka digest) merkelized list of key-value records|
|fields|[KeyValueItem]¦null|true|none|List of key-value records|

#### KeyValueItem
=== "json"
```json
[
  "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
]
```
Key-value record represented as a pair of hex strings in an array.

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[HexString]|false|none|Key-value record represented as a pair of hex strings in an array.|

#### CandidateBlock
=== "json"
```json
{
  "version": 2,
  "extensionHash": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "timestamp": 1524143059077,
  "stateRoot": "333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "nBits": 19857408,
  "adProofBytes": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "parentId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "transactionsNumber": 2,
  "transactions": [
    {
      "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "inputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "spendingProof": {
            "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "extension": {
              "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
            }
          }
        }
      ],
      "dataInputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
        }
      ],
      "outputs": [
        {
          "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "value": 147,
          "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
          "creationHeight": 9149,
          "assets": [
            {
              "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
              "amount": 1000
            }
          ],
          "additionalRegisters": {
            "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39...

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|version|integer(int8)|false|none|none|
|extensionHash|Digest32|true|none|Base16-encoded 32 byte digest|
|timestamp|Timestamp|false|none|Basic timestamp definition|
|stateRoot|ADDigest|false|none|Base16-encoded 33 byte digest - digest with extra byte with tree height|
|nBits|integer(int64)|false|none|none|
|adProofBytes|SerializedAdProof|false|none|Base16-encoded ad proofs|
|parentId|ModifierId|true|none|Base16-encoded 32 byte modifier id|
|transactionsNumber|integer(int32)|false|none|none|
|transactions|Transactions|false|none|List of ErgoTransaction objects|
|votes|Votes|false|none|Base16-encoded votes for a soft-fork and parameters|

#### PassphraseMatch
=== "json"
```json
{
  "matched": true
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|matched|boolean|true|none|true if passphrase matches wallet, false otherwise|

#### WalletStatus
=== "json"
```json
{
  "isInitialized": true,
  "isUnlocked": true,
  "changeAddress": "3WzCFq7mkykKqi4Ykdk8BK814tkh6EsPmA42pQZxU2NRwSDgd6yB",
  "walletHeight": 0,
  "error": "string"
}
```
Status of the node wallet

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|isInitialized|boolean|true|none|true if wallet is initialized, false otherwise|
|isUnlocked|boolean|true|none|true if wallet is unlocked, false otherwise|
|changeAddress|string|true|none|address to send change to. Empty when wallet is not initialized or locked. By default change address correponds to root key address, could be set via /wallet/updateChangeAddress method.|
|walletHeight|integer|true|none|last scanned height for the wallet (and external scans)|
|error|string|true|none|last wallet error caught|

#### InitWallet
=== "json"
```json
{
  "pass": "string",
  "mnemonicPass": "string"
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pass|string|true|none|Password to encrypt wallet file with|
|mnemonicPass|string|false|none|Optional pass to password-protect mnemonic seed|

#### InitWalletResult
=== "json"
```json
{
  "mnemonic": "string"
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|mnemonic|string|true|none|Mnemonic seed phrase|

#### RestoreWallet
=== "json"
```json
{
  "pass": "string",
  "mnemonic": "string",
  "mnemonicPass": "string",
  "usePre1627KeyDerivation": true
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pass|string|true|none|Password to encrypt wallet file with|
|mnemonic|string|true|none|Mnemonic seed|
|mnemonicPass|string|false|none|Optional pass to password-protect mnemonic seed|
|usePre1627KeyDerivation|boolean|true|none|use incorrect(previous) BIP32 key derivation (see https://github.com/ergoplatform/ergo/issues/1627 for details). It's recommended to set to 'true' if the original wallet was created by ergo node before v4.0.105.|

#### CheckWallet
=== "json"
```json
{
  "mnemonic": "string",
  "mnemonicPass": "string"
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|mnemonic|string|true|none|Mnemonic seed (optional)|
|mnemonicPass|string|false|none|Optional pass to password-protect mnemonic seed|

#### UnlockWallet
=== "json"
```json
{
  "pass": "string"
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pass|string|true|none|Password to decrypt wallet file with|

#### DeriveKey
=== "json"
```json
{
  "derivationPath": "m/1/2"
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|derivationPath|string|true|none|Derivation path for a new secret to derive|

#### DeriveKeyResult
=== "json"
```json
{
  "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address|ErgoAddress|true|none|Encoded Ergo Address|

#### DeriveNextKeyResult
=== "json"
```json
{
  "derivationPath": "m/1/2",
  "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt"
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|derivationPath|string|true|none|Derivation path of the resulted secret|
|address|ErgoAddress|true|none|Encoded Ergo Address|

#### MerkleProof
=== "json"
```json
{
  "leaf": "cd665e49c834b0c25574fcb19a158d836f3f2aad8e91ac195f972534c25449b3",
  "levels": [
    [
      "018b7ae20a4acd23e3f1bf38671ce97103ad96d8f1c780b5e5e865e4873ae16337",
      0
    ]
  ]
}
```
Merkle proof for a leaf, which is an array of bytes (e.g. a transaction identifier)

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|leaf|string|true|none|Base16-encoded Merkle tree leaf bytes|
|levels|[array]|true|none|none|
anyOf
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» anonymous|string|false|none|hash|
or
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» anonymous|integer|false|none|side of hash|

#### ProofOfUpcomingTransactions
=== "json"
```json
{
  "msgPreimage": "0112e03c6d39d32509855be7cee9b62ff921f7a0cf6883e232474bd5b54d816dd056f846980d34c3b23098bdcf41222f8cdee5219224aa67750055926c3a2310a483accc4f9153e7a760615ea972ac67911cff111f8c17f563d6147205f58f85133ae695d1d4157e4aecdbbb29952cfa42b75129db55bddfce3bc53b8fd5b5465f10d8be8ddda62ed3b86afb0497ff2d381ed884bdae5287d20667def224a28d2b6e3ebfc78709780702c70bd8df0e000000",
  "txProofs": [
    {
      "leaf": "cd665e49c834b0c25574fcb19a158d836f3f2aad8e91ac195f972534c25449b3",
      "levels": [
        [
          "018b7ae20a4acd23e3f1bf38671ce97103ad96d8f1c780b5e5e865e4873ae16337",
          0
        ]
      ]
    }
  ]
}
```
Proof that a block corresponding to given header without PoW contains some transactions

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|msgPreimage|string|true|none|Base16-encoded serialized header without Proof-of-Work|
|txProofs|[MerkleProof]|true|none|Merkle proofs of transactions included into blocks (not necessarily all the block transactions)|

#### WorkMessage
=== "json"
```json
{
  "msg": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
  "b": 987654321,
  "pk": "0350e25cee8562697d55275c96bb01b34228f9bd68fd9933f2a25ff195526864f5",
  "proof": {
    "msgPreimage": "0112e03c6d39d32509855be7cee9b62ff921f7a0cf6883e232474bd5b54d816dd056f846980d34c3b23098bdcf41222f8cdee5219224aa67750055926c3a2310a483accc4f9153e7a760615ea972ac67911cff111f8c17f563d6147205f58f85133ae695d1d4157e4aecdbbb29952cfa42b75129db55bddfce3bc53b8fd5b5465f10d8be8ddda62ed3b86afb0497ff2d381ed884bdae5287d20667def224a28d2b6e3ebfc78709780702c70bd8df0e000000",
    "txProofs": [
      {
        "leaf": "cd665e49c834b0c25574fcb19a158d836f3f2aad8e91ac195f972534c25449b3",
        "levels": [
          [
            "018b7ae20a4acd23e3f1bf38671ce97103ad96d8f1c780b5e5e865e4873ae16337",
            0
          ]
        ]
      }
    ]
  }
}
```
Block candidate related data for external miner to perform work

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|msg|string|true|none|Base16-encoded block header bytes without PoW solution|
|b|integer|true|none|Work target value|
|pk|string|true|none|Base16-encoded miner public key|
|proof|ProofOfUpcomingTransactions|false|none|Proof that a block corresponding to given header without PoW contains some transactions|

#### Peer
=== "json"
```json
{
  "address": "127.0.0.1:5673",
  "restApiUrl": "https://example.com",
  "name": "mynode",
  "lastSeen": 1524143059077,
  "connectionType": "Incoming"
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address|string|true|none|none|
|restApiUrl|string¦null|false|none|none|
|name|string¦null|false|none|none|
|lastSeen|Timestamp|false|none|Basic timestamp definition|
|connectionType|string¦null|false|none|none|

###### Enumerated Values
|Property|Value|
|---|---|
|connectionType|Incoming|
|connectionType|Outgoing|

#### PeersStatus
=== "json"
```json
{
  "lastIncomingMessage": 1524143059077,
  "currentNetworkTime": 1524143059077
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|lastIncomingMessage|Timestamp|true|none|Basic timestamp definition|
|currentNetworkTime|Timestamp|true|none|Basic timestamp definition|

#### PeerMode
=== "json"
```json
{
  "state": "utxo",
  "verifyingTransactions": true,
  "fullBlocksSuffix": 2880
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|state|string|true|none|none|
|verifyingTransactions|boolean|true|none|none|
|fullBlocksSuffix|integer|true|none|none|

#### SyncInfo
=== "json"
```json
{
  "address": "127.0.0.1:5673",
  "mode": {
    "state": "utxo",
    "verifyingTransactions": true,
    "fullBlocksSuffix": 2880
  },
  "version": "4.0.16",
  "status": "Older",
  "height": 65780
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address|string|true|none|none|
|mode|PeerMode|true|none|Peer operating mode parameters|
|version|string|true|none|none|
|status|string|true|none|none|
|height|integer|true|none|none|

#### RequestedInfo
=== "json"
```json
{
  "address": "127.0.0.1:5673",
  "version": "4.0.26",
  "checks": 4
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address|string|false|none|none|
|version|string|false|none|none|
|checks|integer|true|none|How many times we checked for modifier delivery status|

#### RequestedInfoByModifierId
=== "json"
```json
{
  "property1": {
    "address": "127.0.0.1:5673",
    "version": "4.0.26",
    "checks": 4
  },
  "property2": {
    "address": "127.0.0.1:5673",
    "version": "4.0.26",
    "checks": 4
  }
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|additionalProperties|RequestedInfo|false|none|none|

#### ConnectedPeer
=== "json"
```json
{
  "address": "127.0.0.1:5673",
  "version": "4.0.26",
  "lastMessage": 1524143059077
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address|string|true|none|none|
|version|string|false|none|none|
|lastMessage|Timestamp|false|none|Basic timestamp definition|

#### ConnectedPeerByModifierId
=== "json"
```json
{
  "property1": {
    "address": "127.0.0.1:5673",
    "version": "4.0.26",
    "lastMessage": 1524143059077
  },
  "property2": {
    "address": "127.0.0.1:5673",
    "version": "4.0.26",
    "lastMessage": 1524143059077
  }
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|additionalProperties|ConnectedPeer|false|none|none|

#### TrackInfo
=== "json"
```json
{
  "invalidModifierApproxSize": 65780,
  "requested": {
    "property1": {
      "property1": {
        "address": "127.0.0.1:5673",
        "version": "4.0.26",
        "checks": 4
      },
      "property2": {
        "address": "127.0.0.1:5673",
        "version": "4.0.26",
        "checks": 4
      }
    },
    "property2": {
      "property1": {
        "address": "127.0.0.1:5673",
        "version": "4.0.26",
        "checks": 4
      },
      "property2": {
        "address": "127.0.0.1:5673",
        "version": "4.0.26",
        "checks": 4
      }
    }
  },
  "received": {
    "property1": {
      "property1": {
        "address": "127.0.0.1:5673",
        "version": "4.0.26",
        "lastMessage": 1524143059077
      },
      "property2": {
        "address": "127.0.0.1:5673",
        "version": "4.0.26",
        "lastMessage": 1524143059077
      }
    },
    "property2": {
      "property1": {
        "address": "127.0.0.1:5673",
        "version": "4.0.26",
        "lastMessage": 1524143059077
      },
      "property2": {
        "address": "127.0.0.1:5673",
        "version": "4.0.26",
        "lastMessage": 1524143059077
      }
    }
  }
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|invalidModifierApproxSize|integer|true|none|none|
|requested|object|true|none|Currently requested modifiers|
|» additionalProperties|RequestedInfoByModifierId|false|none|none|
|received|object|true|none|Received modifiers|
|» additionalProperties|ConnectedPeerByModifierId|false|none|none|

#### BlacklistedPeers
=== "json"
```json
{
  "addresses": [
    "string"
  ]
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|addresses|[string]|true|none|none|

#### NodeInfo
=== "json"
```json
{
  "name": "my-node-1",
  "appVersion": "0.0.1",
  "fullHeight": 667,
  "headersHeight": 667,
  "maxPeerHeight": 706162,
  "bestFullHeaderId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "previousFullHeaderId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "bestHeaderId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "stateRoot": "dab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "stateType": "digest",
  "stateVersion": "fab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "isMining": true,
  "peersCount": 327,
  "unconfirmedCount": 327,
  "difficulty": 667,
  "currentTime": 1524143059077,
  "launchTime": 1524143059077,
  "headersScore": 0,
  "fullBlocksScore": 0,
  "genesisBlockId": "3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "parameters": {
    "height": 667,
    "storageFeeFactor": 100000,
    "minValuePerByte": 360,
    "maxBlockSize": 1048576,
    "maxBlockCost": 104876,
    "blockVersion": 2,
    "tokenAccessCost": 100,
    "inputCost": 100,
    "dataInputCost": 100,
    "outputCost": 100
  },
  "eip27Supported": true,
  "restApiUrl": "https://example.com"
}
```
Data container for /info API request output. Contains information about node's state and configuration. Contains data about best block, best header, state, etc. Best block is the block with the maximum height.

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|Node's (peer) self-chosen name from config|
|appVersion|string|true|none|Node's application version|
|fullHeight|integer(int32)¦null|true|none|Height of the best block known to the node. Can be 'null' if state is empty (no full block is applied since node launch)|
|headersHeight|integer(int32)¦null|true|none|The height of the best header (i.e. the one with the maximum height). Can be 'null' if state is empty (no header applied since node launch)|
|maxPeerHeight|integer(int32)¦null|true|none|Maximum block height of connected peers. Can be 'null' if state is empty (no peer connected since node launch)|
|bestFullHeaderId|ModifierId¦null|true|none|Best full-block id (header id of such block). Can be 'null' if no full block is applied since node launch.|
|previousFullHeaderId|ModifierId¦null|true|none|Header id of the parent block of the best full-block (i.e. previous block in the blockchain). Can be 'null' if no full block is applied since node launch|
|bestHeaderId|ModifierId¦null|true|none|Best header ID (hex representation). Can be 'null' if no header applied since node launch.|
|stateRoot|string¦null|true|none|Current UTXO set digest. Can be 'null' if state is empty (no full block is applied since node launch)|
|stateType|string|true|none|Whether the node is storing UTXO set or only its digest. Equals digest if only digest is stored, utxo if full UTXO set is stored.|
|stateVersion|string¦null|true|none|Id of a block where UTXO set digest is taken from. Can be 'null' if no full block is applied since node launch.|
|isMining|boolean|true|none|Whether the node is mining (i.e. generating blocks).|
|peersCount|integer(int32)|true|none|Number of peers this node is connected with.|
|unconfirmedCount|integer(int32)|true|none|Number of unconfirmed transactions in the mempool.|
|difficulty|integer¦null|true|none|Difficulty on current bestFullHeaderId. Can be 'null' if no full block is a...

###### Enumerated Values
|Property|Value|
|---|---|
|stateType|digest|
|stateType|utxo|

#### Parameters
=== "json"
```json
{
  "height": 667,
  "storageFeeFactor": 100000,
  "minValuePerByte": 360,
  "maxBlockSize": 1048576,
  "maxBlockCost": 104876,
  "blockVersion": 2,
  "tokenAccessCost": 100,
  "inputCost": 100,
  "dataInputCost": 100,
  "outputCost": 100
}
```
System parameters which could be readjusted via collective miners decision.

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|height|integer(int32)|true|none|Height when current parameters were considered(not actual height). Can be '0' if state is empty|
|storageFeeFactor|integer(int32)|true|none|Storage fee coefficient (per byte per storage period ~4 years)|
|minValuePerByte|integer(int32)|true|none|Minimum value per byte of an output|
|maxBlockSize|integer(int32)|true|none|Maximum block size (in bytes)|
|maxBlockCost|integer(int32)|true|none|Maximum cumulative computational cost of input scripts in block transactions|
|blockVersion|Version|true|none|Ergo blockchain protocol version|
|tokenAccessCost|integer(int32)|true|none|Validation cost of a single token|
|inputCost|integer(int32)|true|none|Validation cost per one transaction input|
|dataInputCost|integer(int32)|true|none|Validation cost per one data input|
|outputCost|integer(int32)|true|none|Validation cost per one transaction output|

#### Version
=== "json"
```json
2
```
Ergo blockchain protocol version

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|integer(int8)|false|none|Ergo blockchain protocol version|

#### TransactionBoxId
=== "json"
```json
"1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
```
Base16-encoded transaction box id bytes. Should be 32 bytes long

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|string(base16)|false|none|Base16-encoded transaction box id bytes. Should be 32 bytes long|

#### TransactionId
=== "json"
```json
"2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
```
Base16-encoded transaction id bytes

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|string(base16)|false|none|Base16-encoded transaction id bytes|

#### ErgoTree
=== "json"
```json
"0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041"
```
Base16-encoded ergo tree bytes

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|string(base16)|false|none|Base16-encoded ergo tree bytes|

#### ErgoTreeObject
=== "json"
```json
{
  "tree": "02a7955281885bf0f0ca4a48678848cad8dc5b328ce8bc1d4481d041c98e891ff3"
}
```

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tree|string|false|none|serialized Ergo tree|

#### Transactions
=== "json"
```json
[
  {
    "id": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
    "inputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "spendingProof": {
          "proofBytes": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
          "extension": {
            "1": "a2aed72ff1b139f35d1ad2938cb44c9848a34d4dcfd6d8ab717ebde40a7304f2541cf628ffc8b5c496e6161eba3f169c6dd440704b1719e0"
          }
        }
      }
    ],
    "dataInputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
      }
    ],
    "outputs": [
      {
        "boxId": "1ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "value": 147,
        "ergoTree": "0008cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041",
        "creationHeight": 9149,
        "assets": [
          {
            "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
            "amount": 1000
          }
        ],
        "additionalRegisters": {
          "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
        },
        "transactionId": "2ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
        "index": 0
      }
    ],
    "size": 0
  }
]
```
List of ErgoTransaction objects

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[ErgoTransaction]|false|none|List of ErgoTransaction objects|

#### FeeHistogramBin
=== "json"
```json
{
  "nTxns": 0,
  "totalFee": 0
}
```
Fee histogram bin

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|nTxns|integer(int32)|false|none|none|
|totalFee|integer(int64)|false|none|none|

#### FeeHistogram
=== "json"
```json
[
  {
    "nTxns": 0,
    "totalFee": 0
  }
]
```
Fee histogram for transactions in mempool

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|[FeeHistogramBin]|false|none|Fee histogram for transactions in mempool|

#### Asset
=== "json"
```json
{
  "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
  "amount": 1000
}
```
Token detail in the transaction

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tokenId|Digest32|true|none|Base16-encoded 32 byte digest|
|amount|integer(int64)|true|none|Amount of the token|

#### Registers
=== "json"
```json
{
  "R4": "100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
}
```
Ergo box registers

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|additionalProperties|SValue|false|none|Base-16 encoded serialized Sigma-state value|

#### SValue
=== "json"
```json
"100204a00b08cd0336100ef59ced80ba5f89c4178ebd57b6c1dd0f3d135ee1db9f62fc634d637041ea02d192a39a8cc7a70173007301"
```
Base-16 encoded serialized Sigma-state value

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|string(base16)|false|none|Base-16 encoded serialized Sigma-state value|

#### Votes
=== "json"
```json
"000000"
```
Base16-encoded votes for a soft-fork and parameters

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|string(base16)|false|none|Base16-encoded votes for a soft-fork and parameters|

#### ModifierId
=== "json"
```json
"3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
```
Base16-encoded 32 byte modifier id

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|string(base16)|false|none|Base16-encoded 32 byte modifier id|

#### Digest32
=== "json"
```json
"4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
```
Base16-encoded 32 byte digest

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|string(base16)|false|none|Base16-encoded 32 byte digest|

#### HexString
=== "json"
```json
"4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
```
Base16-encoded bytes

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|string(base16)|false|none|Base16-encoded bytes|

#### ADDigest
=== "json"
```json
"333ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
```
Base16-encoded 33 byte digest - digest with extra byte with tree height

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|string(base16)|false|none|Base16-encoded 33 byte digest - digest with extra byte with tree height|

#### SerializedAdProof
=== "json"
```json
"3ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
```
Base16-encoded ad proofs

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|string(base16)|false|none|Base16-encoded ad proofs|

#### SpendingProofBytes
=== "json"
```json
"4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd1173ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
```
Base16-encoded spending proofs

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|string(base16)|false|none|Base16-encoded spending proofs|

#### BlockSignature
=== "json"
```json
"5ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117"
```
Base16-encoded block signature

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|string(base16)|false|none|Base16-encoded block signature|

#### Timestamp
=== "json"
```json
1524143059077
```
Basic timestamp definition

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|anonymous|integer(int64)|false|none|Basic timestamp definition|

#### EmissionInfo
=== "json"
```json
{
  "minerReward": 0,
  "totalCoinsIssued": 0,
  "totalRemainCoins": 0,
  "reemitted": 0
}
```
Emission info for height

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|minerReward|integer(int64)|false|none|none|
|totalCoinsIssued|integer(int64)|false|none|none|
|totalRemainCoins|integer(int64)|false|none|none|
|reemitted|integer(int64)|false|none|none|

#### EmissionScripts
=== "json"
```json
{
  "emission": "string",
  "reemission": "string",
  "pay2Reemission": "string"
}
```
Emission related scripts

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|emission|string|false|none|none|
|reemission|string|false|none|none|
|pay2Reemission|string|false|none|none|

#### BalancesSnapshot
=== "json"
```json
{
  "height": 0,
  "balance": 0,
  "assets": [
    {
      "tokenId": "4ab9da11fc216660e974842cc3b7705e62ebb9e0bf5ff78e53f9cd40abadd117",
      "amount": 1000
    }
  ]
}
```
Amount of Ergo tokens and assets

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|height|integer(int32)|true|none|none|
|balance|integer(int64)|true|none|none|
|assets|[Asset]|false|none|[Token detail in the transaction]|

#### AddressValidity
=== "json"
```json
{
  "address": "3WwbzW6u8hKWBcL1W7kNVMr25s2UHfSBnYtwSHvrRQt7DdPuoXrt",
  "isValid": true,
  "error": "string"
}
```
Validity status of Ergo address

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|address|ErgoAddress|true|none|Encoded Ergo Address|
|isValid|boolean|true|none|none|
|error|string|false|none|none|

#### ApiError
=== "json"
```json
{
  "error": 500,
  "reason": "Internal server error",
  "detail": "string"
}
```
Error response from API

##### Properties
|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|error|integer|true|none|Error code|
|reason|string|true|none|Error message explaining the reason of the error|
|detail|string¦null|true|none|Detailed error description|
