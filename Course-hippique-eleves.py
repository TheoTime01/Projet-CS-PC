# 31/05/22
# Gorvien - Perrichet

# Cours hippique
# Version très basique, sans mutex sur l'écran, sans arbitre, sans annoncer le gagant, ... ...

# Quelques codes d'échappement (tous ne sont pas utilisés)
CLEARSCR="\x1B[2J\x1B[;H"          #  Clear SCReen
CLEAREOS = "\x1B[J"                #  Clear End Of Screen
CLEARELN = "\x1B[2K"               #  Clear Entire LiNe
CLEARCUP = "\x1B[1J"               #  Clear Curseur UP
GOTOYX   = "\x1B[%.2d;%.2dH"       #  ('H' ou 'f') : Goto at (y,x), voir le code

DELAFCURSOR = "\x1B[K"             #  effacer après la position du curseur
CRLF  = "\r\n"                     #  Retour à la ligne

# Nov 2021
# Course Hippique (version élèves)
# VT100 : Actions sur le curseur
CURSON   = "\x1B[?25h"             #  Curseur visible
CURSOFF  = "\x1B[?25l"             #  Curseur invisible

# VT100 : Actions sur les caractères affichables
NORMAL = "\x1B[0m"                  #  Normal
BOLD = "\x1B[1m"                    #  Gras
UNDERLINE = "\x1B[4m"               #  Souligné


# VT100 : Couleurs : "22" pour normal intensity
CL_BLACK="\033[22;30m"                  #  Noir. NE PAS UTILISER. On verra rien !!
CL_RED="\033[22;31m"                    #  Rouge
CL_GREEN="\033[22;32m"                  #  Vert
CL_BROWN = "\033[22;33m"                #  Brun
CL_BLUE="\033[22;34m"                   #  Bleu
CL_MAGENTA="\033[22;35m"                #  Magenta
CL_CYAN="\033[22;36m"                   #  Cyan
CL_GRAY="\033[22;37m"                   #  Gris

# "01" pour quoi ? (bold ?)
CL_DARKGRAY="\033[01;30m"               #  Gris foncé
CL_LIGHTRED="\033[01;31m"               #  Rouge clair
CL_LIGHTGREEN="\033[01;32m"             #  Vert clair
CL_YELLOW="\033[01;33m"                 #  Jaune
CL_LIGHTBLU= "\033[01;34m"              #  Bleu clair
CL_LIGHTMAGENTA="\033[01;35m"           #  Magenta clair
CL_LIGHTCYAN="\033[01;36m"              #  Cyan clair
CL_WHITE="\033[01;37m"                  #  Blanc

#-------------------------------------------------------
# Juin 2019
# Cours hippique
# Version très basique, sans mutex sur l'écran, sans arbitre, sans annoncer le gagant, ... ...

# Quelques codes d'échappement (tous ne sont pas utilisés)
CLEARSCR="\x1B[2J\x1B[;H"          #  Clear SCReen
CLEAREOS = "\x1B[J"                #  Clear End Of Screen
CLEARELN = "\x1B[2K"               #  Clear Entire LiNe
CLEARCUP = "\x1B[1J"               #  Clear Curseur UP
GOTOYX   = "\x1B[%.2d;%.2dH"       #  ('H' ou 'f') : Goto at (y,x), voir le code

DELAFCURSOR = "\x1B[K"             #  effacer après la position du curseur
CRLF  = "\r\n"                     #  Retour à la ligne

# VT100 : Actions sur le curseur
CURSON   = "\x1B[?25h"             #  Curseur visible
CURSOFF  = "\x1B[?25l"             #  Curseur invisible

# VT100 : Actions sur les caractères affichables
NORMAL = "\x1B[0m"                  #  Normal
BOLD = "\x1B[1m"                    #  Gras
UNDERLINE = "\x1B[4m"               #  Souligné


# VT100 : Couleurs : "22" pour normal intensity
CL_BLACK="\033[22;30m"                  #  Noir. NE PAS UTILISER. On verra rien !!
CL_RED="\033[22;31m"                    #  Rouge
CL_GREEN="\033[22;32m"                  #  Vert
CL_BROWN = "\033[22;33m"                #  Brun
CL_BLUE="\033[22;34m"                   #  Bleu
CL_MAGENTA="\033[22;35m"                #  Magenta
CL_CYAN="\033[22;36m"                   #  Cyan
CL_GRAY="\033[22;37m"                   #  Gris

# "01" pour quoi ? (bold ?)
CL_DARKGRAY="\033[01;30m"               #  Gris foncé
CL_LIGHTRED="\033[01;31m"               #  Rouge clair
CL_LIGHTGREEN="\033[01;32m"             #  Vert clair
CL_YELLOW="\033[01;33m"                 #  Jaune
CL_LIGHTBLU= "\033[01;34m"              #  Bleu clair
CL_LIGHTMAGENTA="\033[01;35m"           #  Magenta clair
CL_LIGHTCYAN="\033[01;36m"              #  Cyan clair
CL_WHITE="\033[01;37m"                  #  Blanc

