# Programa Python para verificar se o ano é um ano bissexto ou não

year = 2000

# Para obter o ano do usuário
# year = int (input ("Insira um ano:"))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} é um ano bissexto".format(year))
       else:
           print("{0} não é um ano bissexto".format(year))
   else:
       print("{0} é um ano bissexto".format(year))
else:
   print("{0} não é um ano bissexto".format(year))
