import random
import math
from function import fn


class Country(object):
    def __init__(self, items: list):
        self.loc = []
        for item in items:
            self.loc.append(item)

    def get_loc(self) -> list:
        '''
        Returns a list which defines the coordinates of the country
        '''
        return self.loc

    def cost(self, fun=fn) -> float:
        '''
        Params function
        Returns the cost of the country based on the param function
        '''
        return fun(self.loc)

    def dist(self, item) -> float:
        '''
        Params country
        Returns the distance between self and param country
        '''
        res = 0
        for i in range(len(item.loc)):
            res += (self.loc[i]-item.loc[i])**2

        return math.sqrt(res)
