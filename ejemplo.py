import numpy as np
import pandas as pd

# create pandas data set function name() using pandas


def name():
    name = 'Jack'
    surname = 'Crowley'
    name_dataset = {
        'Name': [name],
        'Surname': [surname],

    }

    name_dataframe = pd.DataFrame(name_dataset, )

    return name_dataframe


# call and print the name function
print(name())

"""
a = np.array([[2, 1, -2],
              [3, 0, 1],
              [1, 1, -1]])
# print(m)
b = np.array([[-3], [5], [-2]])
bt = (np.transpose(b))  # matriz transpuesta

# sistema de ecuaciones

x = np.linalg.solve(a, b)
# print(x)
# print(a)
# print(np.allclose(np.dot(a, x), b))  # validar que esta correcta la ecuacion

m1 = np.array([[2, 7, 3], [2, 8, 2], [1, 3, 1]])
print(m1)

m2 = np.array([1, 1, 0])
m2.shape = (3, 1)  # sirve para transponer

print(np.linalg.solve(m1, m2))
"""
