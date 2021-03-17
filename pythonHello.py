print('Hello, world!')

# Soma
num1 = 2.3
num2 = 7.8
soma = num1 + num2
print('A soma de {0} e {1} eh {2}'.format(num1, num2, soma))

my_str = "Olah meus amigos esta eh uma frase que serah ordenada"
words = [word.lower() for word in my_str.split()]
words.sort()
print("Em ordem:")
for word in words:
   print(word)