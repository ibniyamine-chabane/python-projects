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
lvlChoose = int(input("Bonjour, à quel niveau souhaite tu jouer? choisis entre 1: Débutant, 2: Intermédiaire, 3:Expert ")) #Je demande à quel niveau l'utilisateur veux jouer 
life = 10 #les vie de l'utilisateur 

if lvlChoose == 1 :
    life = 10 
elif lvlChoose == 2 :
    life = 5 
elif lvlChoose == 3 :
    life = 3


file = open("dico_france.txt", "r") #dans la variable file on ouvre le fichier dico_france.txt 
dico_list = [] # tableau vide prévu pour contenir le contenu de la variable dico
dico = file.readlines() #dans la variable dico stocke la lecture de la variable file.

#------------------------Lecture du dictionnaire------------------------
for line in dico: # on crée une variable line qui va parcourir dico
    line = line.replace("\n", "")# line remplace "\n" par une chaine vide ""
    dico_list.append(line)# on envoie le nouveau contenu de line qui n'a plus de "\n" vers dico liste qui était vide
    word = random.choice(dico_list)# on prend des élement au hasard dans notre 
    
#print(word)
#------------------------Zone de jeu------------------------------------
zone_Game = ""
right_letter = ""
letter_already_choosed = []

for l in word: # je fait une boucle pour la zone de mot
    zone_Game = zone_Game + "_ " # la zone de mot qui correspond au nombre de mot a trouvé 


while life > 0: #tant  que mes vies sont supérieur à 0 
    print("nombre de vies restant ",life) 
    print(zone_Game)  
    proposition = input("Lettre proposées : ")
    letter_already_choosed.append(proposition) # stocke les lettres déja proposer dans ma liste vide letter_already_choosed
    print("lettre déja jouée" ,letter_already_choosed) 

    if proposition in word: # si ma proposition match avec une lettre dans le mot.
        right_letter = right_letter + proposition
        print("trouvé !")
    elif proposition not in word: 
        life -= 1
#----------------------pour la bonne lettre dans la zone de jeu-----------------------
    zone_Game = ""
    for x in word: #on parcour le mot word avec un var x
        if x in right_letter: # si x match avec la bonne lettre "right_letter"
            zone_Game += x + " " # la bonne lettre right_letter va prendre place dans la zone de jeu 
        else:
            zone_Game += "_ "

    if life == 0: 
        print("tu a perdu, la réponse était :",word)
        break

    if "_" not in zone_Game:
        print (zone_Game)
        print("Bravo vous avez trouvé toute les lettres")
        break
