# Proot (RocksDB) - ErgoDocs
Source: [https://docs.ergoplatform.com/node/install/node-android/proot-rocksdb/](https://docs.ergoplatform.com/node/install/node-android/proot-rocksdb/)
Generated: 2025-05-11

## Summary
This guide details the more advanced method for running an Ergo node on Android using an Arch Linux environment within Termux via proot. This method is necessary if you need to run the node with stateType="utxo" (which uses RocksDB for state storage) or if you encounter database issues (e.g., LevelDB failures) with the direct Termux setup. Why is this needed? Disclaimer:

## Keywords
guide, method, ergo, node, android, arch, linux, environment, termux, proot, statetype="utxo, state, storage, database, issue, leveldb, failure, setup, disclaimer, case

## Content
## Android Node: Arch Linux via proot (RocksDB/UTXO Mode)#
This guide details the more advanced method for running an Ergo node on Android using an Arch Linux environment within Termux via proot. This method is necessary if you need to run the node with stateType="utxo" (which uses RocksDB for state storage) or if you encounter database issues (e.g., LevelDB failures) with the direct Termux setup.
Why is this needed?
The Ergo node uses database engines (LevelDB by default, RocksDB as an option, especially for stateType="utxo") to store blockchain state.
The Java bindings for RocksDB often rely on the standard GNU C Library (glibc).
Android/Termux typically use a different C library (musl libc via Bionic).
Running the RocksDB-enabled node JAR directly in Termux can lead to incompatibility errors.
proot-distro allows running a Linux distribution (like Arch Linux, which uses glibc) within Termux, providing the necessary environment for RocksDB.
Disclaimer: This is a more complex setup than the direct Termux method and adds overhead. It's primarily required for specific use cases needing RocksDB/UTXO mode. For most mobile users, the direct Termux setup with stateType="digest" is recommended.
Prerequisites:
Android device meeting the requirements (Note: UTXO mode requires significantly more storage than digest mode).
Termux installed from F-Droid.
Steps:
Install proot-distro in Termux:
Open Termux and run:
    pkg update && pkg upgrade -y
pkg install proot-distro -y



Install Arch Linux via proot-distro:
proot-distro install archlinux

This will download the Arch Linux root filesystem.


Login to Arch Linux Environment:
Each time you want to run the node using this method, you first need to log into the Arch environment:
    proot-distro login archlinux

Your terminal prompt should change, indicating you are now inside Arch Linux within Termux.


Inside Arch Linux: Install Dependencies (First Time Only):
Update package lists:
    pacman -Syu --noconfirm

Install Java (OpenJDK 17 recommended), wget, and nano:
    pacman -S jdk-o...
