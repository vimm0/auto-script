## class method vs static method
- A class method will receive the class itself as the first argument, while a staticmethod does not.
- So a static method is, in a sense, not bound to the Class itself and is just hanging in there just because it may have a related functionality.

### Use cases
1. Grouping utility function to a class
2. Having a single implementation in inheritance

```
>>> class Klaus:
        @classmethod
        def classmthd(*args):
            return args

        @staticmethod
        def staticmthd(*args):
            return args

# 1. Call classmethod without any arg
>>> Klaus.classmthd()  
(__main__.Klaus,)  # the class gets passed as the first argument

# 2. Call classmethod with 1 arg
>>> Klaus.classmthd('chumma')
(__main__.Klaus, 'chumma')

# 3. Call staticmethod without any arg
>>> Klaus.staticmthd()  
()

# 4. Call staticmethod with 1 arg
>>> Klaus.staticmthd('chumma')
('chumma',)
```
