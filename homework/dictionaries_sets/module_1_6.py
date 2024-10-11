# Dictionary
my_dict = {'Name': 'Emil', 'City': 'Yekaterinburg', 'Age': 25}
print('Initial dictionary:', my_dict)
print('Existing value:', my_dict['Name'])
print('Non-existing value:', my_dict.get('Height', 'Invalid key'))
my_dict.update({'Weight': 80,
                'Height': 182})
print('Deleted value:', my_dict.pop('Weight'))
print('Modified dictionary:', my_dict)

# Set
my_set = {0, 1, 2, 2, 3, 3, 3, 'One', 'One', 'One', True, False, True}
print('Initial set:', my_set)
my_set.update({4, 'Five'})
my_set.remove(False)
print('Modified set:', my_set)