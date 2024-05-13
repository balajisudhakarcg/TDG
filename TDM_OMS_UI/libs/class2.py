# class2.py
from libs.class1 import Class1


class Class2:
    @staticmethod
    def print_shared_variable():
        shared_value = Class1.get_shared_variable()
        print("Shared Variable Value:", shared_value)
        return shared_value
