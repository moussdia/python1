# 


#TP COMPRENDRE LA BOUCLE 'for'

# Affiche 'x' Pour 'x' dans la chaine de caractère ''mangue''
'''
for x in "mangue":

   print(x) '''


'''
# Declare les arguments de la variable fruits
fruits = ["poire", "mangue", "kiwi"]

#Affiche tous les arguments inférieurs ou egale à 'x' dans la variable fruits
#et arrete la boucle  
for x in fruits:
	print(x)
	if x == "mangue":
	  break 
'''

'''
# Declare les arguments de la variable fruits
fruits = ["poire", "mangue", "kiwi"]

#Affiche tous les arguments strictement inférieurs à 'x' dans la variable fruits
#et arrete la boucle  
for x in fruits:
	
	if x == "mangue":
	  break 
	print(x) 
'''

'''
# Declare les arguments de la variable fruits
fruits = ["poire", "mangue", "kiwi"]

#Affiche tous les arguments egale à 'x' dans la variable fruits
#et arrete la boucle  
for x in fruits:
	
	if x == "mangue":
	   break 
print(x) 

'''


'''
# Declare les arguments de la variable fruits
fruits = ["poire", "orange", "mangue", "kiwi", 'goyave']

#Affiche tous les arguments strictement inférieurs à 'x' dans la variable fruits
#et continue la boucle pour afficher tous les arguments après 'x'  
for x in fruits:
	if x == "mangue":
		continue
	print(x)
'''

'''
# Declare les arguments de la variable fruits
fruits = ["poire", "orange", "mangue", "kiwi", 'goyave']

#Affiche le dernier argument dans la variable fruits
   
for x in fruits:
	if x == "goyave":
		continue
print(x)
'''

'''
# Declare les arguments de la variable fruits
fruits = ["poire", "orange", "mangue", "kiwi", 'goyave']

#Affiche tous les arguments de la variable fruits
   
for x in fruits:
	print(x)
	if x == "orange":
		continue
'''

'''
#Affiche 6 nombres entiers '0 1 2 3 4 5'

for x in range(6):
	print(x)
'''

'''
#Affiche le resultat en commençant par 2 en incrementant de 3 a chaque fois
#Jusqu'à atteindre 30 

for x in range(2,30,3):
	print(x)
'''

'''
#Affiche le resultat en commençant par '-4' en incrementant de '-6' a chaque fois
#Jusqu'à atteindre '-50' 

for x in range((-4),(-50),(-6)):
	print(x)
'''

