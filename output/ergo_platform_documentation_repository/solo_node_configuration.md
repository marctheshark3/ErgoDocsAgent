# Solo Node Configuration
Source: docs/mining/setup/solo-node.md
Generated: 2025-05-11

## Summary
# Solo Node Configuration



To be able to spend any ERG mined this way, you will need to include the [EIP27 rules](eip27.md) in your `ergo.conf` file which you run with the `.jar` as such


## Run

```bash
java -Xmx4g -jar ergo-5.0.4.jar --mainnet -c ergo.conf
```

## ergo.conf

```bash
	ergo {
	  node {
	    mining = true
	  }
    chain {
      reemission {
        checkReemissionRules = true
      }
    }
    wallet {
      checkEIP27 = true
    }
	}
	
	scorex {
	 restApi {
	    ## Hex-encoded Blake2b256 hash of an API key. ## Should be 64-chars long Base16 string. ## below is the hash of the string 'hello'
	    ## replace with your actual hash generated from within swagger. apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf"
	  }
	}
```

You'll then either want to use the [Ergo Stratum](stratum.md) mining server or [Mining Core](miningcore.md). ## Resources

- [Ergo Node + Stratum Server mining tutorial](https://www.youtube.com/watch?v=_1M8dGpfKjU)
-

## Keywords
solo, node, configuration, eip27, rules](eip27.md, file, .jar, bash, java, -jar, ergo-5.0.4.jar, ergo.conf, ergo, mining, chain, reemission, checkreemissionrule, wallet, checkeip27, scorex

## Content
## Solo Node Configuration
To be able to spend any ERG mined this way, you will need to include the EIP27 rules in your ergo.conf file which you run with the .jar as such

### Run
bash
java -Xmx4g -jar ergo-5.0.4.jar --mainnet -c ergo.conf

### ergo.conf
```bash
    ergo {
      node {
        mining = true
      }
    chain {
      reemission {
        checkReemissionRules = true
      }
    }
    wallet {
      checkEIP27 = true
    }
    }
scorex {
 restApi {
    ## Hex-encoded Blake2b256 hash of an API key. 
    ## Should be 64-chars long Base16 string.
    ## below is the hash of the string 'hello'
    ## replace with your actual hash generated from within swagger. 
    apiKeyHash = "324dcf027dd4a30a932c441f365a25e86b173defa4b8e58948253471b81b72cf"
  }
}
```
You'll then either want to use the Ergo Stratum mining server or Mining Core.

### Resources
Ergo Node + Stratum Server mining tutorial
Youtube: Mine Ergo from your own Node
ErgoForum: Q&A on mining (for pool operators and solo miner)
