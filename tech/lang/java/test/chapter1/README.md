# Note

Java is a computer language that enforces an object-oriented programming model

Java is a programming language and computing platform first released by Sun Microsystems(Oracle now) in 1995

Java was created by a team lead by James Gosling

Java is a platform independent programming language that follows the logic of "Write once, Run anywhere"

Java can be used to create complete applications that may run on a single computer or can be distributed among servers and clients in a network

RECENT VERSION: Java 12 (2019)

## Java Features

- Simple
  Java is easy to learn and its syntax is quite simple, clean and easy to understand. The confusing and ambigurous concepts of C++ are either left out in java or they have been re-implemented in cleaner way
- Secure
  - Java can be used to develop virus-free systems
    - Java programs run inside virtual machine sandbox to prevent any activity from untrusted sources
    - no use of explicit pointers
    - does garbage collection
- Portable
  - can be run on any platform
- Distributed
  - RMI (Remote Method Invocation), EJB(Enterprise Java Bean) etc. are used for creating distributed application using java
  - Using this a program can call a method of another program running in some other computers in the network
- Object Oriented
- High Performance
  Although Java is interpreted language, it was designed to support "just-in-time" compilers, which dynamically compile bytecodes to machine code
- Robust
- Dynamic
  - Many objects are evaluated at run time and execution is carried out. For example: runtime polymorphism
- Multi-threaded
  - Thread is a task in a process/program
  - Muli-threading is multiple tasks running/executing at the same time.
  - This facility is provided by java so that many tasks can be executed at the same time

## In which sectors is java used

- Android Apps
  - All android applications are written in Java programming language, with Google's Android API, which is similar to JDK(Java Development Kit)
- Server Apps at financial services industry
  - Lots of global investment banks like citigroup, barclays, standard chartered and other banks use java for writing front and back office electornic trading system, writing settlement and confirmation systems, data processing projects and serveral others.
- Java Web Application
  - Many of government, healthcare, insurance, education, defence and serveral other deprtment, have their web application built in Java using servlets, JSP, structs, Spring MVC
- Embedded systems
  - java is platform where you only need 130kb memory to use java technology (on a smart card, sensor)
- Web Servers and Application Servers
  - Apache Tomcat, Simple, Jo!, Rimfaxe Web Server(RWS) and Project Jigsaw are web server space
  - Weblogic, WebSphere and Jboss EAP dominate commercial application server space
- Enterprise Application
  - Java Enterprise Edition(Java EE) is a popular platform that provide API and runtime environment for scripting and running enterprise softwares

## where is java used

- Scientific Application

  - java is the choice of many software developer for writing application involving scientific calculations and mathematical operations
    - These programs are generally considered to be fast and secure, have a higher degress of portability and low maintenance

- Big Data technologies
  - Hadoop and other big data technologies are also using java in one way or other
  - eg Apache kafka components API - producer and consumer are written in java
- Internet of things(IOT)
  - internet of things which is a way to blend hardware and software together to solve problems faced in real life.

## Java versions

- J2SE(standard edition): data types, for statemnt
- J2EE(enterprise edition): web application
- J2ME(micro edition): light in weight (for embedded system)

## Java Internals

- Java Virtual Machine (JVM)
  - JVM is the virtual machine that runs the java bytecode.
  - the JVM does not understand java source code, that is why you compile your _.java files obtain _.class files that contain the bytecodes understood by the JVM
  - The same bytecode give the same results make java a platform independent language(write once, run anywhere)

```code
java code(.java) -> Javac compiler -> byte code(.class) -> JVM -> any operating system
```

- Java Runtime Environment(JRE)
  -JRE provide the libraries, the JVM, and other components to run applets and applications written in the java programming language

  - JRE = JVM + Set of Libraries + Other Additional Files
  - The JRE does not contain tools and utilties such as compilers and debuggers for developing applets and application
  - JRE (JVM, set of libraries like rt.jar, etc, other files)

