###########################
#  Fichier classe.py      #
# 04/04/18                #
# la communauté de l'info #
###########################

import numpy as np
import random

class HMM():
    """ Define an HMM"""

    #mettre des raise...
    #faire des setter

    #virer les Nones
    def __init__(self, letters_number, states_number, initial, transitions, emissions):
        # The number of letters
        self.__letters_number = letters_number
        # The number of states
        self.__states_number = states_number
        # The vector defining the initial weights
        self.__initial = initial
        # The array defining the transitions
        self.__transitions = transitions
        # The list of vectors defining the emissions
        self.__emissions = emissions


    def check_transition(self, value):
        assert len(value) > 0
        if len(value) != self.__states_number or len(value[0]) != self.__states_number:
            raise ValueError("Le tableau est de mauvaises dimensions")
        for i in range (len(value)):
            somme = 0
            for j in range (len(value[0])):
                if value [i,j] < 0:
                    raise ValueError("Toutes les probabilités doivent être positives")
                somme += value[i, j]
            if not np.isclose([somme], [1]):
                raise ValueError("La somme des probabilités doit être égale à 1")

    def check_emissions(self, value):
        assert len(value) > 0
        if len(value) != self.__states_number or len(value[0]) != self.__letters_number:
            raise ValueError("Le tableau est de mauvaises dimensions")
        for i in range(len(value)):
            somme = 0
            for j in range(len(value[0])):
                if value[i, j] < 0:
                    raise ValueError("Toutes les probabilités doivent être positives")
                somme += value[i, j]
            if not np.isclose([somme], [1]):
                raise ValueError("La somme des probabilités doit être égale à 1")


    @property
    def letters_number(self):
        return self.__letters_number

    @property
    def states_number(self):
        return self.__states_number

    @property
    def initial(self):
        return self.__initial

    @property
    def transitions(self):
        return self.__transitions

    @property
    def emissions(self):
        return self.__emissions

    @letters_number.getter
    def get_letters_number(self):
        return self.__letters_number

    @states_number.getter
    def get_letters_number(self):
        return self.__states_number


    @letters_number.setter
    def set_letters_number(self, value):
        if type(value) == int and value >= 0 :
            self.__letters_number = value
        else :
            raise ValueError("Le nombre de lettre doit être un entier positif")

    @states_number.setter
    def set_states_number(self, value):
        if type(value) == int and value >= 0 :
            self.__states_number = value
        else :
            raise ValueError("Le nombre d'états doit être un entier positif")

    @initial.setter
    def set_initial(self, values):
        self.check_initial(values)
        self.__inital = values

           def check_tran'''

    def check_initial(self,values):
        if not isinstance(values, np.ndarray):
            raise ValueError("Le vecteur initial doit être un vecteur")

        else :
            somme = 0
            for i in range (len(values)):
                if values[i] < 0:
                    raise ValueError ("Toutes les probabilités doivent être positives")
                somme += values[i]

            if not np.isclose([somme], [1]):
                raise ValueError ("La somme des probabilités doit être égale à 1")






    """"
    @transitions.setter
    def transitions(self, values):
        values = self.check_transitions(values, self.__states_number)
        self.__transitions = values
    """


    @staticmethod
    def load(adr):
        """charge l'adresse"""

        data = open(adr, 'r')
        line = data.readline()
        hash_count = 0


        while hash_count!= 5:
            if line[0] == '#':
                if hash_count == 0 :
                    letters_number = int(data.readline())

                if hash_count == 1 :
                    states_number = int(data.readline())

                if hash_count == 2 :
                    initial = np.zeros((states_number))
                    for i in range(states_number):
                        initial[0][i] = float(data.readline())

                if hash_count == 3 :
                    transitions = np.zeros((states_number, states_number))
                    for i in range(letters_number):
                        ligne = data.readline().split()
                        for j in range (len(ligne)):
                            transitions[i][j] = float(ligne[j])

                if hash_count == 4 :
                    emissions = np.zeros((states_number, states_number))
                    for i in range(letters_number):
                        ligne = data.readline().split()
                        for j in range(len(ligne)):
                            emissions[i][j] = float(ligne[j])

                hash_count += 1

            line = data.readline()

        data.close()


    def __str__(self):
        return 'The number of letters : ' +  str(self.__letters_number) +'\n' +  ' The number of states : '+ str(self.__states_number) +'\n'+ ' The initial vector : ' +  str(self.__initial) +'\n'+  ' The internal transitions : ' +'\n'+ str(self.__transitions) +'\n'+ ' The emissions : ' +'\n'+ str(self.__emissions)



    def gen_rand(self,n):
        #long
        initial_additionne = np.zeros(len(self.initial))
        for i in range (len(self.initial)):
            if i==0:
                initial_additionne[0] =  self.initial[0]
            else:
                initial_additionne[i] = self.initial[i] + self.initial[i - 1]

        transition_additionne = np.zeros(len(self.transitions), len(self.transitions[0]))
        for i in range(len(self.transitions)):
            for j in range(len(self.transitions[0])):
                if j == 0:
                    transition_additionne[i, 0] = self.transitions[i, 0]
                else:
                    transition_additionne[i, j] = self.transitions[i, j] + self.transitions[i, j-1]

        emissions_additionne = np.zeros(len(self.emissions), len(self.emissions[0]))
        for i in range(len(self.emissions)):
            for j in range(len(self.emissions[0])):
                if j == 0:
                    emissions_additionne[i, 0] = self.emissions[i, 0]
                else:
                    emissions_additionne[i, j] = self.emissions[i, j] + self.emissions[i, j-1]

        nb = random.random()
        for i in range (len(self.initial)):
            p_initial = initial_additionne[i]
            if p_initial >= nb:
                val_initial = i
                break
        val_etat = val_initial
        res = self.letters_number[val_initial]
        for var in range (n):
            for j in range(len(self.transitions[0])):
                p_transition = transition_additionne[val_etat, j]
                if p_transition >= nb:
                    val_transition = j
                break
            for k in range(len(self.emissions[0])):
                p_emission = emissions_additionne[val_etat, k]
                if p_emission >= nb:
                    val_emission = k
                break
            res += self.letters_number[val_emission]
            val_etat = val_transition
        return res

    def save(self, address):
        nfile = open(address, "w")
        nfile.write("# The number of letters\n")
        nfile.write(str(self.letters_number) + "\n")
        nfile.write("# The number of states\n")
        nfile.write(str(self.states_number) + "\n")
        nfile.write("# The initial transitions\n")
        for p in self.initial:
            nfile.write(str(p) + "\n")
        nfile.write("# The internal transitions\n")
        for i in range(len(self.transitions)):
            for j in range(len(self.transitions[0])):
                nfile.write(str(self.transitions[i, j]) + " ")
            nfile.write("\n")
        nfile.write("# The emissions" + "\n")
        for i in range(len(self.emissions)):
            for j in range(len(self.emissions[0])):
                nfile.write(str(self.emissions[i, j]) + " ")
            nfile.write("\n")

        nfile.close()
'''
hmm = HMM(2, 2, np.array([0.5, 0.5]), np.array([[1, 1], [1, 1]]), np.array([[1, 1], [1, 1]]))

hmm.save("test1.txt")

HMM = HMM('test1.txt')
HMM.affiche()'''

hmm1=HMM()
hmm1.load('test2.txt')
print(hmm1)