#-------------------------------------------------------
import multiprocessing as mp
 
import os, time,math, random, sys, ctypes

# Une liste de couleurs à affecter aléatoirement aux chevaux
lyst_colors=[CL_WHITE, CL_RED, CL_GREEN, CL_BROWN , CL_BLUE, CL_MAGENTA, CL_CYAN, CL_GRAY,
             CL_DARKGRAY, CL_LIGHTRED, CL_LIGHTGREEN,  CL_LIGHTBLU, CL_YELLOW, CL_LIGHTMAGENTA, CL_LIGHTCYAN]

def effacer_ecran() : print(CLEARSCR,end='')
def erase_line_from_beg_to_curs() : print("\033[1K",end='')
def curseur_invisible() : print(CURSOFF,end='')
def curseur_visible() : print(CURSON,end='')
def move_to(lig, col) : print("\033[" + str(lig) + ";" + str(col) + "f",end='')

def en_couleur(Coul) : print(Coul,end='')
def en_rouge() : print(CL_RED,end='') # Un exemple !

Mutex = mp.Semaphore(1)
mutex_positions = mp.Semaphore(1)

# La tache d'un cheval
def un_cheval(ma_ligne : int, keep_running) : # ma_ligne commence à 0
    global positionsCanassons
    col=1

    while col < LONGEUR_COURSE and keep_running.value :
        move_to(ma_ligne+1,col)         # pour effacer toute ma ligne
        erase_line_from_beg_to_curs()
        en_couleur(lyst_colors[ma_ligne%len(lyst_colors)])
        Mutex.acquire()
        print(chr(ord('A')+ma_ligne)+'🐎'+chr(ord('A')+ma_ligne))
        Mutex.release()
        col+=1
        mutex_positions.acquire()
        positionsCanassons[ma_ligne] = col
        mutex_positions.release()
        time.sleep(0.1 * random.randint(1,5))

#------------------------------------------------
# La partie principale :
def course_hippique(keep_running) :
    global Nb_process
    Nb_process=20
    mes_process = [0 for i in range(Nb_process)]
    

    effacer_ecran()
    curseur_invisible()

    for i in range(Nb_process):  # Lancer     Nb_process  processus
        mes_process[i] = mp.Process(target=un_cheval, args= (i,keep_running,))
        mes_process[i].start()
        pArbitre = mp.Process(target=arbitre, args=(Nb_process,))
        pArbitre.start()
    move_to(Nb_process+10, 1)
    print("tous lancés")


    for i in range(Nb_process): 
      mes_process[i].join()
      pArbitre.join()
    
    print("tous lancés")


    move_to(24, 1)
    curseur_visible()
    print("Fini")


# Arbitre
def arbitre(number):
  while(keep_running):
   
    mutex_positions.acquire()
    pos_firstCanasson = 0
    nb_firstCanasson = 0
    pos_lastCanasson = 99
    nb_lastCanasson = 0
 
    for i in range(Nb_process):
      move_to(Nb_process+11, 1)
      erase_line_from_beg_to_curs()
      print("posCan[i]",positionsCanassons[i])
      move_to(Nb_process+12, 1)
      erase_line_from_beg_to_curs()
      print("pos_firstCanasson",pos_firstCanasson)
      if(positionsCanassons[i] > pos_firstCanasson):
        pos_firstCanasson = positionsCanassons[i]
        nb_firstCanasson = i
 
      if(positionsCanassons[i] < pos_lastCanasson):
        pos_lastCanasson = positionsCanassons[i]
        nb_lastCanasson = i
 
    mutex_positions.release()
 
    # Affichage du titre Arbitre
    move_to(number+2, 1)
    erase_line_from_beg_to_curs()
    print('Arbitre :')
    # Affichage du Canasson de tête
    move_to(number+3, 1)
    erase_line_from_beg_to_curs()
    print("Canasson : ",chr(ord('A')+nb_firstCanasson),'en tête (',pos_firstCanasson,' )')
    # Affichage du Canasson de queue
    move_to(number+4, 1)
    erase_line_from_beg_to_curs()
    print("Canasson : ",chr(ord('A')+nb_lastCanasson),'en queue (',pos_lastCanasson,' )')
 
    # Sortie en cas de victoire
    if(pos_firstCanasson == 100):
      break
 
  winners = "Canasson(s) vainqueur(s) :"
  mutex_positions.acquire()
  for i in range(Nb_process):
    if(positionsCanassons[i] == 100):
      winners += " " + chr(ord('A')+i)
    mutex_positions.release()
    move_to(Nb_process+11, 1)
  print(winners)
 
#−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
 
positionsCanassons = mp.Array('i', 20) # Tableau de deux entiers
# ---------------------------------------------------
# La partie principale :
if __name__ == "__main__" :
    LONGEUR_COURSE = 100 # Tout le monde aura la même copie (donc no need to have a 'value')
    keep_running=mp.Value(ctypes.c_bool, True)

    course_hippique(keep_running)
    
