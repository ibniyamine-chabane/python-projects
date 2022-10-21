#Écrivez un programme pendu.py, qui permet à l’utilisateur de faire une partie du célèbre
#jeu le pendu dans le terminal.
#Le programme devra dans un premier temps demander au joueur le niveau avec lequel il
#souhaite jouer. Il aura un nombre de vies en fonction du niveau choisi (exemple
#débutant 10, intermédiaire 7, expert 4). Vous êtes libres de choisir le nombre de vies par
#niveau.
#Le programme devra donc choisir aléatoirement un mot dans le dictionnaire disponible
#ici, et afficher :
#- Le nombre de vies restantes au joueur
#- Les lettres déjà proposées par le joueur (dans le mode débutant et intermédiaire.
#En expert, la liste n’apparaîtra pas)
#- Des “_” pour remplacer les lettres non trouvées
#- Les lettres proposées qui se trouvent dans le mot
#La partie prend fin lorsque le joueur a trouvé le mot, ou qu’il n’a plus de vie.

import random
#---------------Choix de niveau------------------
lvlChoose = int(input("Bonjour, à quel niveau souhaite tu jouer? choisis entre 1 à 3: ")) #Je demande à quel niveau l'utilisateur veux jouer 
life = 10 #les vie de l'utilisateur 

if lvlChoose == 1 :
    life = 10 
elif lvlChoose == 2 :
    life = 5 
elif lvlChoose == 3 :
    life = 3

#print("nombre de vies restant :",life)


file = open("dico_france.txt", "r") #dans la variable file on ouvre le fichier dico_france.txt 
dico_list = [] # tableau vide prévu pour contenir le contenu de la variable dico
dico = file.readlines() #dans la variable dico stocke la lecture de la variable file.

#------------------------Lecture du dictionnaire------------------------
for line in dico: # on crée une variable line qui va parcourir dico
    line = line.replace("\n", "")# line remplace "\n" par une chaine vide ""
    dico_list.append(line)# on envoie le nouveau contenu de line qui n'a plus de "\n" vers dico liste qui était vide
    word = random.choice(dico_list)# on prend des élement au hasard dans notre 
    
print(word)
#------------------------Zone de jeu------------------------------------
zone_Game = ""
lettre_choisis = []

for l in word: # je fait une boucle pour la zone de mot
    zone_Game = zone_Game + "_ " # la zone de mot qui correspond au nombre de mot a trouvé 


while life > 0: #tant  que mes vies sont supérieur à 0 
    print("nombre de vies restant ",life) 
    print(zone_Game)  
    proposition = input("Lettre proposées : ")
    lettre_choisis.append(proposition)
    print("lettre déja jouée" ,lettre_choisis) 

# pas terminé, recherche de la problemeatique toujours en cours.
if  proposition == word: # si ma proposition match avec une lettre dans le mot.
    #lettre_choisis = lettre_choisis + proposition
    print("trouvé !")


