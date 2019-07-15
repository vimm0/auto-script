##### Object-oriented Design
- **Object-oriented Analysis (OOA)** is the process of looking at a problem, system, or task that somebody wants to turn into an application and identifying the objects and interactions between those objects. 
    - Visitors to the website need to be able to (italic represents actions, bold represents objects):
        - _review_ our **history**
        - _apply_ for **jobs**
        - _browse_, _compare_, and _order_ our **products**

- **Object-oriented Design (OOD)** is the process of converting such requirements into an implementation specification
    - Designer must name the objects, define the behaviors, and formally specify what objects can activate specific behaviors on other objects.
    - All about how things should be done

- **Object-oriented Programming (OOP)** is the process of converting this perfectly defined design into a working program
- Iterative development model
- Unified Modeling Language / class diagrams
- Attributes are settable, while properties are read only
- Encapsulation, abstraction
- Object relations: association, composition, and inheritance
- Composition, Aggregation and inheritance
    -  If the composite (outside) object controls when the related (inside) objects are created and destroyed, composition is most suitable. If the related object is created independently of the composite object, or can outlast that object, an aggregate relationship makes more sense.
    -  _is a_ relationship is formed by inheritance. eg. "Deep Blue _is a_ player" or that "Gary Kasparov _is a_ player".
    - _has a_ relationship is formed by association.
    - Interfaces, Polymorphism, duck typing("If it walks like a duck or swims like a duck, it's a duck".), Multiple inheritance
    - Specialization(changing attributes or behaviors on the subclass to make it somehow different from the parent class)
- Object diagram / Instance diagram
