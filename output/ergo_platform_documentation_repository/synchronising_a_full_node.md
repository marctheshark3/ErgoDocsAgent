# Synchronising a full node
Source: docs/node/testnet/testnet-full.md
Generated: 2025-05-11

## Summary
# Synchronising a full node

To join the testnet, download [latest Ergo protocol reference client](https://github.com/ergoplatform/ergo/releases) and launch using

```bash
java -jar -Xmx4G ergo-*.jar --testnet -c testnet.conf
```


A minimal `testnet.conf` would be:

```conf
ergo {
  networkType = "testnet"
}
scorex {
 restApi {
    # Hex-encoded Blake2b256 hash of an API key. Should be 64-chars long Base16 string.

## Keywords
node, testnet, download, ergo, protocol, reference, ergoplatform, release, java, ergo-*.jar, networktype, scorex, restapi, blake2b256, hash, char, long, base16, string, quote

## Content
## Synchronising a full node
To join the testnet, download latest Ergo protocol reference client and launch using
bash
java -jar -Xmx4G ergo-*.jar --testnet -c testnet.conf
A minimal testnet.conf would be:
conf
ergo {
  networkType = "testnet"
}
scorex {
 restApi {
    # Hex-encoded Blake2b256 hash of an API key. Should be 64-chars long Base16 string.
    # Below is hash corresponding to API_KEY = "hello" (with no quotes)
    apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf"
  }
}
The node will be available at localhost:9052/panel
Once the node is synchronised, a user interface for Swagger is available at localhost:9052/swagger.
/// details | Mining
    {type: info, open: true}
If you want to help mine the testnet, you can do so by following the steps outlined on CPU Mining.
///
