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

# Loop
lower = 1
upper = 10
for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)

# Python Program to find the area of triangle

a = 5
b = 6
c = 7

# Uncomment below to take inputs from the user
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)