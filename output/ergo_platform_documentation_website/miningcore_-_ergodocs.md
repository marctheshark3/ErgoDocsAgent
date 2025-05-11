# MiningCore - ErgoDocs
Source: [https://docs.ergoplatform.com/mining/setup/miningcore/](https://docs.ergoplatform.com/mining/setup/miningcore/)
Generated: 2025-05-11

## Summary
ð¡ If you're using Windows 10, see the Windows Tutorial Requirements: Replace 'your-secure-password' with a strong password: â Make sure you can connect using psql before proceeding. You should configure your pool to auto-start using a startup script. The JSON config defines the log files you should monitor for: You may need to adjust the config to fit your specific pool setup. When everything is working properly, your logs should show the following messages: â ï¸

## Keywords
windows, tutorial, requirements, replace, password, psql, pool, auto, start, startup, script, json, config, setup, message, network, difficulty, value, check, diff

## Content
## ð§± MiningCore Setup Tutorial for Linux#
ð¡ If you're using Windows 10, see the Windows Tutorial

### Step 1: Download MiningCore#
Clone Mining Core from GitHub
Requirements:
You must have a working PostgreSQL database
Ensure you meet all dependencies from the README
Avoid Docker unless you are confident managing containers

### Step 2: Install and Configure PostgreSQL#
For production environments:
Monitor I/O, disk, CPU, and memory â MiningCore's API can put heavy load on your DB
Keep all PostgreSQL settings default for now


Reference setup guide

#### Login to PostgreSQL#
sudo -u postgres psql

#### Create Role and Database#
Replace 'your-secure-password' with a strong password:
CREATE ROLE miningcore WITH LOGIN ENCRYPTED PASSWORD 'your-secure-password';
CREATE DATABASE miningcore OWNER miningcore;

### Step 4: Load Schema SQL Files#
â Make sure you can connect using psql before proceeding.
As the postgres user, run:
psql -d miningcore -f miningcore/src/Miningcore/Persistence/Postgres/Scripts/createdb.sql
Then apply the partitioning script:
psql -d miningcore -f miningcore/src/Miningcore/Persistence/Postgres/Scripts/createdb_postgresql_11_appendix.sql

### Step 5: Create a Pool Table#
Run the following command once per pool you set up:
CREATE TABLE shares_mypool1 PARTITION OF shares FOR VALUES IN ('mypool1');
Replace mypool1 with your pool's unique identifier
This name is used in the configuration files as well

### Step 6: Configure the Pool#
Go to the build/ directory inside your MiningCore folder
Create a <coin>.json configuration file (e.g. ergo.json)
Refer to: MiningCore Config Example and the example given below.
Example Ergo config.json:
Required Fields in Config#

Replace placeholders:
YOURPOSTGRESQL_PASSWORD_GOES_HERE
YOUR_REWARD_ADDR_GOES_HERE


Adjust:
rewardRecipients percentage to fit your payout model
Enable paymentProcessing if you will use automatic share payouts



{
    "logging": {
        "level": "info",
        "enableConsoleLog": true,
        "enableConsoleColors": true,
        // Log file name (full log) - can be null in which case log events are written to console (stdout)
        "logFile": "core.log",
        // Log file name for API-requests - can be null in which case log events are written to either main logFile or console (stdout)
        "apiLogFile": "api.log",
        // Folder to store log file(s)
        "logBaseDirectory": "/path/to/logs", // or c:\path\to\logs on Windows
        // If enabled, separate log file will be stored for each pool as <pool id>.log
        // in the above specific folder.
        "perPoolLogFile": false
    },
    "banning": {
        // "integrated" or "iptables" (linux only - not yet implemented)
        "manager": "Integrated",
        "banOnJunkReceive": true,
        "banOnInvalidShares": false
    },
    "notifications": {
        "enabled": true,
        "email": {
            "host": "smtp.example.com",
            "port": 587,
            "user": "user",
            "password": "password",
            "fromAddress": "[email protected]",
            "fromName": "pool support"
        },
        "admin": {
            "enabled": false,
            "emailAddress": "[email protected]",
            "notifyBlockFound": true
        }
    },
    // Where to persist shares and blocks to
    "persistence": {
        // Persist to postgresql database
        "postgres": {
            "host": "127.0.0.1",
            "port": 5432,
            ...

#### Required Fields in Config#
Replace placeholders:
YOURPOSTGRESQL_PASSWORD_GOES_HERE
YOUR_REWARD_ADDR_GOES_HERE


Adjust:
rewardRecipients percentage to fit your payout model
Enable paymentProcessing if you will use automatic share payouts
{
    "logging": {
        "level": "info",
        "enableConsoleLog": true,
        "enableConsoleColors": true,
        // Log file name (full log) - can be null in which case log events are written to console (stdout)
        "logFile": "core.log",
        // Log file name for API-requests - can be null in which case log events are written to either main logFile or console (stdout)
        "apiLogFile": "api.log",
        // Folder to store log file(s)
        "logBaseDirectory": "/path/to/logs", // or c:\path\to\logs on Windows
        // If enabled, separate log file will be stored for each pool as <pool id>.log
        // in the above specific folder.
        "perPoolLogFile": false
    },
    "banning": {
        // "integrated" or "iptables" (linux only - not yet implemented)
        "manager": "Integrated",
        "banOnJunkReceive": true,
        "banOnInvalidShares": false
    },
    "notifications": {
        "enabled": true,
        "email": {
            "host": "smtp.example.com",
            "port": 587,
            "user": "user",
            "password": "password",
            "fromAddress": "[email protected]",
            "fromName": "pool support"
        },
        "admin": {
            "enabled": false,
            "emailAddress": "[email protected]",
            "notifyBlockFound": true
        }
    },
    // Where to persist shares and blocks to
    "persistence": {
        // Persist to postgresql database
        "postgres": {
            "host": "127.0.0.1",
            "port": 5432,
            "user": "miningcore",
            "password": "YOURPOSTGRESQL_PASSWORD_GOES_HERE",
            "database": "miningcore"
        }
    },
    // Generate payouts for recorded shares and blocks
    "paymentProcessing": {
        "enabled"...

### Step 7: Start the Pool#
You should configure your pool to auto-start using a startup script.
cd build
Miningcore -c <your-config>.json
The JSON config defines the log files you should monitor for:

Startup errors
Daemon issues
Pool activity



You may need to adjust the config to fit your specific pool setup.

#### â Expected Log Output (Success)#
When everything is working properly, your logs should show the following messages:

##### ð¢ Node Online and Synced#
[2022-03-16 14:26:12.9080] [I] [ergo1] All daemons online
[2022-03-16 14:26:12.9345] [I] [ergo1] Daemon is synced with blockchain

##### ð¢ Pool Online#
[2022-03-16 14:26:14.4346] [I] [ergo1] Pool Online

##### ð Pool Info Summary#
Mining Pool:            <YOUR POOL NAME>
Coin Type:              ERG [ERG]
Network Connected:      <testnet|mainnet>
Detected Reward Type:   POW
Current Block Height:   <BLOCKHEIGHT>
Current Connect Peers:  5
Network Difficulty:     <NETWORK DIFF>
Network Hash Rate:      <NETWORK HASHRATE>
Stratum Port(s):        3056, 4056, 3156, 4156
Pool Fee:               <YOUR FEE>
â ï¸ If the network difficulty or other values look off, double-check your diff setting in the config.

### Step 8: Network Setup Notes#
If your miner, pool, or node are on different machines, you will need to open ports to allow communication between them.

#### Initial Mining Traffic Flow#
Miner
  â connects to Stratum port (e.g. 3746)  
Pool Server
  â connects to Node RPC (mainnet: 9053, testnet: 9052)  
Node
Once all components connect, traffic becomes bi-directional.

#### Port Opening Guidelines#
If all components are on the same machine:

â No need to open ports â uses localhost



If using LAN or WAN:

ð¥ï¸ Open required ports on your OS firewall
ð On WAN, configure port forwarding on your router

### You're Good to Go!#
You now have a fully operational MiningCore pool on Linux.
Make sure everything is synced, ports are configured, and logs show green â then start mining! âï¸
