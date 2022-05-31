# 31/05/22
# Gorvien - Perrichet

import multiprocessing as mp
import time

start_time = time.time()

Nb_process = 5

def arc_tan(n):
    """ Chaque process va calculer une somme de même taille et ajouter celle-ci dans la variable partagée pi
Arguments:
    n : nombre d'itération du process
"""
    somme_Part = 0
    for i in range(n):
        somme_Part += 4/(1+ ((i+0.5)/n)**2)
    pi.value += (1/nb_total_iteration)*somme_Part
    


if __name__ == "__main__" :

    nb_total_iteration = 1000000

    nb_iteration_par_process = nb_total_iteration/Nb_process

    listeProcess = []
    mutex = mp.Lock()
    pi = mp.Value('f',0)


    print("Temps d'execution : ", time.time() - start_time)


    for _ in range(Nb_process) :
        process = mp.Process(target = arc_tan, args = (int(nb_iteration_par_process),))
        
        listeProcess.append(process)
        process.start()
    
    for p in listeProcess :
        p.join()

    print("Valeur estimée de Pi : ", pi.value)
