from country import Country
from empire import Empire
import random
import math
from functools import cmp_to_key
from function import fn


list_of_countries = []

# number of countries used in the algorithm.
NUM_OF_COUNTRIES = 100

for i in range(NUM_OF_COUNTRIES):
    temp = Country([random.random()*random.randint(-100, 100),
                    random.random()*random.randint(-100, 100)])
    list_of_countries.append(temp)


def compare(con1, con2):
    return con1.cost()-con2.cost()


list_of_countries = sorted(list_of_countries, key=cmp_to_key(compare))

list_of_imperialists = []

# number of imperialists at initialization.
IMPERIALIST_COUNT = 10

for i in range(IMPERIALIST_COUNT):  # to make 8 empires intially
    list_of_imperialists.append(list_of_countries[i])

empires = [[item] for item in list_of_imperialists]

for i in range(IMPERIALIST_COUNT):  # removing imperialists from the list_of_countries
    del list_of_countries[0]

random.shuffle(list_of_countries)

NUM = 4
j = 0

for i in range(len(list_of_countries)):
    if i % NUM == 0:
        j = (j+1) % IMPERIALIST_COUNT

    empires[j].append(list_of_countries[i])


list_of_empires = [Empire(item) for item in empires]


def cmp(emp1, emp2):
    # cmp function used for sorting empires in the algorithm implemention.
    return emp1.__cost__() - emp2.__cost__()


file_hndl = open("function_value_data.txt", 'w')
file_hndl.write(
    "Function Value(for imperialist of the most powerful empire)\nat in each iteration: \n")

counter = 0
COUNT_MAX_VAL = 100
while len(list_of_empires) > 1 and counter < COUNT_MAX_VAL:
    counter += 1
    # iterate untill only one empire is left.
    for i in range(len(list_of_empires)):
        # assimilate each of the empires in the list_of_empires
        list_of_empires[i].assimilate()

    fVal = list_of_empires[0].__cost__()
    file_hndl.write(str(fVal)+'\n')

    # sort the list_of_empires based on the cmp function. cmp function(line 44) sorts
    # the list in the decreasing order of power or increasing order of cost of the empire.
    list_of_empires = sorted(list_of_empires, key=cmp_to_key(cmp))
    # the weakest empire is the last one in the sorted list
    weakest_empire = list_of_empires[-1]
    # index is randomly generated
    index = random.randint(0, len(list_of_empires)-2)
    # the weakest colony of the weakest empire is then added to a more powerful empire of index
    # generated above
    list_of_empires[index].add_colony(weakest_empire.get_weakest())
    # the weakest colony of the weakest empire is then removed from the weakest empire
    weakest_empire.remove_weakest()

    if weakest_empire.size() == 0:
        # this is elimination step
        # we delete the weakest empire if its size reduces to 0.
        del list_of_empires[-1]


list_of_empires = sorted(list_of_empires, key=cmp_to_key(cmp))
fVal = list_of_empires[0].__cost__()
file_hndl.write(str(fVal)+'\n')
file_hndl.close()

print("optima: ", list_of_empires[0].get_imperialist().get_loc(),
      "\nfunction value optima: ", list_of_empires[0].get_imperialist().cost())
