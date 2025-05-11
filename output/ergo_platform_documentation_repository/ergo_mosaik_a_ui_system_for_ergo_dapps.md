# Ergo Mosaik: A UI system for Ergo dApps
Source: docs/dev/stack/mosaik/tutorial3.md
Generated: 2025-05-11

## Summary
# Ergo Mosaik: A UI system for Ergo dApps

## 3: Processing data

In Part 2 of this tutorial series for Ergo Mosaik, we learned how to define the first simple UI for a dApp that can be shown within Wallet applications (and by using the Mosaik web executors in web browsers as well).

! [Mosaik 1](../../../assets/img/mosaik/tutorial3-1.png)

So far, we have seen how to show a card with a label and a button and how to run actions within Mosaik. I recommend you to take a look at the view elements demo again: Start the backend-demo-kotlin subproject from the mosaik repository and start the desktop debugger


```
    ./gradlew backend-demo-kotlin:bootRun
    ./gradlew desktop-demo:run
```


Then navigate to localhost:8080 on the desktop demo. Check out all the sub screens to get a feeling of how much is provided by Mosaik. Every page has a GitHub link at the top that brings you to the source code.

## Keywords
ergo, mosaik, system, dapps, processing, datum, part, series, dapp, wallet, application, executor, browser, tutorial3, 1.png, card, label, button, action, look

## Content
### 3: Processing data
In Part 2 of this tutorial series for Ergo Mosaik, we learned how to define the first simple UI for a dApp that can be shown within Wallet applications (and by using the Mosaik web executors in web browsers as well).
So far, we have seen how to show a card with a label and a button and how to run actions within Mosaik. I recommend you to take a look at the view elements demo again: Start the backend-demo-kotlin subproject from the mosaik repository and start the desktop debugger
./gradlew backend-demo-kotlin:bootRun
    ./gradlew desktop-demo:run
Then navigate to localhost:8080 on the desktop demo. Check out all the sub screens to get a feeling of how much is provided by Mosaik. Every page has a GitHub link at the top that brings you to the source code. Use this to learn how to describe the view elements in the code.
There is also an overview of available actions. Most actions are much like the showDialog action we already learned about: openBrowser, copyToClipboard etc work quite similar.
There are some actions that are more complex. Some enable Mosaik to have real interaction and to process data with your backend, namely backendRequest() and changeView(). Some others allow initiating a blockchain interaction, namely ErgoPay and ErgoAuth. We’ll take a look at the former ones now.

##### Process data with backendRequest
backendRequest() is an action that executes a POST request to your backend containing all input values of the current screen and expects a response with an action to run subsequently. This enables you to write complex logic in your backend resulting in different outcomes for the Mosaik app user. Your logic can operate on input values by the user. To have any input values defined, we need to add an input view element on our current screen. We start with a simple text input field. Open your MosaikController from last time and add it to your card:
```
card {
   column(Padding.DEFAULT) {
       label("Hello Ergo world!", LabelStyle.HEADLINE2)
box(Padding.HALF_DEFAULT)


   // this is new - begin


   textInputField("inputId", "Enter your name")

   box(Padding.HALF_DEFAULT)


   // this is new - end

   button("Click me") {
       onClickAction(showDialog("You clicked the button.", "myaction"))
   }
}
}
```
Start your Spring server process and navigate to your app in the desktop debugger. We can observe two things: First, unsurprisingly, is that the text input field is shown and ready for input. The second observation is less obvious and perhaps not expected: The debugger shows the current values for inputs on the right-hand side above the JSON sources with validity information:
When there is nothing entered (like in the screenshot above), the value for “inputId” is “null” which is valid. Enter something. You will see the value reflected and the type switches to String.
What is this validity? On many input types, you can add some properties defining restrictions on which inputs are valid. For example, we can define that only names with a length of 3 to 10 characters are valid by changing our app code like this:
textInputField("inputId", "Enter your name") {
   minValue = 3
   maxValue = 10
}
Restart the app server and reload the app. You will now see that the text input field will indicate invalid inputs, and the desktop debugger will report them as invalid.
The validit...

##### Alter the screen content with changeView()
changeView() is an action that contains a new mosaikView view content to attach it to the current screen. A view content is what you already delivered with your first main screen: it is an object holding a list of actions, and a root view element.
Excursus: View element, view group, view content
We already know all of these objects, but to make sure no one gets confused, we list a clarification definition here.
A view element is a basic element in a Mosaik view, like a label or a button.
A view group is a special view element containing other view elements, like Box, Column, Row, Card.
A view content defines the state of what Mosaik shows for your app. It is made up of is a root view element and a list of actions (which can be empty). Usually, the root view element should be a view group - otherwise, the screen would look very boring.
The behavior of changeView() action needs some more explanation regarding how it actually affects existing screen content:
the new actions defined by the view content of the changeView() action are added to the existing set of actions. (If any of the new actions’ IDs equal an ID of an already defined action, the new action replaces the existing one.)
the view root of the view content of the changeView() action will replace an existing view with the same id. If no view is found, or if the view root does not have an ID, the complete view tree is replaced
This behavior allows to alter the entire screen, or only change some single view elements.
To demonstrate this, let’s use our existing screen, but instead of showing a message box when a name was submitted, we change the title of the screen to show the name.
We will give the full code here and explain the annotated changes below:
```
@RestController
@CrossOrigin
class MosaikAppController {
   @GetMapping("/")
   fun getMainPage(): MosaikApp {
       return mosaikApp(
           "First Mosaik App", // app name shown in executors
           1 // the app version
       ) {
           // def...
