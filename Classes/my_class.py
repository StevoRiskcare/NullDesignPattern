from AbsClass.abs_class import AbsClass


class MyClass(AbsClass):
    def do_something(self, value):
        print("Do something with {}".format(value))