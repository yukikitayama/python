# OOP

`help()` can be used to get a list of object-specific methods.

## Inheritance

`isinstance()` works on object of subclass of other superclass too.

## Magic method

`__getitem__()` enables indexing and slicing. Define behavior when the index operator `[]` is used.

`__index__()` is called on an object to get its associated **integer value**.

Division magic method is `__truediv__()` for `/` and `__floordiv__()` for `//`. `__div__` doesn't exist.

`__new__()` is used to create a new instance of a class before it is initialized. It's a static method that is called
before `__init__()` when an object is created. Use it for specific control over the instance creation process.

`__contains__()` defines object behavior when `in` keyword is used to check if an object is a member of another object.

## Polymorphism

The ability of an object to take on many forms and exhibit different behaviors based on the context.

Same method or operation to be applied to different objects, resulting in different beheviors based on the specific
object's implementation of the method.

## MRO

`__mro__` is **Method Resolution Order** attribute containing a **tuple** that defines the order in which base
classes are searched for a method during method resolution. It represents the inheritance hierarchy of a class,
listing the base classes in the order they would be checked for method resolution.

`__mro__` has `object` at the last of a tuple.

## Exception

- `__cause__`
  - Explicitly chained exception
- `__context__`
  - Implicitly chained exception
  - It points to the exception that caused the current exception to be raised.
  - When raising a new exception while another exception is being handled, the new exception's special attribute that is
    automatically set to the handled exception
- `__traceback__`
  - Traceback representing the stack trace information associated with the exception
  - Information about the sequence of function calls leading up to the exception

