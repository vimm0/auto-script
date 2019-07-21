# Chapter 2

- Class
- Object
- Attributes
  - built-in
  - attributes defined by user
- Java Naming Convention(camelCase)
  - Variable Name: start with lowercase letter(instanceVariable)
  - Constant Name: start with uppercase letter(CONSTANT)
  - Class Name: start with uppercase letter and should be noun(ClassName) - PascalCase
  - Method Name: start with lowercase letter and should be verb(getName) - camelCase
  - Interface Name: start with uppercase letter and should be adjective(Interface)
- Constructor:

  - new keyword create constructor with the help of JVM and assign 0, null depending upon type of instance variable
  - must be same name as class name
  - constructors can appear anywhere in the code for the class
  - constructor is used to initialize state of an object
  - invoked implicitly

    - default constructor

      ```java
      ClassName() {
          instanceVariable=200;
      }
      ```

    - parameterized constructor

      ```java
      ClassName(int value) {
          instanceVariable=value;
      }
      ```

- Constructor Overloading

  - is just like method overloading without return type
  - in java is a technique of having more than one constructor with different parameter list

- Constructor Chaining
  - is process of calling one constructor from another constructor with respect to the current object
  - purpose of constructor chaining is to pass parameters through a bunch of different constructors, but the initialization should be done at single place
  - can be done in two ways:
    - within same class
    - from base class
  - occur through inheritance

## Static Keyword

- is used for memory management
- is a non access modifier applicable for blocks, methods, class variables
- is used to refer the common properties of an object
- when the static keyword is used to declare any parameter, then memory is allocated only once for that parameter
- can be invoked without need to create instance of a class

## this keyword

- this keyword is used as reference variable to the current object
- this can be passed as an argument in the constructor call
- this can be used to invoke current class method
- this can be passed as an argument in the method call
- this() can be used to invoke current class constructor
- this keyword is used to refer current class instance variable and it can also be used to return the current class instance from the method

## super keyword

- is a reference variable that is used to refer parent class object
- types
  - used to refer immediate parent class instance variable
  - used to invoke parent class method
  - used to invoke parent class constructor

## Object Programming Language

- Inheritance

  - object acquire some or all the properties and behaviour of parent object.
  - is-a relationship
  - used for
    - method overriding(to acheive run-time polymorphism)
    - code reusability
      - `class SubClass extends SuperClass{}`
  - types
    - single inheritance
    - hierarchical in heritance
    - multilevel inheritance

- Aggregation (Has-a relationship)

- final keyword

  - non-access modifier
  - final can be
    - instance variable
    - method
    - class variable
    - local variable
    - method parameters
      -final variable is used to create constant variable
  - final method is used prevent method overriding
  - final class is used to prevent inheritance
  - if a class is declared as "final", then child classes cannot be created for that. A final class cannot be given after "extends" keyword.
  - constructor cannot be declared as final
  - A blank final variable should be initialized in the constructor

- Polymorphism

  - types

    - static (method overloading)
    - dynamic

  - Dynamic Binding(Run time polymorphism)
    - connecting a method calll to the method body is known as Binding
    - The binding can be Static and Dynamic

- Abstraction: is a mechanism of hiding the implementation details from the user and only providing the functionality to the user.
  - two ways to acheive abstration
    - abstraction class
    - interface
  - Abstract class and Abstract Method
    - An abstract method is a method that is declared without an implementation
    - Any class that contains one or more abstract methods, must also be declared with abstract keyword
    - An abstract class is a class that is declared with abstract keyword.
    - An abstract class may or may not have all abstract methods.
    - Abstract class is mostly used for inheritance
- Encapsulation
  - is the methodology of binding code and data together into single unit
  - to achieve encapsulation in java:
    - declare the variable of a class as private
    - provide publc setter and getter methods to modify and view the variables values.
  - advantages of encapsulation
    - data hiding: user will have no idea about the inner implementation of class
    - increased flexibility: we can make variables and method read-only or write-only as per requirement
    - reusability: easy to reuse and easy to change with new requirements
    - testing is easy

* Interface

  - is a blue print of how it should be done.
  - An interface contains all these specification and can be used while creating a new object
  - Interface contains variables and methods, but the methods declared inside interface are
    by default abstract methods
  - interface is used to achieve abstraction(loose coupling)
  - we can achieve multiple inheritance
  - java interface represents is-a relationship
  - implement multiple interfaces not multiple classes

