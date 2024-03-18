from AbsClass.abs_class import AbsClass


class NullClass(AbsClass):
    def do_something(self, value):
        print("Cannot do anything with {}".format(value))