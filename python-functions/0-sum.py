def random_func(name: str, age: int, weight: float) -> str:
        print("Name :", name)
        print("Age :", age)
        print("Weight :", weight)
    
        return "{} is {} years old and weighs {}".format(name, age, weight)

print(random_func("Derek", 30, 80))