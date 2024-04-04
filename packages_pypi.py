# https://pypi.org/

from prettytable import PrettyTable

table = PrettyTable()
# Method
table.add_column("Pokemon Name",
["Pikachu","Squirtle","Charmander"])
# Method
table.add_column("Type",
["Electric","Water","Fire"])

# an attribute
table.align = "l"
print(table.align)
print(table)