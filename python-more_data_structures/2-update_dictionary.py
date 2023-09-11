# The function below replaces or adds key/value in a dictionary.
# key argument is a string
# If a key exists in the dictionary, the value will be overwritten/replaced
# If a key doesn’t exist in the dictionary, it will be created

def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary
