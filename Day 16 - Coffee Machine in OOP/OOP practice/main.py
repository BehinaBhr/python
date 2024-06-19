from prettytable import PrettyTable
table = PrettyTable()
table.add_column("family",["Behina","Sadjad","Farshad","Nooshin","Borna"])
table.add_column("relationship", ["girl", "son- in-law", "father", "mother", "boy"])
print(table)

print(table.align)
table.align = "l"
print(table)