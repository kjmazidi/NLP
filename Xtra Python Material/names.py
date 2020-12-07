# put this in a file named 'names.py'
# error in the last line
# check types: $mypy names.py

def find_first(names: list) -> str:
    if not names:
        return 'Error: "names" is an empty list'
    first = names[0]
    for name in names[1:]:
        if name < first:
            first = name
    return first

names = ['Jane', 'Zelda', 'Bud']
print('first name is ', find_first(3))  # sending wrong type to function