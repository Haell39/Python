print("Merging dictionaries")

dict_a = {'a': 1, 'b': 2, 'o': 3}

dict_b = {'c': 3, 'd': 4, 'p': 5}

dict_d = {'z': 7, 't': 10, 'w': 9}

dict_e = {'x': 11, 'y': 12, 'z': 13}

dict_c = {**dict_a, **dict_b, **dict_d, **dict_e}
print(dict_c, "\n")


import pprint
pprint.pprint(dict_c)


