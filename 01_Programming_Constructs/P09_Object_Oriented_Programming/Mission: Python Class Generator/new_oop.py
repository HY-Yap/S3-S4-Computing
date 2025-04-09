class PythonClassName(SuperClassName):
    def __init__(self, ClassAttributes):
        super().__init__()
        self._ClassAttributes = ClassAttributes

    def set_ClassAttributes(self, new_ClassAttributes):
        self._ClassAttributes = new_ClassAttributes

    def get_ClassAttributes(self):
        return self._ClassAttributes

class Person():
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def set_name(self, new_name):
        self._name = new_name

    def set_age(self, new_age):
        self._age = new_age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

class Student(Person):
    def __init__(self, name, age, class_, subject_list):
        super().__init__(name, age)
        self._class_ = class_
        self._subject_list = subject_list

    def set_class_(self, new_class_):
        self._class_ = new_class_

    def set_subject_list(self, new_subject_list):
        self._subject_list = new_subject_list

    def get_class_(self):
        return self._class_

    def get_subject_list(self):
        return self._subject_list

class Teacher(Person):
    def __init__(self, name, age, classes, teaching_subject):
        super().__init__(name, age)
        self._classes = classes
        self._teaching_subject = teaching_subject

    def set_classes(self, new_classes):
        self._classes = new_classes

    def set_teaching_subject(self, new_teaching_subject):
        self._teaching_subject = new_teaching_subject

    def get_classes(self):
        return self._classes

    def get_teaching_subject(self):
        return self._teaching_subject
