# ErgoScript Playground with KioskWeb
Source: docs/dev/stack/kiosk.md
Generated: 2025-05-11

## Summary
<!-- TODO: Check if this is still the most up to date info -->

/// admonition | Archive
    type: warning

The Kiosk repository has been archived by the owner on May 26, 2022. It is now read-only. ///


# ErgoScript Playground with KioskWeb

[KioskWeb](https://github.com/scalahub/KioskWeb), built on top of the [Kiosk](https://github.com/scalahub/Kiosk) project, offers a user-friendly web interface to interact with ErgoScript.

## Keywords
todo, date, info, admonition, archive, type, kiosk, repository, owner, ergoscript, playground, kioskweb, kioskweb](https://github.com, scalahub, kiosk](https://github.com, project, user, interface, action, define

## Content
## ErgoScript Playground with KioskWeb
KioskWeb, built on top of the Kiosk project, offers a user-friendly web interface to interact with ErgoScript. It allows you to perform the following actions:
Define boxes with custom ErgoScript code and register values.
Create transactions that output specific predefined boxes.

### Getting Started
KioskWeb requires a fully configured Ergo node to be running. By default, it assumes the node's REST API is accessible at http://localhost:9052. You can modify this by invoking the method org.sh. Kiosk.ergo.ErgoAPI.setUrl from the web-UI.
A precompiled jar is available here. You can run it using the command java -jar <jarfile>. If you wish to generate the jar from sources, issue the command sbt assembly.
To operate a local copy (the recommended approach), clone the project and follow one of these steps:
Run sbt using the command sbt. Inside the sbt prompt, type jetty:start. This command initiates the built-in Jetty web server on port 8080, which can be accessed at http://localhost:8080.


Compile the war file using sbt package. Then, run the war file as you would with any other J2EE application.
Currently, KioskWeb relies solely on ergo-appkit and utilizes the public explorer for posting transactions, thus eliminating the need for a local running Ergo node.
Appkit handles the signing process, replicating a large part of the Ergo node wallet's functionality locally, as both are JVM-based.
KioskWeb provides a "multi-tenant" environment as each URL corresponds to a private instance of the script environment and box storage. This setup allows you to bookmark a URL and revisit it later to find your declared variables and boxes intact. Unless someone has the same URL, they won't be able to view or modify your environment.

### Usage
Establish the environment for use in ErgoScript. This environment consists of a map of (key, value) pairs, with keys referenced within the ErgoScript code and set in the boxes' registers.


Define one or more boxes using ErgoScript code, including some registers if necessary.


Generate and send a transaction containing certain boxes predefined in the previous step.
The final output will be the transaction ID and the request made to the Ergo node's API.
