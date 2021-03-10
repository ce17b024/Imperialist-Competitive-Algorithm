from country import Country
from functools import cmp_to_key
import random
import math


class Empire(object):
    def __init__(self, lis):
        self.colonies = lis
        self.weakest = None
        self.imperialist = None

    def size(self) -> int:
        '''
        Returns the size of the empire.
        '''
        return len(self.colonies)

    def __cost__(self):
        if self.imperialist == None:
            self.set_imperialist()

        res = self.imperialist.cost()

        if len(self.colonies) > 1:
            sm = sum([colony.cost() for colony in self.colonies]) - res
            avg = sm/(len(self.colonies)-1)
            res += avg*0.001

        return res

    def __compare__(self, col1, col2):
        return col1.cost() - col2.cost()

    def sort_colonies(self) -> None:
        '''
        Sorts the colonies list in the decreasing order of their power
        '''
        self.colonies = sorted(
            self.colonies, key=cmp_to_key(self.__compare__))

    def set_imperialist(self) -> None:
        '''
        Sets the imperialist of the empire
        '''
        if self.size() > 0:
            self.sort_colonies()
            self.imperialist = self.colonies[0]

    def get_imperialist(self):
        '''
        Returns the imperialist of the empire
        '''
        if self.imperialist == None:
            self.set_imperialist()

        return self.colonies[0]

    def set_weakest(self) -> None:
        '''
        sets the weakest in the empire
        '''
        if self.size() > 0:
            self.sort_colonies()
            self.weakest = self.colonies[-1]

    def get_weakest(self):
        '''
        Returns the weakest colony of the empire
        '''
        if self.weakest == None:
            self.set_weakest()

        return self.weakest

    def remove_weakest(self) -> None:
        '''
        Removes the weakest colony of the empire.
        returns None
        '''
        self.sort_colonies()
        del self.colonies[-1]
        self.set_weakest()
        self.set_imperialist()

    def add_colony(self, col) -> None:
        '''
        Adds a country(param) to the empire
        Params: Country to be added
        Returns: None
        '''
        self.colonies.append(col)
        self.set_weakest()
        self.set_imperialist()

    def assimilate(self):
        '''
        Performs the Assimilation subroutine of the ICA. 
        The explaination of this step can be 
        found in the Project Report page 8.
        Params: No params
        Returns: None
        '''
        new_list = [self.get_imperialist()]
        for colony in self.colonies:
            if colony != self.imperialist:
                v = []  # vector from colony to imperialist
                d = colony.dist(self.get_imperialist())
                if d == 0:
                    d = 1
                x = 2*d*random.random()

                phi = random.random()*math.pi/4
                if random.randint(0, 101) % 2 == 0:
                    phi = -phi

                for i in range(len(colony.loc)):
                    if i == 0:
                        v.append(
                            (self.imperialist.loc[i]-colony.loc[i])*math.cos(phi)*x/d + colony.loc[i])
                    elif i == 1:
                        v.append(
                            (self.imperialist.loc[i]-colony.loc[i])*math.sin(phi)*x/d + colony.loc[i])
                    else:
                        v.append(
                            (self.imperialist.loc[i]-colony.loc[i])*x/d + colony.loc[i])

                temp = Country(v)
                if temp.cost() < colony.cost():
                    new_list.append(temp)
                else:
                    new_list.append(colony)

        self.colonies = new_list
        self.set_imperialist()
        self.set_weakest()
