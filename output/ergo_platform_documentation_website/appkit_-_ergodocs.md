# AppKit - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/stack/appkit/](https://docs.ergoplatform.com/dev/stack/appkit/)
Generated: 2025-05-11

## Summary
Ergo Appkit is a library for polyglot development of Ergo Applications based on GraalVM. It is a thin wrapper around core components provided by the ErgoScript interpreter and Ergo protocol implementations which are written in Scala. It is published on maven repository and cross-compiled to both Java 7 and Java 8+ jars. AppKit provides methods for the following: Using Appkit, Ergo applications can be written in one of the languages supported by GraalVM (i.e. Java, JavaScript, C/C++, Python, Ruby, R) and using this library, applications can communicate with Ergo nodes via unified API and programming model provided by Appkit. In addition, Appkit based Ergo applications can be compiled into native code using native-image ahead of time compiler and then executed without Java VM with very fast startup time and lower runtime memory overhead compared to a Java VM.

## Keywords
ergo, appkit, library, development, applications, graalvm, wrapper, core, component, ergoscript, interpreter, protocol, implementation, scala, maven, repository, java, method, following, application

## Content
## Appkit#
Ergo Appkit is a library for polyglot development of Ergo Applications based on GraalVM.
It is a thin wrapper around core components provided by the ErgoScript interpreter and Ergo protocol implementations which are written in Scala. It is published on maven repository and cross-compiled to both Java 7 and Java 8+ jars.
AppKit provides methods for the following:
Fetch data from Ergo Explorer API
Interact with Ergo Node, both public and private methods
Build transactions and sign them
Helper methods to handle cryptographic like calculating PK addresses from secrets
Using Appkit, Ergo applications can be written in one of the languages supported by GraalVM (i.e. Java, JavaScript, C/C++, Python, Ruby, R) and using this library, applications can communicate with Ergo nodes via unified API and programming model provided by Appkit. In addition, Appkit based Ergo applications can be compiled into native code using native-image ahead of time compiler and then executed without Java VM with very fast startup time and lower runtime memory overhead compared to a Java VM. This is an attractive option for high-performance, low-latency microservices.

### Tutorials#
General Example
ð AppKit By ExampleFollow this example to create and programmaticaly send a transaction.
ErgoPay Example
Gradle

### Videos#
AppKit by Example

### Code examples#
Appkit Examples
Testing Ergo Contracts Off-chain

### How-to Guides#
Ergo Android application that demonstrates how Ergo Appkit can be used to develop Ergo applications running on Android.

### References#
ErgoTool | A Command Line Interface for Ergo based on Appkit and GraalVM native-image. Read the introduction and overview.
