# FORMAT FOR TXT FILES TO BE READ (PER LINE):
# [class  name]; [super  class  name]; [list  of attributes separated by ","]

import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Task 1.1
class PythonClass:
    def __init__(self, c_name: str, sc_name: str, attr_list: list) -> None:
        self._c_name = c_name
        self._sc_name = sc_name
        self._attr_list = attr_list
    
    def set_c_name(self, new_c_name) -> None:
        self._c_name = new_c_name
    
    def set_sc_name(self, new_sc_name) -> None:
        self._sc_name = new_sc_name
    
    def set_attr_list(self, new_attr_list) -> None:
        self._attr_list = new_attr_list

    def get_c_name(self) -> str:
        return self._c_name
    
    def get_sc_name(self) -> str:
        return self._sc_name
    
    def get_attr_list(self) -> list:
        return self._attr_list
    
    def __str__(self) -> str:
        result = f"Class: {self._c_name}\n"
        result += f"__init__({self._c_name}, {self._sc_name}, {self._attr_list})\n"
        result += f"Mutators:"
        for attr in self._attr_list:
            result += f" set_{attr}(),"
        result = result[:-1] + "\n"
        result += f"Accessors:"
        for attr in self._attr_list:
            result += f" get_{attr}(),"
        result = result[:-1] + "\n"
        result += "__str__(): Generate  a  long  string  which  contains  the  class definition, __init__function, mutators, accessors and the dummy __str__ function."
        return result

# pc = PythonClass("Person", "object", ["name", "age"]) 
# print(pc)

# Task 1.2
class PCG:
    def __init__(self) -> None:
        self._pc_list = []
    
    def add_pc(self, pc: PythonClass) -> None:
        self._pc_list.append(pc)
    
    def read_file(self, file_name) -> None:
        file = os.path.join(basedir, file_name)
        with open(file, "r") as f:
            line = f.readline()
            while line:
                c_name, sc_name, attr = line.strip().split(";")
                attr_lst = attr.split(",")
                
                # if there is a superclass, include its attributes
                if sc_name != "" and self._pc_list:
                    for pc in self._pc_list:
                        if pc.get_c_name() == sc_name:
                            inherited_attr_lst = pc.get_attr_list() # inherit the attr from parent
                            attr_lst = inherited_attr_lst + attr_lst
                            break
                
                pc = PythonClass(c_name, sc_name, attr_lst)
                self._pc_list.append(pc)
                line = f.readline()
    
    def generate(self, file_name) -> None:
        file = os.path.join(basedir, file_name)
        result = ""
        for pc in self._pc_list:
            # class definition
            result += f"class {pc.get_c_name()}({pc.get_sc_name()}):\n"
            
            # __init__
            result += "    def __init__(self"
            for attr in pc.get_attr_list():
                result += f", {attr}"
            result += "):\n"
            
            # super().__init__() if there is a superclass
            parent = None
            if pc.get_sc_name() != "":
                result += f"        super().__init__("
                for parent in self._pc_list:
                    if parent.get_c_name() == pc.get_sc_name():
                        parent = parent
                        for attr in parent.get_attr_list():
                            result += f"{attr}, "
                        result = result[:-2]
                        break
                result += ")\n"
            
            # init the attributes
            for attr in pc.get_attr_list():
                if parent is None or attr not in parent.get_attr_list():
                    result += f"        self._{attr} = {attr}\n"
            result += "\n"
            
            # mutators
            for attr in pc.get_attr_list():
                if parent is None or attr not in parent.get_attr_list():
                    result += f"    def set_{attr}(self, new_{attr}):\n"
                    result += f"        self._{attr} = new_{attr}\n"
                    result += "\n"
            
            # accessors
            for attr in pc.get_attr_list():
                if parent is None or attr not in parent.get_attr_list():
                    result += f"    def get_{attr}(self):\n"
                    result += f"        return self._{attr}\n"
                    result += "\n"
        
        with open(file, "w") as f:
            f.write(result[:-1])
    
    def display(self) -> None:
        result = "Classes:"
        for pc in self._pc_list:
            result += f" {pc.get_c_name()},"
        result = result[:-1]
        print(result)

# pcg = PCG()
# pcg.read_file("new_class.txt")
# pcg.generate()

# Task 1.3
def display_menu():
    menu_opts = """
1. Get User Input
2. Display
3. Read File
4. Generate OOP File and End
"""
    print(menu_opts)

def menu():
    pcg = PCG()
    done = False
    while not done:
        display_menu()
        user_input = input("Please select an option 1 to 4: ")
        if user_input == "1":
            c_name = input("Class name: ")
            sc_name = input("Superclass name (Press 'Enter' if none): ")
            attr_lst = input("List of attributes, separated by ',': ").split(",")
            pc = PythonClass(c_name, sc_name, attr_lst)
            pcg.add_pc(pc)
            print("Added object successfully.")
        elif user_input == "2":
            pcg.display()
        elif user_input == "3":
            file_name = input("Enter the file name to read: ")
            try:
                pcg.read_file(file_name)
                print("File read successfully.")
            except:
                print("Likely an invalid file name. lol")
        elif user_input == "4":
            file_name = input("Enter the file name to write to: ")
            pcg.generate(file_name)
            print("Generated OOP file and ending program. Thank you!")
            done = True
        else:
            print("Invalid option. Please select a valid option.")

            
menu()