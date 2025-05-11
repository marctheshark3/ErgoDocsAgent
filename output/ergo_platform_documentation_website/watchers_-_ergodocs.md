# Watchers - ErgoDocs
Source: [https://docs.ergoplatform.com/eco/rosen/watcher/](https://docs.ergoplatform.com/eco/rosen/watcher/)
Generated: 2025-05-11

## Summary
Watchers are integral to Rosen Bridge, serving as cross-chain oracles. They observe and report deposit events on their network to Ergo, contributing to the network's security and expansion. See the pre-requisites page for information on setting up a local node, as well as minimal hardware and software requirements. (Docker) There is a General Watchers app Tutorials Playlist, and more tailored guides for each platform available: mgpai walks through a Watcher instance in Linux and Cloud Below you'll find some frequently asked questions as well as common issues and troubleshooting tips. Watchers are essential for accurate reporting and receive 70% of transaction fees as rewards for successful and accurate reporting.

## Keywords
watcher, rosen, bridge, oracle, deposit, event, network, ergo, security, expansion, page, information, node, hardware, software, requirement, docker, general, watchers, tutorials

## Content
## Ergo Rosen Bridge Watcher Setup#
Watchers are integral to Rosen Bridge, serving as cross-chain oracles. They observe and report deposit events on their network to Ergo, contributing to the network's security and expansion.

### Watcher Setup Guides#
Tutorials

Pre-requisites
See the pre-requisites page for information on setting up a local node, as well as minimal hardware and software requirements. (Docker)

There is a General Watchers app Tutorials Playlist, and more tailored guides for each platform available:

Windows

Follow along as QX guides you through a Windows Watcher installation
Rosen Bridge Watcher â Windows Setup Guide



Mac

Rosen Watcher with Mac (ErgoTutorials)



Linux
mgpai walks through a Watcher instance in Linux and Cloud

Below you'll find some frequently asked questions as well as common issues and troubleshooting tips.

#### Operational#
Role and Rewards
Watchers are essential for accurate reporting and receive 70% of transaction fees as rewards for successful and accurate reporting. (while 30% goes to the guard set). 25% of the emission is also reserved for 'Event-Based Emission (Rewards)'
Who can become a Watcher?
Anyone. You can actively contribute to the expansion and security audit of the Rosen Bridge by becoming a Watcher. Watchers receive rewards for accurate reporting.

Configure and run the Watcher app for your desired network (In progress, so stay tuned!).
Top it off with enough RSN and ERG.
Put in collateral and receive reporting permits.
Enjoy reporting and getting rewards.
Is there a limit on the number of watchers?
77 is the one repo's capacity and cannot be changed, but we'll open other repos. So technically, we can have any number of repos that each has 77 watchers. However, in long run I assume one or two repos is sufficient for each network.
A minimum of 60%+1 of the total number of watchers is required to trigger an event, adjustable by the guard set.
Can I run multiple watchers?
Yes, but it incurs financial considerations to prevent abuse. Each instance needs a unique folder and WATCHER_PORT.

#### Collateral, Permits and Reporting#
Collateral Requirements
Each instance requires 800 ERG and 30,000 RSN as collateral. This collateral is fully redeemable and the amount is adjustable.
How do I redeem my collateral?
You can redeem it after redeeming your last permit token, but if you have unsettled reports, you must wait until those permits are returned.
Permit Acquisition
To report, watchers must acquire permits, costing an additional 3,000 RSN. Multiple permits are necessary for reporting concurrent events, and permits can be seized if reports are found fraudulent.
Reporting Process

Watchers report deposit events as part of a collective effort.
A consensus among watchers on an event triggers a final report and guard intervention.
Guards take necessary actions based on these reports.
Watchers involved in successful cross-chain settlements are rewarded.
What if my report is successful?
You'll receive rewards and your staked amount will be returned.
What if my report is incorrect and uncorroborated?
You'll get a refund of your stake without any additional penalties.
What are the consequences of collusion and fraud in reporting?
Colluding watchers will lose the amount they staked.
Are permits spent or staked for reporting?
Permits are staked, not spent, and can be managed through your dashboard.
Can I adjust my permits?
Yes, you can increase or decrease your permits at any time and redeem them when leaving.
How many permits are needed for concurrent reporting?
The number depends on bridge activity, with about 160 needed to report one transaction per minute.
Do I still need RSN on Ergo to be a watcher on another chain?
Yes, all permit operations are conducted on the Ergo platform, and Rosen's logic is Ergo-based.

### Operational#
Do I need to do anything after setup?
You don't need to manually watch and approve transactions, the software will handle everything automatically, you just need to ensure the watcher keeps running.

Observe an event and wait a bit.
Create a commitment using report permits.
Aggregate all participating watchers commitment (into something called event trigger).
Wait for guards stuff, especially target chain tx and reward tx submission.
Get rewards.
Interacting with a headless server
To interact with a headless server, you can use SSH (Secure Shell) to establish a secure connection. You can also forward ports to access specific services on the server. In the example below, we are using SSH to forward the local port 3030 to port 3030 on the server. This allows us to access a service running on port 3030 of the server as if it was running on our local machine.
ssh -L 3030:127.0.0.1:3030 user@watcher-server

In this command:

ssh is the command to start the SSH client program.
-L 3030:127.0.0.1:3030 specifies that the local port 3030 should be forwarded to port 3030 on the server. 127.0.0.1 is the loopback IP address, which refers to the server itself in this context.
user@watcher-server specifies the username and the server to connect to. Replace user with your actual username and watcher-server with the actual hostname or IP address of your server.
Security Considerations
{type: warning, open: false}

Keep your watcher machine and Docker installation updated with the latest security patches.
Do not reuse your watcher's RPC password anywhere else.
Secure your machine's SSH login with a strong password and/or public key authentication.
Consider running the watcher in a dedicated VM or container for isolation.
Regularly monitor your watcher's logs and web UI for any signs of issues.
Keep your collateral wallet secure, as the wallet owner has control over unstaking collateral.
Monitoring and Alerting
{type: info, open: false}
Maintaining high watcher uptime is critical to a...

#### UI Errors#
scanner is out of sync
Your scanner is out of sync. You need to wait until it scan all blocks. The service runs every 3 minutes or so. Depending on when it calls and blocks produced it may drop a block sync here and there but catches up in most cases.
Alternatively you can delete docker volumes and restart your watcher with newer initial height
Then it doesn't need to scan that much blocks to be synced
docker compose down --volumes

Then update the local.yaml initial height
Then rerun the watcher
Permit Health Broken
By default, the permit health warning parameter is set to 100. This is adjustable locally by adding the following into your local.yaml and adjusting as neccessary
healthCheck:
  permit:
     warnCommitmentCount: 1 # amount of permits left before giving a warning
     criticalCommitmentCount: 0 # amount of permits left it is critical

Adjust the numbers as you wish.
warnCommitmentCount will change the warning to yellow when the available Permits reduce to the number.
criticalCommitmentCount will change to red when the available Permits reduce to this number.
watcher-db-1 is unhealthy

dependency failed to start: container watcher-db-1 is unhealthy


Your .env file might be missing? turn on view file extensions like in the video, are you sure it's .env and not .env.txt?
update your local.yaml with the current ergo blockheight

As a last resort, some ssers are reporting that this issue can be fixed by pruning existing images and rebuilding 
docker system prune -a

As long as you don't have other docker images to worry about.
Lock, Unlock 500 Error
If you're receiving a 500 Error while trying to lock or unlock your ERG and/or RSN, it could possibly be from having an insufficient box value on chain. This is fixed in the latest release, please update if you have not done so already.
Update with 
docker-compose pull
docker-compose down
docker-compose up -d

please check your service logs first. If you see a warning indicating "Box value BoxValue(1100000) is to...

#### Working with docker#
Checking logs
docker compose logs
Updating your watcher
docker-compose pull
docker-compose down
docker-compose up -d
Restarting your watcher
You can restart your watcher instance simply by running the following command from within the same folder the docker-compose.yaml is stored.
docker compose up -d
no configuration files provided: not found
Check you're in the correct directory. You should be executing docker compose commands from within the operation/watcher folder
Dumping databases
docker compose down
docker volume remove watcher_postgres-data
#---edit block height in YAML after this step
docker compose up -d
Clearing Volumes
You may wish to clear Docker volumes for a number of reasons, e.g. changing Initial_Height to sync. To do so run the following Docker command from the Watcher directory
docker compose down --volumes

Re-initiate the Watcher with
docker compose up -d
Clean Slate
If you want to remove everything and start from scratch
docker ps -a
docker compose down
docker rm CONTAINERID1 CONTAINERID2 CONTAINERID3

then delete the folder and start fresh
