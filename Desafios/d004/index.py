var = input('Digite um valor: ')
print('{}\nIs alphanum: {}\nIs alpha: {}\nIs ASCII: {}\nIs Decimal: {}\nIs Digit: {}\nIs Identifier: {}\nIs lower: {}\nIs numeric: {}\nIs Printable: {}\nIs Space: {}\nIs Title: {}\nIs Upper: {}\n'.format(type(var), var.isalnum(), var.isalpha(), var.isascii(), var.isdecimal(), var.isdigit(), var.isidentifier(), var.islower(), var.isnumeric(), var.isprintable(), var.isspace(), var.istitle(), var.isupper()))
