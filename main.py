from AbsClass.null_class import NullClass
from Classes.my_class import MyClass


class ObjectFactory(object):
    @staticmethod
    def create_object(value):
        if value == "MyClass":
            return MyClass()
        else:
            return NullClass()


obj = ObjectFactory.create_object("MyClass")
obj.do_something("my object")