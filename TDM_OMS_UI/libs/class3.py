# class3.py
from libs.class1 import Class1


class Class3:
    @staticmethod
    def get_shared_variable():
        return Class1.get_variable()

    @staticmethod
    def get_shared_variable_i():
        return Class1.get_variable_i()
