# 

#TP COMPRENDRE LES FONCTIONS

#Affiche le contenu de print 
print ("Akwaba Python Calculator")
'''
#Declarer l'argument de ma fonction et renvoyer les valeurs 'x' et 'y'
def somme (x,y):
    return x + y

#Definir la fonction 'main' qui va faire la somme des entiers x et y, afficher la somme de x et y 
def main():
    print("Faire la somme x et y")
    x = int(input("Premier chiffre est:"))
    y = int(input("Deuxieme chiffre est:"))
    resultat = somme(x,y)
    print("La somme de ", x ,"et", y ,"est",
resultat)

# 
if __name__=="__main__":

#Appel la fonction 'main()'	
    main()
'''

#Fonction avec soustraction 


#Declare l'argument de ma fonction et renvoyer les valeurs 'x' et 'y'
def soustraction (x,y):
    return x - y

#Definir la fonction 'main' qui va faire la soustraction et afficher la soustraction de x et y 
def main():
    print("Faire la soustraction x et y")
    x = int(input("Premier chiffre est:"))
    y = int(input("Deuxieme chiffre est:"))
    resultat = soustraction(x,y)
    print("La soustraction de ", x ,"et", y ,"est",
resultat)


if __name__=="__main__":
#Appel la fonction 'main()'	
    main()
