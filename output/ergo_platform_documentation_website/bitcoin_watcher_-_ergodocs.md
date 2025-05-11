# Bitcoin Watcher - ErgoDocs
Source: [https://docs.ergoplatform.com/eco/rosen/bitcoin-watcher/](https://docs.ergoplatform.com/eco/rosen/bitcoin-watcher/)
Generated: 2025-05-11

## Summary
To participate as a watcher in the Rosen Bridge, you need to deploy a watcher app that observes one of the supported networks. Each supported network has its own set of watchers responsible for reporting users' actions on that specific network. This section is adapted from the deploy-docker.md section on the Rosen Bridge documentation. Clone the Operation repository and navigate to the operation/watcher directory: Create your environment file .env based on the env.template file in the watcher directory: To view hidden .env files later, use ls -a.

## Keywords
watcher, rosen, bridge, network, user, action, section, documentation, operation, repository, directory, environment, file, .env, variable, space, sign, permission, config, macos

## Content
## Bitcoin Rosen Bridge Watcher Setup#
To participate as a watcher in the Rosen Bridge, you need to deploy a watcher app that observes one of the supported networks. Each supported network has its own set of watchers responsible for reporting users' actions on that specific network.

### Docker Setup#
This section is adapted from the deploy-docker.md section on the Rosen Bridge documentation.
Clone the Operation repository and navigate to the operation/watcher directory:
git clone https://github.com/rosen-bridge/operation.git
cd operation/watcher/
Create your environment file .env based on the env.template file in the watcher directory:
cp env.template .env
To view hidden .env files later, use ls -a.

#### Environment Variable Configurations#
Configure the required environment variables in the .env file (ensure no spaces after the '=' sign):
# Required Environments

POSTGRES_PASSWORD=your_random_password
POSTGRES_USER=your_random_username
POSTGRES_DB=your_random_db_name
POSTGRES_PORT=5432
Set the required permissions and create the local.yaml file in the config directory:
sudo chown -R 3000:3000 logs
touch config/local.yaml
For MacOS users, set 707 permission for the logs directory:
sudo chmod -R 707 logs
Working with Docker

Checking logs
{type: info, open: false}
To check logs, use:
docker compose logs



Updating your watcher
{type: info, open: false}
To update your watcher, use:
docker compose pull
docker compose down
docker compose up -d



Restarting your watcher
{type: info, open: false}
To restart your watcher instance, run:
docker compose up -d



no configuration files provided: not found
{type: danger, open: false}
Ensure you're in the correct directory. You should execute docker compose commands from within the operation/watcher folder.


Dumping databases
{type: info, open: false}
To dump databases, use:
docker compose down
docker volume remove watcher_postgres-data


#---edit block height in YAML after this step
docker compose up -d



Clearing Volumes
{type: info, open: false}
To clear Docker volumes, use:
docker compose down --volumes

Re-initiate the watcher with:
docker compose up -d



Clean Slate
{type: info, open: false}
To remove everything and start from scratch:
docker ps -a
docker compose down
docker rm CONTAINERID1 CONTAINERID2 CONTAINERID3

Then delete the folder and start fresh.
Note for Raspberry Pi ARM Users
{type: info, open: false}
To run the watcher on an ARM-based Raspberry Pi, use an ARM-based DB image. Update the docker-compose.yml as follows:
Change the DB image according to your architecture (e.g., arm64v8):
services:
  db:
-   image: rapidfort/postgresql:16.0.0
+   image: arm64v8/postgres:16.0

Update the volume of the DB:
    volumes:
-     - postgres-data:/bitnami...

#### Pull Docker Images and Run Service#
Pull the Docker image:
docker compose pull
Set up your local.yaml using the instructions in the next section (Local Config). After saving the changes, run the container:
docker compose up -d

### Local Config#
To start your watcher, configure the local.yaml file.

#### Specify the Target Network#
Set the target network you're watching. Currently supported networks are ergo, cardano, and bitcoin:
network: bitcoin

#### API Configuration#
api:
  apiKeyHash: "YOUR_API_KEY_HASH"
To secure the action-based APIs (e.g., lock, unlock), set a unique and robust API key hash using the Blake2b algorithm. You can generate the hash using the rosen command line:
npx @rosen-bridge/cli blake2b-hash YOUR_API_KEY
Alternatively, use Docker:
docker run -it --rm node:18.16 npx --yes @rosen-bridge/cli blake2b-hash YOUR_API_KEY

#### Bitcoin Configuration#
Choose your information source for the Bitcoin network and specify its connection information.
You can use either rpc
bitcoin:
  type: rpc
  rpc:
    url: "YOUR_RPC_URL"
    username: "YOUR_RPC_USERNAME"
    password: "YOUR_RPC_PASSWORD"
Setting Up a Bitcoin Node (RPC)
{type: info, open: false}
For optimal watcher performance and decentralization, running your own fully synced Bitcoin node is recommended. However, this consumes significant disk space, so you can use a public node as detailed in the next section.


Install Bitcoin Core following the official instructions for your OS.


Configure Bitcoin Core:


Locate the bitcoin.conf file in the Bitcoin data directory:

Linux: ~/.bitcoin/
macOS: ~/Library/Application Support/Bitcoin/
Windows: %APPDATA%\Bitcoin\



Open bitcoin.conf with a text editor or create it if it doesn't exist.


Generate an RPC username and password:


Visit this RPC auth generator

Enter a username and click "Generate"

Copy the generated line starting with rpcauth=


Edit bitcoin.conf to enable the RPC server and allow the watcher to connect:


Paste the rpcauth line you copied

Add the following lines to enable the RPC server:
     server=1
rpcbind=0.0.0.0
rpcallowip=0.0.0.0/0
txindex=1
rest=1


To limit RPC access to only the watcher container, set rpcallowip to the Docker network range:
rpcallowip=172.16.0.0/12



Save the file


If bitcoind was already running, stop and restart it:


bitcoin-cli stop
bitcoind -daemon


Verify the node is running and wait for it to sync:
   bitcoin-cli getblockchaininfo

   Look for "initialblockdownload": false to confirm the node is synced.


Running a Pruned Bitcoin Node
{type: info, open: false}
A pruned Bitcoin node is not compatible with the Rosen Bitcoin bridge watcher. The watcher requires the txindex=1 setting, which is not supported by pruned nodes. If you initially synced a pruned node, you'll need to restart the sync with a full node.


Increasing Bitcoin Node DbCache
{type: info, open: false...

#### Ergo Configuration#
Even if you are running a Bitcoin Watcher, you must configure the Ergo section
Create a new wallet and set the wallet mnemonic, you can also load this through an environmental variable so it's only stored in-memory.
ergo:
  mnemonic: "YOUR_WALLET_MNEMONIC"
Select your primary data source:
ergo:
  type: node
  node:
    url: https://example.node.com
  explorer:
    url: https://api.ergoplatform.com
Set the initial height of your watcher:
initialHeight: LATEST_HEIGHT
Customize observation confirmation and validity threshold:
observation:
  confirmation: 10
  validThreshold: 720

#### Example Configuration for Bitcoin Watcher#
network: bitcoin
api:
  apiKeyHash: "YOUR_API_KEY_HASH"
ergo:
  type: explorer
  initialHeight: LATEST_ERGO_HEIGHT
  mnemonic: "YOUR_WALLET_MNEMONIC"
  node:
    url: https://example.node.com
bitcoin:
  type: rpc
  rpc:
    url: "YOUR_BITCOIN_RPC_URL"
    username: "YOUR_RPC_USERNAME"
    password: "YOUR_RPC_PASSWORD"
  initial:
    height: LATEST_BITCOIN_HEIGHT
observation:
  confirmation: 2
  validThreshold: 72

### Get Your Watcher Permit#
After setting up and running your watcher instance, access the watcher UI by visiting localhost:3030. From your dashboard, you can view network information, assets, and health status alongside action buttons. To activate your watcher, proceed to the 'LOCK' action, where you can utilize assets from the watcher wallet for registration and obtain reporting permits. Top up your wallet with the specified amounts of ERG and RSN to receive these permits.
As a watcher, your primary responsibility is to monitor your network and report actions related to the bridge. To report a bridge event, you must have report permits. Acquiring these permits involves two types of payments:
Collateral: Provide one-time collateral in the form of ERG and RSN tokens to obtain initial report permits. This collateral serves as a security measure to mitigate Sybil attacks. When you return all your report permits, the collateral is refunded, and your watcher is unregistered.


RSN for Permits: Lock RSN tokens to receive permit tokens. Use these tokens to create report permits for reporting events. The number of report permits determines how many concurrent reports you can create. In the event of a valid report, the permit is refunded along with your reward. If the report is invalid, the permit is seized as a penalty.
For tips, troubleshooting, FAQs, and other information, please refer to the main watcher documentation.
