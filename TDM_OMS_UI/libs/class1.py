# class1.py
class Class1:
    shared_variable = None

    @classmethod
    def set_shared_variable(cls, value):
        cls.shared_variable = value

    @staticmethod
    def get_shared_variable():
        return Class1.shared_variable
