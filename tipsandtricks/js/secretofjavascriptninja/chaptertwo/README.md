# Building the page at runtime
> GUI application carried out two steps:
1. Page Building
2. Event Handling

1. Page Building Phase
* Parsing the HTML and building the Document Object Model ( DOM )
* Executing JavaScript code
##### GLOBAL OBJECTS IN JAVASCRIPT
* window -> document

2. Event handling
* The browser checks the head of the event queue.
* If there are no events, the browser keeps checking.
* If there’s an event at the head of the event queue, the browser takes it and exe-
cutes the associated handler (if one exists). During this execution, the rest of
the events patiently wait in the event queue for their turn to be processed.

##### EVENTS ARE ASYNCHRONOUS
* Browser events, such as when a page is finished loading or when it’s to be unloaded
* Network events, such as responses coming from the server (Ajax events, server-
side events)
* User events, such as mouse clicks, mouse moves, and key presses
* Timer events, such as when a timeout expires or an interval fires

##### Registering event handlers
* By assigning functions to special properties
```
window.onload = function(){};
```
* By using the built-in addEventListener method
```
document.body.onclick = function(){};
```

##### Facts
* When browser find script element, the browser pauses the DOM construction from HTML code and starts exe-
cuting JavaScript code.
