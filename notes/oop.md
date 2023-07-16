# OOP

## Polymorphism

The ability of an object to take on many forms and exhibit different behaviors based on the context.

Same method or operation to be applied to different objects, resulting in different beheviors based on the specific
object's implementation of the method.

## MRO

`__mro__` is **Method Resolution Order** attribute containing a **tuple** that defines the order in which base
classes are searched for a method during method resolution. It represents the inheritance hierarchy of a class,
listing the base classes in the order they would be checked for method resolution.

## Exception

- `__cause__`
  - Explicitly chained exception
- `__context__`
  - Implicitly chained exception
- `__traceback__`
  - Traceback representing the stack trace information associated with the exception
  - Information about the sequence of function calls leading up to the exception

