calls = 0
def count_calls():
    global calls
    calls = calls + 1


def string_info(string):
    count_calls()
    b = len(string)
    c = string.upper()
    d = string.lower()
    tuple_ = b, c, d
    print(tuple_)


def is_contains(string, list_to_search):
    count_calls()
    for i in range((len(list_to_search))):
        list_to_search[i] = str(list_to_search[i])
        if string.casefold() == (list_to_search[i].casefold()):
            print(True)
            print(False)


string_info('Capybara')
string_info('Armageddon')

is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)


