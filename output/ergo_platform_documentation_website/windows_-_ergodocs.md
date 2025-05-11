# Windows - ErgoDocs
Source: [https://docs.ergoplatform.com/mining/setup/pool_win/](https://docs.ergoplatform.com/mining/setup/pool_win/)
Generated: 2025-05-11

## Summary
This guide walks you through setting up MiningCore on a Windows 10 machine step-by-step. â ï¸ During installation, you do not need to install StackBuilder. In the pSQL Shell, run the following commands (replace myPassword with your actual password): Locate the following files on your PC: Then, in the pSQL Shell, run these commands (replace with actual paths): For each coin you setup, create a partition of the shares table: ð Replace coinName with your desired coin identifier (e.g., btc, eth). ð

## Keywords
guide, miningcore, windows, machine, step, installation, stackbuilder, psql, shell, command, mypassword, password, locate, file, path, coin, setup, partition, share, table

## Content
## MiningCore Setup Tutorial on Windows 10#
This guide walks you through setting up MiningCore on a Windows 10 machine step-by-step.

### ð¦ Step 1: Install PostgreSQL#
Download and install PostgreSQL 10 or the latest version:
  ð https://www.postgresql.org/download/
â ï¸ During installation, you do not need to install StackBuilder.

### ð Step 2: Launch pSQL Shell#
Open the Windows search bar and type psql.
Launch the pSQL Shell.
Login using the credentials you set during PostgreSQL installation.
Username: postgres (default)
Password: (the one you set during install)

### ð Step 3: Create Database Role and Schema#
In the pSQL Shell, run the following commands (replace myPassword with your actual password):
CREATE ROLE miningcore WITH LOGIN ENCRYPTED PASSWORD 'myPassword';
CREATE DATABASE miningcore OWNER miningcore;

### ð Step 4: Run Database Setup Scripts#
Locate the following files on your PC:
createdb.sql
createdb_postgresql_11_appendix.sql
Then, in the pSQL Shell, run these commands (replace with actual paths):
\i c:/Users/YourUser/Desktop/miningcore/src/Miningcore/Persistence/Postgres/Scripts/createdb.sql
\i c:/Users/YourUser/Desktop/miningcore/src/Miningcore/Persistence/Postgres/Scripts/createdb_postgresql_11_appendix.sql

### ð§± Step 5: Create Pool Table#
For each coin you setup, create a partition of the shares table:
CREATE TABLE shares_coinName PARTITION OF shares FOR VALUES IN ('coinName');
ð Replace coinName with your desired coin identifier (e.g., btc, eth).

### âï¸ Step 6: Configure the Pool#
Go to your MiningCore build directory.
Create a coinName.json config file for your coin.
Inside the config file:
Ensure "logFile" and "apiLogFile" under "logging" are filled in (e.g., coinName_core.log, coinName_api.log).
ð Example config:
MiningCore Configuration Example

### ð ï¸ Step 7: Create a Startup Batch File#
In your MiningCore root directory, create a .bat file with the following content (adjust for your coin name):
cd build
./Miningcore -c coinName.json

### â Step 8: All Done!#
MiningCore is now set up and ready to go!
â ï¸ Ensure your coin's node is fully synced before launching the pool.
Happy mining! âï¸
