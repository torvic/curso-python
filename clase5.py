x = 10
y = 5.678
z = 1.2e-6 # 1.2E6
print(type(x))
print(type(y))
print(z)
print(type(z))

print(x + y)
print(y + y)

is_true = True
is_false = False

print(type(is_true))
print(type(is_false))

# sep
print("Nunca", "pares", "de", "aprender", sep="//")

# end
print("Nunca", end="\n")
print("pares de aprender")

# f-strings
phrase = 'Nunca pares de aprender'
author = 'XD'
print(f'Phrase: {phrase}, Author: {author}')

# format
print('Phrase: {}, Author: {}'.format(phrase, author))

# saltos de linea
print("Hola\nmundo")

