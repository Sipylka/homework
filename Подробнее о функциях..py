data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def recursive_print(data):
  summa = 0
  if isinstance(data, (list, tuple, set)):
    for item in data:
      summa += recursive_print(item)
  elif isinstance(data, dict):
    for key, value in data.items():
      summa += recursive_print(key)
      summa += recursive_print(value)
  elif isinstance(data, str):
      summa += len(data)
  elif isinstance(data, (float,int)):
      summa += data
  return summa

print(f'Сумма: {recursive_print(data_structure)}')