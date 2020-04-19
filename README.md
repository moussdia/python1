# python1


#TP2 Calculer la moyenne de classe  

#-*- coding: utf-8 -*-
'''
# Calculer la moyenne de classe des eleves 
# Entrer la note math
Math = input ("Saisir la note de math : " )

# Entrer la note physique
Physique = input ("Saisir la note physique : " )

# Entrer la note francais
Francais = input ("Saisir la note Francais : " )

# Entrer la note anglais
Anglais = input ("Saisir la note de Anglais : " )

# Faire la somme 
Toto = int(Math) + int(Physique) + int(Francais) + int(Anglais)
        
print('La somme des notes est: ', Toto) 

#Faire la moyenne
Total = int(Toto) / 4
print('La moyenne est: ', Total)

#Donne la mention de l'eleve
if (Total >= 13):
   print('Mention Assez bien')
elif(Total >=10):
   print('Mention Passable')
elif(Total <10):
   print('Mention Mediocre')
else:
   print('Mention Tres Mediocre')
'''

'''
#Calculer l'age des personnes

#-*- coding: utf-8 -*-

#Declare une variable age et entrer le nombre entier

age = int(input('tapez votre age : '))

 #j'applique la condition pour definir la tranche d'age
if(age >= 18):
 	 print('Vous êtes majeur !')
elif(age <15):
 	 print('Vous êtes trop petit !')
else: 
 	 print('Vous êtes adolescent') 

'''