- Java Development Kit(JDK)
  - JDK is a superset of JRE, and contains everything that is in the JRE, plus tools such as the comilers and debuggers necessray for developing applets and applications
    - JDK = JRE + development tools
    - JDK = (JVM + set of libraries + other additional files) + development tools

![alt text](./images/deep-dive.png)
![alt text](./images/working.png)

`Public` keyword is an access modifier which represets visibility, it means it is visible to all

`class` keyword is used to declare a class in java

`void` is the return type of the method, it means it doesn't return any value

`static` is a keyword, if we declare any static, it is known as static method. The core advantage of static method is that there is no need to create object to invoke the static method.

`Sting[] args` is used for command line argument.

`main` represents statup of the program.

`System.out.Println` is used print statment.

Modifiers:
is a word or phrase or clause that describes, changes or modifies that meaning of another word or phrase in some way.

- access modifiers(Encapsulation)

  - java provides a number of access controll modifiers to set access levels of classes, variables, methods and contructors

    - default: visible to the package
    - public: visible to the world
    - private: visible to class only
    - protected: visible to the package and all subclass

- non-access modifiers
  - java provides a number of non-access modifiers to provide additional functionalities to a class, variable, method or constructor.
    - static
      - static modifier for calling methods and variables without an object to which it belong
    - final(constant)
      - final modifier for finalizing the implementation of classes, methods and variables
    - abstract(generic modifier without any funtionality of its own)
      - abstract modifier for creating abstract classes and methods
    - synchronized and volatile
      - synchronized and volatile modifiers, which are used for threads

## Variables

- variables are memory locations which are reserved to store value
- this implis while declaring a variable you reserve some memory
- types

  - local
    - local variables are declared in methods, constructors, or blocks
    - local variables are created when execution enters a method, constructor or block
    - access modifiers cannot be used for local variables
    - local variables are visible only within the declared method, constructor or block
    - local variables are implemented at stack level internally
    - there are no default value for local variables, so local variables should be declared and an initial value should be assigned before the first use.
  - class/static
    - class variables are declared with the static keyword inside a class, buit it is created outside a mthod, constructor or a block
    - class variables are declared as constants i.e. variable never change from their initial value
    - static variable are stored in static memory
    - It is rare to use static variables other than declared final and used as either public or private contstats
    - static variables are created when the program starts and destroyed when the program stops
    - static variables are declared public since they must be available for users of the class
    - static variables can be accessed by calling with the class name -- ClassName.VariableName
  - instance
    - instance variables are declared in a class
    - when a space is allocated for an object in the heap, a slot for each instance variable value is created.
    - instance variables are created when an object is created with the use of keyword 'new' and destroyed when the object is destroyed.
    - access modifiers can be given for instance variables
    - the instance variables are visible for all methods, constructors and block in the class
    - Instance variable have default value. for numbers, the default value is 0, for booleans it is false, and for oject reference it is null.
    - values can be assigned during the declaration or within the constructor
    - instance variables can be accessed directly by calling the variable name inside the class. However, within static methods (when instance variables are given accessibility), they should be called using the fully qualified name ObjectReference.VariableName

- Datatypes( How do we decide what amount of memory is to be allocated?)

  - each variable in java has a specific type, which determines the size of memory, the range of values that can be stored and the set of operations that can be applied to the variable

        - datatype types:

          - primitive

            - datatypes which predefined by the language and named as a keyword
            - 8 major primitive datatypes:
              - byte -numbeer
              - short
              - int
              - long
              - float
              - double
              - char
              - boolean
                Syntax:
                `int num = 50;`

          - non-primitive/reference

            - reference variable are created using defined constructors of the classes
            - these variables are declared to be of a specific type that cannot be changed
            - object of various classes String and Arrays come under reference datatype
              Syntax:
              `Student s1 = new Student();`

    ![alt text](./images/primitive-datatypes.png)
    ![alt text](./images/non-primitive-datatypes.png)

