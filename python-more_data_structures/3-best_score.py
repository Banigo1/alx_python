# A function that returns a key with the biggest integer value.

def best_score(a_dictionary):
    if not a_dictionary:
        return
    max_key = max(a_dictionary, key=lambda x: a_dictionary[x])
    return (max_key)

#  Another way that works WITHOUT using lambda
#  if not a_dictionary:
#    return
#  max_key = max(a_dictionary, key=a_dictionary.get)
#    return max_key