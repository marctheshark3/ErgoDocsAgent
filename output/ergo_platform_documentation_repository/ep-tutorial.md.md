# ep-tutorial.md
Source: docs/dev/wallet/payments/ergopay/ep-tutorial.md
Generated: 2025-05-11

## Summary
---
tags:
  - Tutorial
  - dApp Development
---

### What we’ll do in this tutorial This tutorial will focus on implementing the backend server-side for ErgoPay, building and preparing transactions. We’ll use [Spring Boot](https://spring.io/) to implement a simple ErgoPay REST API. Spring has the following benefits why we’ve chosen it here: It’s JVM-based, and [ergo-appkit](https://github.com/ergoplatform/ergo-appkit), one of Ergo’s SDKs, is also JVM-based. It’s easy and boilerplate-free, tons of tutorials and information is available, it runs on your local machine with ease.

## Keywords
tutorial, dapp, development, server, side, ergopay, building, transaction, spring, boot](https://spring.io/, rest, benefit, ergo, ergoplatform, appkit, boilerplate, information, machine, ease, service

## Content
#### What we’ll do in this tutorial
This tutorial will focus on implementing the backend server-side for ErgoPay, building and preparing transactions. We’ll use Spring Boot to implement a simple ErgoPay REST API. Spring has the following benefits why we’ve chosen it here: It’s JVM-based, and ergo-appkit, one of Ergo’s SDKs, is also JVM-based. It’s easy and boilerplate-free, tons of tutorials and information is available, it runs on your local machine with ease. There are both free and paid services to get the application deployed to the public.
Of course, you are free to use any other programming language and framework you are experienced with and adapt the concepts outlined here.
We won’t cover the implementation of the UI side of your dApp here, but the code of the ErgoPay showcase dApp is open-sourced and of course, you can use it as you wish.

#### Starting your Spring Boot project
Spring provides an IDE, but it is not needed so you can work with the IDE of your choice. You’ll also need to have a Java Development Kit installed. If you don’t have one installed yet, use OpenJDK on Linux or install Adoptium on Windows. Head over and generate a fresh Spring Boot project with the initializr. Change the information in the form as you like, for this tutorial you only need to add the “Spring web” dependency. If you don’t use Eclipse I would also recommend switching to “Gradle project”. Download and extract the generated project and open it with your IDE.
You can start your application with Gradle by typing
bash
./gradlew bootRun // MacOS/Linux
gradlew bootRun   // Windows
This prints out that the server is running on http://localhost:8080/ now. But as we didn’t do something, it’s not of much use, so you can stop it with Ctrl-C.
To get more familiar with how a REST API is implemented using Spring, you should now follow the Spring Quick Start and implement the Hello World endpoint before proceeding here.

#### Adding an ErgoPay request endpoint
Now it is time to build your first ErgoPay request endpoint. Such an endpoint is a GET REST API method that returns an “ErgoPayResponse” in its response body. ErgoPayResponse is a JSON-based data interchange format between a dApp and a wallet app and is described in Ergo Improvement Proposal 0020.
At first, we need to declare this response data type as a Java Object.
Add the following file to your Spring Boot project:
```java
package org.ergoplatform.ergopay;
import com.fasterxml.jackson.annotation.JsonInclude;
public class ErgoPayResponse {
    @JsonInclude(JsonInclude.Include.NON_NULL)
    public String message;
    @JsonInclude(JsonInclude.Include.NON_NULL)
    public Severity messageSeverity;
    @JsonInclude(JsonInclude.Include.NON_NULL)
    public String address;
    @JsonInclude(JsonInclude.Include.NON_NULL)
    public String reducedTx;
    @JsonInclude(JsonInclude.Include.NON_NULL)
    public String replyTo;
enum Severity { NONE, INFORMATION, WARNING, ERROR }
}
```
To send this back as the response body of an endpoint, simply declare this new class as the return type of a RestController method. Spring Boot will automatically handle serialization to JSON format. Such a method could be declared as follows:
java
@GetMapping("/ergopay/")
public ErgoPayResponse ergoPayError() {
     ErgoPayResponse response = new ErgoPayResponse();
     response.messageSeverity = ErgoPayResponse.Severity.ERROR;
     response.message = "Nothing implemented yet.";
     return response;
}
This is already a valid ErgoPay response and endpoint. It does not serve a transaction, but will only present an error message to the users in their wallet apps.
If you start your Spring Boot application now and open http://localhost:8080/ergopay in your local web browser, you’ll see the JSON response in your browser.
Use the endpoint from the wallet application
It’s all good to see the response in your browser, but of course you want to see this in a wallet app. If you have a mobile device with th...

#### Building and reducing a transaction
The spice of ErgoPay is building a transaction on the dApp side and let the user sign it. For this, ErgoPayResponse has a field “reducedTx”. But how to build a transaction and “reduce” it? For this, we need to integrate the Ergo SDK into our Spring Boot project. To pull in the SDK, edit the build.gradle file of your Spring project and add the following line in the dependencies section, right below the spring-boot-starter-web dependency declaration:
```java
dependencies {
   implementation 'org.springframework.boot:spring-boot-starter-web'
*  implementation 'org.ergoplatform:ergo-appkit_2.11:4.0.6'
testImplementation 'org.springframework.boot:spring-boot-starter-test'
}
```
When this is done, you can add the following helper method that builds a transaction for sending a certain amount of nanoERG from “sender” to “recipient”:
```java
    // This function takes in boolean, long, address of sender and address of recipient
    // and returns a reduced transaction object.
    private ReducedTransaction getReducedSendTx(boolean isMainNet, long amountToSend, Address sender, Address recipient) {
        // Determine the network type
        NetworkType networkType = isMainNet ? NetworkType.MAINNET : NetworkType.TESTNET;
        // Create a REST API client with default explorer url
        return RestApiErgoClient.create(
                getDefaultNodeUrl(isMainNet),
                networkType,
                "",
                RestApiErgoClient.getDefaultExplorerUrl(networkType)
        ).execute(ctx -> {
            // Create a new Ergo contract with the recipient's Ergo address
            ErgoTreeContract contract = new ErgoTreeContract(recipient.getErgoAddress().script());
            // Create an unsigned transaction to put the given amount of funds to the contract
            UnsignedTransaction unsignedTransaction = BoxOperations.putToContractTxUnsigned(ctx,
                    Collections.singletonList(sender),
                    contract, amountToSend, Collecti...

#### Going further
Now it’s time to start experimenting with building other types of transactions.
Also check out the ErgoPay example server project — its ErgoPayController.java file defines some more endpoints: minting tokens, burning tokens, and spending a specific box.
You can also just use the getReducedSendTx method to issue payments on behalf of the user to yourself, for example as a payment service. The great thing is that you know the transaction id beforehand: every detail of the transaction is already known when the Reduced Transaction is built, and you can save this transaction id in your backend db and monitor the blockchain to observe when the payment was made to proceed with delivering the goods or services the user paid for.
You know enough now to build something like the token minter and box spender of the ErgoPay showcase app. For the token burner, we need one more feature: Connecting a wallet to the dApp UI.

#### Connect a wallet to your UI
Connecting a wallet is not needed in general, as you’ve seen: for a payment or minting a token, you don’t need to know the user’s wallet address to collect or validate the data from the user. It is enough to know the address when the transaction is built on request of the wallet app. But for specific use cases, you might need the wallet address more early: The showcase dApp ships a token burner example. For showing the list of owned tokens to choose from, connecting a wallet is needed before the actual transaction is built.
Indeed, we can obtain the address with all ErgoPay ingredients we already learned about. But we need to introduce some kind of session management on the dApp backend. Chances are high that you already have some kind of session running for the user. For example if your dApp is a web shop, you probably already store the items added to the cart.
But if you don’t have any type of session management running, we’ll implement the simplest kind of it now: every user of your dApp has a unique ID (“uuid”) that is randomly chosen by your frontend UI. This uuid is used as a session id. On the backend, we store a user’s P2PK address mapped to this id.
Our backend needs two API endpoints: one for the wallet app to send a user’s address to store it attached to the uuid, and one for the frontend UI to request if the user address is set.
The following two methods do this:
```java
    @GetMapping("/getUserAddress/{sessionId}")
    public String getUserAddress(@PathVariable String sessionId) {
        UserData userData = sessionService.getUserData(sessionId);
return (userData.p2pkAddress != null) ? userData.p2pkAddress : "";
}

@GetMapping("/setAddress/{sessionId}/{address}")
public ErgoPayResponse setAddress(@PathVariable String sessionId, @PathVariable String address) {
    UserData userData = sessionService.getUserData(sessionId);

    ErgoPayResponse response = new ErgoPayResponse();

    // check the address
    try {
        boolean isMainNet = isMainNetAddre...

#### Your dApp UI on the same device as the wallet app
We assumed that the user visits your dApp on a desktop and uses the wallet application on mobile, so we only talked about QR codes containing the ErgoPay URLs. This won’t work when users visit your dApp on the same device that the wallet app is running on — they simply can’t scan a QR code from the same device. Fortunately, you can simply show the ErgoPay URLs as a link for these users. If the user has a compatible wallet app installed, clicking or tapping such a link will open the wallet application processing the ErgoPay request.

#### Conclusion
You’ve learned to build an ErgoPay capable backend in this tutorial. You’ll find this as a full example on GitHub. It is also deployed on Heroku, a free hosting service for web apps that you can use to start off with your own projects.
