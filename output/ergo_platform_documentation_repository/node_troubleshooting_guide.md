# Node Troubleshooting Guide
Source: docs/node/install/troubleshooting.md
Generated: 2025-05-11

## Summary
#  Node Troubleshooting Guide

This document aims to help you troubleshoot common issues with the Ergo reference client. If you encounter a problem not covered here, please create a [new issue on GitHub](https://github.com/ergoplatform/ergo/issues/new/choose) and provide the following details:

- Node version
- Java command used
- RAM/CPU specification
- Operating System
- JVM version
- Storage location (Cloud, SSD, etc)
- output of ERROR/WARN

You can obtain the output of ERROR/WARN by executing the following command:

```bash
tail -Fn+0 ergo.log | grep 'ERROR\|WARN' > output.log
```

## Searching the Logs The following commands can help you search your logs for specific entries:

```bash
tail -Fn+0 ergo.log | grep 'ERROR\|WARN'
tail -Fn+0 ergo.log | grep 'ERROR'
tail -Fn+0 ergo.log | grep "not modified"
tail -Fn+0 ergo.log | grep ERR
tail -Fn+0 ergo.log | grep xception
tail -Fn+0 ergo.log | grep "stuck"
```

## Synchronization Issues

There are common problems that may occur during synchronization.

### Stuck on 'Active Synchronization'

If your node is stuck on Active Synchronization without a noticeable increase in height, try the following steps:

1. Use the log commands from above to see if there is anything noticeably wrong.

## Keywords
node, troubleshooting, guide, document, issue, ergo, reference, client, problem, ergoplatform, choose, detail, version, java, command, specification, system, storage, location, cloud

## Content
## Node Troubleshooting Guide
This document aims to help you troubleshoot common issues with the Ergo reference client. If you encounter a problem not covered here, please create a new issue on GitHub and provide the following details:
Node version
Java command used
RAM/CPU specification
Operating System
JVM version
Storage location (Cloud, SSD, etc)
output of ERROR/WARN
You can obtain the output of ERROR/WARN by executing the following command:
bash
tail -Fn+0 ergo.log | grep 'ERROR\|WARN' > output.log

### Searching the Logs
The following commands can help you search your logs for specific entries:
bash
tail -Fn+0 ergo.log | grep 'ERROR\|WARN'
tail -Fn+0 ergo.log | grep 'ERROR'
tail -Fn+0 ergo.log | grep "not modified"
tail -Fn+0 ergo.log | grep ERR
tail -Fn+0 ergo.log | grep xception
tail -Fn+0 ergo.log | grep "stuck"

### Synchronization Issues
There are common problems that may occur during synchronization.

#### Stuck on 'Active Synchronization'
If your node is stuck on Active Synchronization without a noticeable increase in height, try the following steps:
Use the log commands from above to see if there is anything noticeably wrong.
Shut down your instance, take a backup, and try to restart.
Join the #node channel on Discord for support or open an issue on GitHub.

#### Node Appears 'Synchronised' Even When It Isn't
If your node appears synchronised even though the height doesn't match the latest one found on the explorer, you can add this to your .conf file under ergo { node {:
```conf

## headerChainDiff = 80
```
You might also be experiencing a header downloading problem during synchronization.

#### Lowering maxConnections
To alleviate some performance issues on later blocks, you can lower the default maxConnections from 30 to 10 in your ergo.conf:
bash
network {
    maxConnections = 10
}
This makes the sync process slower but it should run more smoothly.

#### Reverting Without Resyncing
The latest versions of the node will attempt to fix any errors on their own, but if it fails, there is no way to manually roll back.

#### Resyncing From Scratch
To resync, remove the following two directories and restart the node:
bash
rm -rf .ergo/state
rm -rf .ergo/history

#### Timeouts or Unresponsiveness Under Load
Symptoms:
API requests (e.g., from your wallet, dApp backend, or scripts) take a very long time to respond or fail with timeout errors.
The node's web panel (/panel) might become slow or unresponsive.
This often occurs when the node is handling multiple concurrent API requests or processing large amounts of data.
Potential Causes & Solutions:
Insufficient JVM Memory: The Java Virtual Machine (JVM) running the node might not have enough allocated memory (heap space) to handle the load efficiently, leading to excessive garbage collection pauses or out-of-memory situations.

Check: Monitor the node's memory usage using system tools (like htop, Task Manager) or JVM monitoring tools if available. Look for high memory usage approaching the allocated limit.
Solution: Increase the maximum heap size allocated to the JVM using the -Xmx flag in your node startup command. For example, if you are running with -Xmx4G, try increasing it to -Xmx6G or -Xmx8G (ensure your system has enough physical RAM).
    bash
    # Example startup command with increased memory:
    java -jar -Xmx6G ergo-*.jar --mainnet -c ergo.conf
Restart the node after changing the -Xmx value.



High System Load: The server running the node might be overloaded due to other processes consuming CPU, RAM, or disk I/O. Check overall system resource usage.


Node Mode Limitations: Certain node modes (like Digest mode) might have inherent limitations in handling specific API queries that require scanning the full UTXO set, potentially leading to slower responses for those queries. Refer to the Node Modes documentation.


Network Latency: Slow network connections between your client application and the node can also contribute to perceived timeouts.


Specific API Endpoint Issues: Occasionally, a specific API endpoint might have a bug or inefficiency causing performance problems. Check the Ergo Node GitHub Issues for reports related to the endpoint you're using.

#### Correct Address/Balance Not Displayed
If your correct address or balance isn't displayed, follow these steps:
Make sure the wallet is synchronised.
Try to derive new addresses as per the swagger instructions.
Ensure you derived additional addresses during the sync process.
If the problem persists, restore the wallet on a different client.

#### 'Unable to Define External Address'
If you see this warning:
WARN [tor.default-dispatcher-11] s.c.n.NetworkController - 
Unable to define external address.
Specify it manually in `scorex.network.declaredAddress`
it means you aren't running a public node. You can ignore this warning.

#### 'Got GetReaders Request in State None'
This error message is normal in the first few minutes of starting the node:
WARN  [ergoref-api-dispatcher-9] 
o.e.n.ErgoReadersHolder 
Got GetReaders request in state (None,None,None,None)
If you continue to receive this message, it likely indicates database corruption, which can be caused by unexpected shutdowns. To resync, remove the directories .ergo/state and .ergo/history, then restart the node.

#### 'Invalid Z Bytes'
This error is related to parsing the z value for this constructor: UncheckedSchnorr(dl, None, challenge, SecondDLogProverMessage(z)).
To view the log entries surrounding this error, use the following command:
bash
cat ergo.log | grep -A 30 -B 30 "Invalid z bytes"

#### 'Dead Letters'
In Akka, messages that cannot be delivered are routed to an actor with the path /deadLetters. Dead letters do not necessarily indicate a problem but are logged by default for caution.
To search for these messages, use the following command:
bash
tail -Fn+0 ergo.log | grep "akka.log-dead-letters"

#### 'Failed to Connect to localhost Port 9053: Connection Refused'
You can use these commands to troubleshoot:
bash
netstat -ln | grep 9053
sudo netstat -tulpn

#### 'Tree Root Should Be Real'
This error typically means you're trying to sign a box that you don't own (i.e., you don't have the private key needed to sign).

### Issues with Public Nodes & Explorers
While running your own node provides the most control and trust, many users rely on public infrastructure (nodes and explorers) for convenience or when running a personal node isn't feasible.
Known Public Resources (Community-Run, Status May Vary):
Node Lists:
ergonodes.net: Provides a list of public nodes with basic status monitoring.


Explorers (Often provide public API access):
explorer.ergoplatform.com (Official)
ergexplorer.com
sigmaspace.io
ergobackup.aap.cornell.edu (May primarily be a backup service, check API availability)


(Note: This list is not exhaustive and uptime/reliability are not guaranteed. Always verify the trustworthiness and status of a public service before relying on it for critical operations.)
Troubleshooting Public Infrastructure Issues:
If you encounter problems with a public node or explorer (e.g., incorrect data, API timeouts, connectivity problems, website errors):
Try Alternatives: The simplest first step is to switch your wallet or application to use a different public node/explorer from the lists above or other known community resources. The issue might be specific to the service you were initially using.
Check Service Status:
For nodes listed on ergonodes.net, check their reported status (height, sync status).
Check the explorer website itself for any status banners or announcements.
Look in community channels (Discord, Telegram) for recent reports about the specific service.


Identify the Operator (If Possible): Some public services are run by known community projects or individuals. If you can identify the operator, check their specific project channels (Discord, Telegram, GitHub) for status updates or to report issues.
Report in General Community Channels: If the operator is unknown or the issue seems widespread, report the problem in general Ergo community support channels (like the #node or relevant dApp/wallet channels on Discord). Provide clear details:
The IP address or URL of the public node/explorer.
The specific issue...
