# Perpetual Tokens - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/tokens/perpetual/](https://docs.ergoplatform.com/dev/tokens/perpetual/)
Generated: 2025-05-11

## Summary
ErgoScript allows the creation of a 'perpetual token', a token that is designed to exist indefinitely, unless it is removed by garbage collection. {
      val isPerpetual = {(b: Box) =>
        b.propositionBytes == SELF.propositionBytes && b.tokens == SELF.tokens
      }

      sigmaProp(OUTPUTS.exists(isPerpetual))
    }

This code snippet ensures the persistence of a collection of perpetual tokens, even if the collection's size is zero. If you protect a single token using this script, it guarantees that the token will only be removed by garbage collection. For a comprehensive discussion, refer to this thread. Multi-stage protocols are beneficial in situations where multiple scripts need to interact.

## Keywords
ergoscript, creation, token, garbage, collection, b.propositionbytes, self.propositionbytes, b.tokens, self.token, sigmaprop(outputs.exists(isperpetual, code, snippet, persistence, size, script, discussion, thread, stage, protocol, situation

## Content
## Perpetual Tokens#
ErgoScript allows the creation of a 'perpetual token', a token that is designed to exist indefinitely, unless it is removed by garbage collection.
{
      val isPerpetual = {(b: Box) =>
        b.propositionBytes == SELF.propositionBytes && b.tokens == SELF.tokens
      }

      sigmaProp(OUTPUTS.exists(isPerpetual))
    }

This code snippet ensures the persistence of a collection of perpetual tokens, even if the collection's size is zero. If you protect a single token using this script, it guarantees that the token will only be removed by garbage collection.
For a comprehensive discussion, refer to this thread.

### Multi-Stage Protocols#
Multi-stage protocols are beneficial in situations where multiple scripts need to interact. In these protocols, a script can reference the script of a subsequent stage.
For instance, consider the following example:
In script1, we have the statement:
hash(OUTPUTS(0).propositionBytes) == script2Hash
Here, script1 verifies if the hash of the first output's propositionBytes matches the hash of script2.
But, if we want script2 to refer back to script1, as shown below:
hash(OUTPUTS(0).propositionBytes) == script1Hash
We face a cyclic reference problem, as both scripts are referencing each other.
To overcome this, we can store script1Hash in a register of the box that contains script2. We also need to modify script1 to ensure that the corresponding register of any box containing script2 equals hash(SELF.propositionBytes).
While the "vanilla" perpetual token is intriguing, the "max-once-per-block-use" perpetual token offers more flexibility and power, and should be considered as a distinct design pattern.
