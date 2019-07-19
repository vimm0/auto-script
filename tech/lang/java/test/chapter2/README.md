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
