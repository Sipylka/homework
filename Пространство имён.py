calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    count_calls()
    stroke = len(string), str(string).upper(), str(string).lower()
    return stroke

def is_contains(string, list_to_search):
    new_list = []
    for i in range(0,len(list_to_search)):
        new_list = list_to_search[i].lower()
    if string.lower() in new_list:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
