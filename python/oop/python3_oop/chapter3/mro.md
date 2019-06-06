- https://www.python.org/download/releases/2.3/mro/
- https://stackoverflow.com/questions/1848474/method-resolution-order-mro-in-new-style-classes
- _if C1 precedes C2 in the linearization of C, then C1 precedes C2 in the linearization of any subclass of C_
```>>> O = object
>>> class X(O): pass
>>> class Y(O): pass
>>> class A(X,Y): pass
>>> class B(Y,X): pass
```
- In this case, it is not possible to derive a new class C from A and B, since X precedes Y in A, but Y precedes X in B, therefore the method resolution order would be ambiguous in C.

Terms
- C3 superclass linearization is an algorithm used primarily to obtain the order in which methods should be inherited (the "linearization") in the presence of multiple inheritance, and is often termed Method Resolution Order (MRO).
- C3 linearization results in three important properties:
    - a consistent extended precedence graph,
    - preservation of local precedence order, and
    - fitting the monotonicity criterion.

