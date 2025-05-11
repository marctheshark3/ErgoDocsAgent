# Features
Source: docs/dev/stack/appkit/tutorial.md
Generated: 2025-05-11

## Summary
---
tags:
  - Java
  - Tutorial
---

## Features

[Ergo Appkit](https://github.com/aslesarenko/ergo-appkit) is a library for polyglot development of Ergo Applications based on [GraalVM](https://www.graalvm.org/). GraalVM has many [great use cases](https://medium.com/graalvm/graalvm-ten-things-12d9111f307d). Expanding on that, in this article, we will go through some of the Appkit features inherited from GraalVM and take you step-by-step in learning how to take advantage of them. ### Example Scenario

We will create a simple console application (called [FreezeCoin](https://github.com/aslesarenko/ergo-appkit-examples/blob/master/java-examples/src/main/java/org/ergoplatform/appkit/examples/FreezeCoin.java)) in Java which uses the Appkit library. By using Appkit, we will be able to easily send a new transaction to an Ergo node programmatically.

## Keywords
java, tutorial, feature, ergo, appkit](https://github.com, appkit, library, development, applications, graalvm, cases](https://medium.com, things-12d9111f307d, article, step, advantage, example, scenario, console, application, blob

## Content
### Features
Ergo Appkit is a library for polyglot development of Ergo Applications based on GraalVM. GraalVM has many great use cases. Expanding on that, in this article, we will go through some of the Appkit features inherited from GraalVM and take you step-by-step in learning how to take advantage of them.

#### Example Scenario
We will create a simple console application (called FreezeCoin) in Java which uses the Appkit library. By using Appkit, we will be able to easily send a new transaction to an Ergo node programmatically. The
transaction will transfer a given amount of Erg into a new box protected by the following Ergo contract written in ErgoScript (see this introduction and more advanced examples to learn more about ErgoScript).
java
// Freezer Contract
{ 
  // Parameters
  // freezeDeadline: Int - some future block number after which the box can be spent
  // ownerPk: SigmaProp - public key of the new box owner
  sigmaProp(HEIGHT > freezeDeadline) && ownerPk
}
In short, a box (and therefore the funds within the box) are locked under a contract (or script) on the Ergo blockchain. In order for the box to be spent, the contract must evaluate to be true. Thus the individual who wishes to spend the box must ensure that the contract evaluates to true based on the encoded logic within it.
Our Freezer contract above checks the following conditions before allowing the box to be spent:
The current block number of the Ergo blockchain (aka blockchain HEIGHT) is 
greater than the specified deadline


The spending transaction must be signed by the owner of the secret key
corresponding to the ownerPk public key.
The first condition forbids anyone from spending the box before the Ergo
blockchain grows to the given height. Because new blocks on the blockchain are mined approximately every 2 minutes on average, using the current
blockchain height, it is easy to define any duration of delays we wish, such as 1 day, 1 week, or 1 month. (i.e. (60 / 2) * 24 * 7 = 5040, which is the # of blocks per week).
We will now be going in-depth on how we can take this Freezer Contract and integrate it with the Apkit library in order to create the FreezeCoin console application so that anyone and everyone can choose to freeze their coins if they so wish. (Granted, this contract/dApp is not useful; however, it is an...

#### Java Ergo App Development
Appkit aims to provide a set of interfaces that can be used idiomatically in Java. You will feel right at home using Appkit if you are a Java veteran.
Please follow the setup instructions for GraalVM and Appkit if you wish to reproduce the examples below.
To use Appkit in our Java implementation of FreezeCoin, we must add the following dependency in the gradle file
kotlin
dependencies {
    implementation("org.ergoplatform", "ergo-appkit_2.12", "3.1.0", "compile")
    ...
}
Furthermore, at runtime, Appkit/our application needs to connect with an Ergo Node via REST API. Often,
the node will be running locally and made available at http://localhost:9052/. This is the standard scenario for anyone who has set up a full-node by following these
instructions and is using the default configuration.
Henceforth we will assume that you have set up and started your Ergo Node so that it is available for testing of the application.
Next, our application will need to know how to be able to connect to our local running node, in addition to other various settings, in order to function properly. We will use a JSON file with the following
configuration parameters which our FreezeCoin app will load at startup.
freeze_coin_config.json:
JSON
{
  "node": {
    "nodeApi": {
      "apiUrl": "http://localhost:9052/",
      "apiKey": "put your secret apiKey generated during node setup here"
    },
    "wallet": {
      "mnemonic": "the mnemonic key used to initialize or restore the wallet of the node",
      "password": "the password you chose to protect the wallet",
      "mnemonicPassword": "the password you chose to protect the mnemonic"
    },
    "networkType": "TESTNET"
  },
  "parameters": {
    "newBoxSpendingDelay": "30",
    "ownerAddress": "3WzR39tWQ5cxxWWX6ys7wNdJKLijPeyaKgx72uqg9FJRBCdZPovL"
  }
}
Here apiKey is the secret key required for API authentication, which can be
acquired as described
here.
Your mnemonic is the secret phrase obtained during setup of a new
wallet.
How our...

#### Low-footprint, Fast-startup Ergo Applications
As you may know, using Java for short-running processes has a lot of drawbacks.
Applications tend to suffer from long startup times and relatively high memory usage.
Let's run FreezeCoin using the time command to
get the real (wall-clock elapsed time). It takes the entire program to run from
start to finish. We use the -l flag to print the memory usage as well.
shell
$ /usr/bin/time -l java -cp build/libs/appkit-examples-3.1.0-all.jar \
   org.ergoplatform.appkit.examples.FreezeCoin 1000000000
...
       4.97 real         8.41 user         0.69 sys
 513703936  maximum resident set size
         0  average shared memory size
         0  average unshared data size
         0  average unshared stack size
    125010  page reclaims
      1216  page faults
         0  swaps
         0  block input operations
         0  block output operations
        13  messages sent
        86  messages received
         1  signals received
      2384  voluntary context switches
     17409  involuntary context switches
As seen above, this tiny application took 2 parallel threads almost 4
seconds to run. Most of that time can be attributed to the JVM startup and
the background JIT compiler running. This is quite a sub-par performance, and we know we can do a lot better.
Luckily, GraalVM provides us with the perfect solution.
We can solve this inherent issue with the JVM by compiling the Java code
ahead of time into a native executable image via GraalVM. This skips over the need to use the Java just-in-time compiler
at runtime.
The experience for us (the developer using GraalVM) is quite similar to a conventional compiler like GCC. Note,
we may need to run ./gradlew clean shadowJar first.
shell
$ ./gradlew clean shadowJar
$ native-image --no-server \
 -cp build/libs/appkit-examples-3.1.0-all.jar\
 --report-unsupported-elements-at-runtime\
  --no-fallback -H:+TraceClassInitialization -H:+ReportExceptionStackTraces\
   -H:+AddAllCharsets -H:+AllowVMInspection -H:-RuntimeAssertions\
   --al...

#### Develop Ergo Applications in JavaScript, Python, Ruby
GraalVM supports so-called polyglot programming in which different components of
an application can be developed using the most suitable language and then seamlessly combined together at runtime. In this way, a unique library written in, say, Java can be used in a node.js application written in JavaScript, for example.
To support polyglot programming GraalVM platform has high-performance implementations of popular languages. We are going to take advantage of this for our FreezeCoin example project to show you how easy this is to use your preferred language.
Before running the examples below (in JavaScript, Python and Ruby), please make sure that you have the Java version of FreezeCoin working locally in order to ensure everything is set up correctly.

##### JavaScript
GraalVM can run JavaScript and Node.js applications out of the box. It is compatible with the ECMAScript 2019
specification.
Additionally, js and node launchers accept special --jvm and --polyglot command-line options which allow JS scripts to access Java objects and classes.
Given that being the case, a JS implementation of FreezeCoin can be easily written using the Appkit.
API interface.
Please see the full source code of FreezeCoin JS implementation
for details.
The following command uses the node launcher to execute the FreezeCoin.js script.
shell
$ node --jvm --vm.cp=build/libs/appkit-examples-3.1.0-all.jar \
  js-examples/FreezeCoin.js  1000000000
Note, the paths in the command are relative to the root of
ergo-appkit-examples project directory.

##### Python
GraalVM can run Python
scripts, thoughthe Python implementation is still experimental (see also
compatibility section for details).
Python example of FreezeCoin can be executed using the following command
shell
$ graalpython --jvm --polyglot --vm.cp=build/libs/appkit-examples-3.1.0-all.jar \
   python-examples/FreezeCoin.py 1900000000

##### Ruby
GraalVM can run Ruby scripts using TruffleRuby implementation, which is however still experimental (see also compatibility section for details).
TruffleRuby aims to be fully compatible with the standard implementation of Ruby, MRI, version 2.6.2
Ruby example of FreezeCoin can be executed using the following command
shell
$ truffleruby --polyglot --jvm --vm.cp=build/libs/appkit-examples-3.1.0-all.jar \
    ruby-examples/FreezeCoin.rb 1900000000

#### Ergo Native Shared Libraries
Another great benefit of GraalVM is that we can compile Java classes down into a native shared library instead of an executable.
To do this, we declare one or more static methods as the @CEntryPoint.
```Java
public class FreezeCoin {
    ...
     /*
     * Entry point callable from C which wraps {@link FreezeCoin#sendTx}
     /
    @CEntryPoint(name = "sendTx")
    public static void sendTxEntryPoint(
            IsolateThread thread,
            SignedWord amountToSendW,
            CCharPointer configFileNameC,
            CCharPointer resBuffer, UnsignedWord bufferSize) throws FileNotFoundException {
        long amountToSend = amountToSendW.rawValue();
        // Convert the C strings to the target Java strings.
        String configFileName = CTypeConversion.toJavaString(configFileNameC);
        String txJson = sendTx(amountToSend, configFileName);
// put resulting string into the provided buffer
    CTypeConversion.toCString(txJson, resBuffer, bufferSize);
}  
...
}
```
We can then compile down to a shared library and an automatically generated header file. Notice the use of the --shared option.
```shell
$ native-image --no-server \
 -cp build/libs/appkit-examples-3.1.0-all.jar\
 --report-unsupported-elements-at-runtime\
  --no-fallback -H:+TraceClassInitialization -H:+ReportExceptionStackTraces\
   -H:+AddAllCharsets -H:+AllowVMInspection -H:-RuntimeAssertions\
   --allow-incomplete-classpath \
    --enable-url-protocols=http,https 
    --shared -H:Name=libfreezecoin -H:Path=c-examples
$ otool -L c-examples/libfreezecoin.dylib 
c-examples/libfreezecoin.dylib:
  .../c-examples/libfreezecoin.dylib (compatibility version 0.0.0, current version 0.0.0)
  /usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1252.50.4)
  /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation (compatibility version 150.0.0, current version 1455.12.0)
  /usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.11)
```
Now we ca...

## include
int main(int argc, char argv) {
  graal_isolate_t isolate = NULL;
  graal_isolatethread_t thread = NULL;
if (graal_create_isolate(NULL, &isolate, &thread) != 0) {
    fprintf(stderr, "graal_create_isolate error\n");
    return 1;
  }
char * configFileName = "freeze_coin_config.json";
// get amountToSend from cmd args and call transaction creation
  long amountToSend = atol(argv[1]);
  char result[1024 * 16];
  sendTx(thread, amountToSend, configFileName, result, sizeof(result));
// print out serialized result
  printf("%s\n", result);
if (graal_detach_thread(thread) != 0) {
    fprintf(stderr, "graal_detach_thread error\n");
    return 1;
  }
  return 0;
}
```
We can compile this with our standard system tools and easily run our executable (set LD_LIBRARY_PATH=. on Linux).
shell
$ clang -Ic-examples -Lc-examples -lfreezecoin c-examples/freezecoin.c -o call_freezecoin
$ otool -L call_freezecoin
$ DYLD_LIBRARY_PATH=$GRAAL_HOME/jre/lib ./call_freezecoin 1000000000

#### Debugging Your Polyglot Ergo Application
You can debug JS, Python and Ruby in IntelliJ, but if, for some reason, this doesn't work for you or fit with your preferred editor, GraalVM offers another option.
All of the GraalVM languages (except for Java) are implemented using the common Truffle framework.
Truffle allows for tooling like debuggers to be implemented once and be available for all supported languages.
As such, we can run our program with the flag --inspect, which will give us a link to open in Chrome and will pause the program in the debugger.
shell
$ ruby --polyglot --jvm --inspect --vm.cp=build/libs/appkit-examples-3.1.0-all.jar \
    ruby-examples/FreezeCoin.rb 1900000000
Debugger listening on port 9229.
To start debugging, open the following URL in Chrome:
    chrome-devtools://devtools/bundled/js_app.html?ws=127.0.0.1:9229/30c7da1e-7558a47d09b
...
From here, we can set breakpoints and continue execution. When it breaks, we’ll see values of the variables, can continue again until the next breakpoint, and do everything we've come to expect from debuggers.

#### Conclusions
And with all of that said and done, we see just how easy it is to use Appkit to develop Ergo Applications. Appkit relies on the same core libraries which were used in implementing the Ergo consensus protocol. These libraries include the ErgoScript compiler, cryptography, byte code interpreter, data serialises and the other core components. Using GraalVM, we can reuse these tried and tested components in different application contexts without any modification or rewriting them ourselves.
No matter if you are using Java, JavaScript, Python or Ruby, you can take advantage of Appkit with GraalVM to drastically simplify the process of interacting with the Ergo blockchain while creating native-running (d)Apps.

#### References
Ergo Site
Ergo Sources
Ergo Appkit
Ergo Appkit Examples
GraalVM
