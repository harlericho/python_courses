myStr = "HarleRricho,Carlos"
dir(myStr)
# print(dir(myStr))
print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace('Harle','Carlos').upper())
print(myStr.count('r')) # Contar
print(myStr.startswith('Ha')) # Booleans, busca por caracteres
print(myStr.endswith('choo'))
print(myStr.split())
print(myStr.split(',')) # por un caracter separa el texto
print(myStr.split('o'))
print(myStr.find('H')) # Busca la posicion de la letra a encontrar
print(len(myStr)) # longitud del texto 
print(myStr.index('e')) # el indice la letra a buscar
print(myStr.isnumeric()) # si es numerico
print(myStr.isalpha()) # si es alfanumerico
print(myStr[2]) # imprime la letra por posicion
print(myStr[-2]) # imprime la letra inverso

myStr0, myStr1 = "My name is" ,"harlericho"
print(myStr0, myStr1)
print('My name is', myStr1)
print('My name is '+ myStr1)
print(f"My name is {myStr1}")
print("My name is {0}". format(myStr1))
print("{0} {1}".format(myStr0,myStr1))