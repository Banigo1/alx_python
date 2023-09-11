def update_dictionary(a_dictionary, key, value):
    # Check if the key exists in the dictionary
    if key in a_dictionary:
        # If the key exists, replace the existing value
        a_dictionary[key] = value
    else:
        # If the key doesn't exist, add a new key-value pair
        a_dictionary[key] = value

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Update an existing key's value
update_dictionary(my_dict, 'b', 42)
print(my_dict)  # Output: {'a': 1, 'b': 42, 'c': 3}

# Add a new key-value pair
update_dictionary(my_dict, 'd', 99)
print(my_dict)  # Output: {'a': 1, 'b': 42, 'c': 3, 'd': 99}
