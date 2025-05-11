# Web UI - ErgoDocs
Source: [https://docs.ergoplatform.com/dev/stack/mosaik/tutorial5/](https://docs.ergoplatform.com/dev/stack/mosaik/tutorial5/)
Generated: 2025-05-11

## Summary
Welcome back to the Ergo Mosaik tutorial series! In the previous parts of this series, we already implemented a full-fledged Mosaik app for sending ERG that is working 
smoothly when launched in a Mosaik executor like the Ergo Wallet app or the Mosaik desktop debugger. But there are people out there without Mosaik executing wallet apps, 
or people using the app but not being aware that they can use Mosaik dApps within their wallet app, or people preferring to have a clear separationâ¦ long story short, 
we need to keep care of web browsers, as they are the go-to app for most users to visit an URL or host name. This tutorial will show you how to handle two use cases: Letâs focus on 1) first. Letâs go back to our tutorial app and start up the Spring Boot process.

## Keywords
ergo, mosaik, series, part, executor, wallet, desktop, debugger, people, dapps, separationâ, story, care, browser, user, host, name, tutorial, case, letâs

## Content
### Part 5: The Web#
Welcome back to the Ergo Mosaik tutorial series! In the previous parts of this series, we already implemented a full-fledged Mosaik app for sending ERG that is working 
smoothly when launched in a Mosaik executor like the Ergo Wallet app or the Mosaik desktop debugger. But there are people out there without Mosaik executing wallet apps, 
or people using the app but not being aware that they can use Mosaik dApps within their wallet app, or people preferring to have a clear separationâ¦ long story short, 
we need to keep care of web browsers, as they are the go-to app for most users to visit an URL or host name.
This tutorial will show you how to handle two use cases:
You only want your Mosaik app to be used from within wallet apps. But you want web browsers visiting your app URL to show a nice site explaining the users to open the app URL from within a wallet app
You want your Mosaik app to run within a web browser
Letâs focus on 1) first.

##### Show an informational page in web browsers visiting your Mosaik app#
Letâs go back to our tutorial app and start up the Spring Boot process. We know that our Mosaik app is living on http://localhost:8080/ now, 
and opening it in the desktop debugger works as great as expected. However, when we open up the app in a web browserâ¦we only get to see the json output that is our 
serialized app. Letâs do this better!
There is no way in getting web browsers understanding what a Mosaik app is, so we use a simple trick to achieve what we want: We move the Mosaik app away from the URL, 
and instead serve HTML content we want the user to see there. But we leave a hint for Mosaik executors where to find the actual Mosaik app.
Moving the Mosaik app is easy. Letâs open MosaikAppController and change the annotation for getMainPage:
@GetMapping("/firstapp")
fun getMainPage(): MosaikApp {...}
We also need to change the annotation for userEnteredName:
@PostMapping("/firstapp/enteredName")
fun userEnteredName(@RequestBody values: Map<String, Any?>) = â¦
Now we need to define new content for the main page.
Create a new directory âstaticâ in the src/main/resources directory and create a file ânobrowser.htmlâ with the following content:
<html>
<head>
   <link rel="mosaik" href="firstapp">
</head>
<body>
Please navigate to this page with a Mosaik executor application.
</body>
</html>
This is the content to be served. The important part for Mosaik executors is the link <rel=âMosaikâ â¦> tag, while all other content is for web browsers to show.
We tell Spring to serve this file for the main page with the following addition to MosaikAppController.kt.
@GetMapping("/")
fun browserHintPage(): ModelAndView {
   return ModelAndView("nobrowser.html")
}
And thatâs it! After restarting Spring, web browsers show a hint message when visiting localhost:8080, while Mosaik executors automatically load the linked Mosaik app.
Of course, you donât need to show an ugly hint message, but can instead serve your main web page here.
You can find this vers...

##### Run your Mosaik app in web browsers#
Mosaik apps are platform agnostic and can be executed in wallet applications on different operating systems and architectures. There is also a Mosaik executor 
available to run your apps from within a web browser. It is not a browser plugin, but instead an interactive website consisting only of a single html page, a 
single Js file and a configuration file that you host on your web site. The configuration file specifies where the web executor loads your Mosaik app from, so 
you can reuse your Mosaik apps for the wallet apps here - in most cases without a change.
Before we do the necessary steps to run our apps with the web executor, some words on what to expect and what it is meant for:
Since Mosaik is platform agnostic and meant to be used for wallet plugins, the Mosaik UI defines certain elements and its placements in a view hierarchy. There 
is no absolute way to define how elements look like, so it is expected that buttons or icons do not look the same when run with another executor. Hence, Mosaik 
will never support pixel-pefect element positioning or coloring elements in all available colors. If you need this, Mosaik web is not for you, you need to 
develop your own web UI.
However, Mosaik web is designed to behave the same as Mosaik executed in wallet applications. Your apps will behave the same without a code change on your side, and
you can publish your app as a web app with practically no effort regarding web development.
Now letâs start using the web executor. You can find it on its Git repository https://github.com/MrStahlfelge/mosaik-kt-js 
under releases as a zip file. In most cases, it is not needed that you build it yourself - this is only needed if you need the latest working version, or if you want to 
customize the colors. See the README on the repository for infos on this.
Download the latest zip file. It contains the three files mentioned above. You can host these files on any static web hosting provider so that it integrates well into 
your e...

##### Add ErgoPay connect wallet support#
Connecting a wallet with ErgoPay needs establishing a channel back from the wallet app to the Mosaik web executor, thatâs why you need to add two new API endpoints 
and a data holder service to your Spring controllers and configure these two endpoints in web executorâs mosaikconfig.json.
For simplicity, the actual code is not shown here as it is some boilerplate. If you read through it, it is pretty easy to understand that it handles the following: 
Endpoint A is called continuously by the web executorâs connect wallet screen to check if the user already connected. Endpoint B is an ErgoPay endpoint connected 
from the wallet app when the user connects. It saves the userâs wallet address in a temporary map for endpoint A to pick up.
The two endpoints are implemented in UserSessionController and the temporary wallet address map is implemented in UserSessionService. Feel free to copy them as is 
in your own project. You can find them here:
https://github.com/MrStahlfelge/mosaik-tutorial-series/tree/fba56d65e8c8a01821ecb1c56037bc5dfa8a652a/src/main/kotlin/com/example/ergomosaik/mosaikapp
For the web executor to know where to connect to, the mosaikconfig.json file needs to be edited as follows:
{
 "starturl": "firstapp",
 "chooseWalletErgoPay": {
   "getAddressForSessionUrl": "http://127.0.0.1:8080/getUserAddress/#RID#",
   "ergoPaySetAddressUrl": "ergopay://127.0.0.1:8080/setAddress/#RID#/#P2PK_ADDRESS#"
 },
 "routes": {
   "send": "http://127.0.0.1:8080/sendfunds"
 }
}
Please note: Since we have a local address (127.0.0.1) here, the connection wonât work when using a mobile device to read the QR code. 
It works when using a local network IP.

##### Conclusion#
In the five parts of this tutorial series, youâve learned what Mosaik is about and how to write Mosaik apps that run as wallet application 
plugins and on the web. Mosaik is still a framework being worked on. To proceed, we need you, the developers, to jump on. What is not working 
well yet, where do the existing view elements have shortcomings? Give us feedback by DM or on the Ergo discord in #dev-support
Happy coding!
