# Day2

## Regular expressions

### Template strings

I notice that we can use `fr"..."`


## `super()`

### Parameter of `super()`

No idea.

### Method resolution order (MRO)

```py
class Root:
    def fn(self):
        print("Root", self)


class A(Root):
    def fn(self):
        print("A", self)
        super().fn()


class B(Root):
    def fn(self):
        print("B", self)


class C(A, B):
    def fn(self):
        print("C", self)
        super().fn()


c = C()
c.fn()
print(c.__class__.__mro__)
# C <__main__.C object at 0x107c0d510>
# A <__main__.C object at 0x107c0d510>
# B <__main__.C object at 0x107c0d510>
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Root'>, <class 'object'>)

```

### What does `super()` return?

An instance of super class. It is a proxy object that delegates method calls to a parent or sibling class of type.

> proxy object: a wrapper class that stores an object and forwards attribute lookups to that object

```py
class SimpleProxyObject:
    def __init__(self, obj: object):
        self.obj = obj

    def __getattr__(self, item: str):
        return getattr(self.obj, item)


obj = [1, 2, 3]
proxy = SimpleProxyObject(obj)

proxy.append(4)
assert obj == [1, 2, 3, 4]
```


