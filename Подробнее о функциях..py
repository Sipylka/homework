data_structure = [

  [1, 2, 3],

  {'a': 4, 'b': 5},

  (6, {'cube': 7, 'drum': 8}),

  "Hello",

  ((), [{(2, 'Urban', ('Urban2', 35))}])

]

def calculate_structure_sum(*n):
  if isinstance(data_structure, str):
    n = len(data_structure)
    if n == 0:
      return 1
    return n + calculate_structure_sum(n - 1)
    #return data_structure

result = calculate_structure_sum(data_structure)

print(result)