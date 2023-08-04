#!/usr/bin/python3
import importlib.util

def import_variable_from_file(file_name, variable_name):
    spec = importlib.util.spec_from_file_location("module_name", file_name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, variable_name)

if __name__ == "__main__":
    variable_value = import_variable_from_file("variable_load_2.py", "a")
    print("The value of 'a' is:", variable_value)