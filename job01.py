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



#if lvlChoose == 1 :
#    life = 10 
#elif lvlChoose == 2 :
#    life = 7 
#elif lvlChoose == 3 :
#    life = 4
#
#print("nombre de vies restant :",life)

#qui pourrait marcher !! 

#lvlChoose = int(input("Bonjour, à quel niveau souhaite tu jouer: ")) #Je demande à quel niveau l'utilisateur veux jouer 
life = 10 #les vie de l'utilisateur 

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
entry_Word = input()
for l in word:
    zone_Game = zone_Game + "_ "
if len(word) != entry_Word:
    print("il vous reste",life-1,"vie")


     

#    
print(zone_Game)
print(len(word))
    
