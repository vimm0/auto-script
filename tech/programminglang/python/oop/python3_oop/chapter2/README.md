##### Objects in Python

Initializing the object
- initialization method
    - special name: __init__.
- constructor
    - __new__
    - accepts exactly one argument, the class that is being constructed (it is called before the object is constructed, so there is no self argument
- To write API documentation: docstrings
- Modules and packages 
    - single file in our small program is a module.
    - Avoid * import
        - `from database import *`
    - `from database import Database as DB`
    - `from database import Database`
    - `from database import Database, Query`
    -  **package** is a collection of modules in a folder.
    -  there are two ways of importing modules: 
        - absolute imports
        - relative imports
-  __name__ special variable
-  Classes can be defined anywhere
- if a method is meant for internal use only, prefix an attribute or method with an underscore character: _. 
- name mangling 
- **top-down design**, when you work out the different interactions and describe how they should work before actually implementing what they do
- **bottom-up design**, implements details first and then ties them all together

Tips and Tricks:
- Whenever the Python interpreter reads a source file, it does two things:
    - it sets a few special variables like __name__, and then
    - it executes all of the code found in the file.
    - https://stackoverflow.com/questions/419163/what-does-if-name-main-do
- Excercise: 
    - Note Book
    - TO DO application
