# Programa Python para embaralhar um baralho de cartas

# importando módulos
import itertools, random

# montando um baralho de cartas
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
print("Você tem:")
for i in range(5):
   print(deck[i][0], " de ", deck[i][1])