- Interface vs class

  - interface can never be instantiated
  - interface should contain abstract method
  - members of an interface are always public
  - interface can never have a constructor
  - "implements" keyword is used for inheritance
  - after extends keyword any number of interfaces can be given
  - cannot contain instance fields. The only fields that can appear in an interface
    in an interface must be declared both static and final

  - class is instantiated to create objects
  - class should contain only concrete methods
  - member of a class can be private, public or protected
  - class can have constructor to initialize the variables
  - "extends" keyword is used for inheritance
  - after extends keyword only once class can be given
  - can contains instance fileds

- Class vs Abstract Class

  - classes have implementation
  - concrete class are instatiated to create objects
  - concrete class can be final

  - abstract class have no implementation
  - abstract clas cannot be instantiated
  - abstract class can never be final, as it has no defined functions

- Abstract Class vs Interface

  - abstract class can be extended to a class using keyword "extends"
  - abstract class can extend only one class at at time
  - abstract class can have private, default, protected and public
  - abstract class, keyword "abstract" is mandatory to declare a method as an abstract method.
  - abstract class are to achieve 0% to 100% abstraction.
  - abstract class can have constructors
  - abstract class can have abstract and non-abstract methods.

  - interface can be implemented to a class using keyword "implements"
  - interface can extend any number of interface at a time.
  - intarface member (member data) are public by default.
  - keyword 'abstract' is optional to declare a method as an abstract method
  - interface cannot have constructors
  - interface can have only abstract methods. From Java8, it can have default and static methods also.

  ![alt text](./images/class-interface-relation.png)

- Rules for using private methods in Interfaces
  - private interface method cannot be abstract
  - private method can be used only inside interface
  - private static method can be called from other static and non-static interface method
  - private non-static methods cannot be called from private static method.

## pacakge

- java package is a mechanism for organizing java classes to namespaces.
- programmers use package to organize classes belonging to the same category
- classes in the same package can access each other's member.
- java pre-defined packages: java.lang,java.util, java.io, java.net
  ![alt text](./images/access-level.png)
- Access package from Another package
  - import package.\*
  - import package.classname
  - fully qualified name

## Regular expression

- is a pattern used for searching and manipulating strings
- either matches the text or fails to match
- abbreviation used for regular expression is regex
- from java.util.regex pacakge
- types
  - Pattern class
  - Matcher class
  - PatternSyntaxException
- quantifier

## Exception

- is an event, which occurs durint the execution of a program, that disrupts the normal flow of the program's instruction
- when an exception occurs, the JVM creates an exception object to identify the type of exception that has occured
- An Exception is often to referred as Runtime Error
- types
  - checked exception
    - also called as compile-time exception.
    - means if a method is throwing a checked exception then it should handle the exception using try-catch block or it should declare the exception using throw keyword, otherwise the program will give a compilation error
  - unchecked exception
    - also called as run-time exception.
    - means if your program is throwing an unchecked exception and even if you didn't handle/declare that exception, the program won't give a
      compilation error. It is upto the programmer to judge the condition in advance, that can cause such exceptions and handle them appropriately
  - error
    - these are exceptional conditions that are external to the application, and that the application usually cannot anticipate or recover from. for example, if a (heap memory overflow)stack overflow occurs, an error will arise. They are also ignored at the time of compilation.
- exception class
  - throwable
    - error
    - exception
      - unchecked exception
        - runtime exception
          - ArithmeticException
          - ArrayStoreException
          - ClassCastException
          - IllegalArgumentException
          - IllegalMonitorException
          - IndexOutOfBoundsException
          - NegativeArrayException
          - NullPointerException
          - SecurityException
          - Other unchecked exceptions
      - checked exception
        - io exception
        - sql exception

## Exception Handling

- when a runtime error occurs, program gets crashed and control comes out of program
- exception handling is done to execute the program, without getting an exception
- mainly, try, catch and finally are keywords for exception handling
- multiple catch block
  - there will be many cases in which different exceptions may occur. So, in such scenarios, one try block can have multiple catch blocks.
    Depend on the type of exception thrown corresponding catch block is invoked.
  - Since all the exception are derived from Exception, catch (Exception e) should be placed at last. It can catch all the exceptions.

## throw

- java throw keyword is used to explicitly to throw an Exception while executing the program.
- It can be used to throw Checked or Unchecked Exceptions
- throw keyword is used inside a method

## Throw vs Throws keyword

- throw keyword is used to explicitly throw an Exception
- throw keyword is followed by an instance
- throw keyword is used within a method
- throw keyword can throw only one exception

- throws keyword is used to declare an Exception
- throws keyword is followed by a Throwable Class
- throws keyword is used with the method signate
- throws keyword is used to declare multiple exceptions

## User-defined Exception using throws

- you can create your own exception, it is called as User-defined exception or custom exception
- user-defined exception class can be created by creating a child class of java.lang.Exception
