# Chapter 2

- Class
- Object
- Attributes
  - built-in
  - attributes defined by user
- Java Naming Convention(camelCase)
  - Variable Name: start with lowercase letter(instanceVariable)
  - Constant Name: start with uppercase letter(CONSTANT)
  - Class Name: start with uppercase letter and should be noun(ClassName)
  - Method Name: start with lowercase letter and should be verb(getName)
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

- Polymorphism
  - static (method overloading)
  - dynamic
- Abstraction
- Encapsulation