## Datatype Conversions

- datatypes of a particular variable can be converted to other datatypes
- there are 2 ways in which we can perform datatypes conversions:
  - implicit conversion
  - explicit conversion
    ![alt text](./images/datatype-conversion.png)
    ![alt text](./images/implicit-conversion.png)
    ![alt text](./images/need-of-conversion.png)
    ![alt text](./images/explicit-conversion.png)

## Type conversion - method

- String to int: Integer.parseInt()/Integer.valueOf()
- int to String: Integer.toString()/String.valueOf()

## Operators

- Unary
- Arithmetic
- Shift
- Relational
- Bitwise
- Logical
- Ternary
- Assignment

## Control Statements

- Selection/Decision making Statement
  - if/else
  - switch
- Iteratin Statement

  - for

    - simple
    - label

      - we can have a label of each for loop
      - it is useful if we have nested for loop so that we can break/continue a specific for loop
      - Normally, break and continue keywords breaks/ continues the inner most for loop only
      - Syntax

        ```java
        labelname:
        for (initialization; condition; incr/decr){
            // code to be executed
        }
        ```

    - for-each / enhanced

      - it is used to traverse array or collection in java
      - it is easier to use than simple for loop because we don't need to increment value and use subscript notation
      - Syntax

        ```java
        for (Type var: array){
            // code to be executed
        }
        ```

- while
- do...while

- Jump Statement
  - break
  - continue
  - return

## Methods

- method has a group of statements
- re-usability of block of code minimizes redundancy
- a class may have multiple methods
- a methods returns a null or a value using the return statement
  ![alt text](./images/method-syntax.png)

## ways of calling method

- call by value
  - method of passing arguments of a function copies to actual value of an argument into the formal parameter of a function
  - method overloading(Polymorphism)
    - a class may define mulitple methods with the same name and return type, but different number of arguments or arguments of different data types. this is called method overloading.
- call by reference

## Arrays

- Array are used to solve the problem of storing multiple elements of the same DataType
- An Array is a group of like-typed variables, that are referred to by a common name
- Specific element in an Array is accessed by it's index.
- Array size is fixed and cannot be changed

```java
int [] a= new int[5];
int [] a= [1,2,3,4,5];

```

## Types of Arrays

- Single Dimensional Array
- Multi Dimensional Array

## Strings

- is a sequnce of characters
- they are objects of type string class
- once a string object is created, it cannot be changed. strings are immutable.

```java
  char c[] = {'a', 'b', 'c'};
  String str = new String(); // string creation using new keyword
  String str1 = "sandesh rana"; // string creation using literals
```

## Immutability of strings

- security
  - string are used for network connection and for database connection. To avoid the access to these connections from external users, string are immutable.
- synchronization
  - immutablitiy of strings automatically makes system thread safe to solve the synchronization problem
- caching
  - if two strings objects are having the same value, and you need only one string, then the two objects will point to the same memory location pointing same string object

## String pool

- used in java is a pool of strings stored in java heap memory
- is possible only because string are immutable
- helps in saving lot of space for java runtime

## String - Memory allocation

- string is not a primitive data types
- are stored in the string pool of the heap area
- when we create object of string, then object name(variable) will be stored in stack portion of memory and the value we are assigning to that variable will be stored in string pool(portion of heap memory)
- reference in stack, actual object in heap

## StringBuffer(synchronized)

- is used to create mutable string i.e. Memory allocation to a string is not fixed, it can change. It is synchronous in nature i.e. Thread Safe
- access / modification by multiple threads at a time
- slower than StringBuilder

## StringBuilder(non-synchronized)

- is used to create mutable string. But, stringBuilder class is non-synchronized i.e it is not Thread Safe. Therefore, StringBuilder is faster
- accessed by single thread at a time
- faster than StringBuffer
