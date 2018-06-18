import collections
# custom libraries
from functions import initialize
import dataTypes

# stub: add code to ask user for 
# - life table
# - initial population size
# - initial demographics
# -model run time (in breeding cycles)
lifeTable = [[0, 1, 0], [1, 0.75, 4], [2, 0.4, 5]]
lifeTable_wrightFisher = [[0, 1, 1]]
pop_size = 100
initialDemographics = [0.25, 0.5, 0.25]
maxYears = 10

# a history of every organism that has ever lived (and then died)
organismRecordList = []

# list of organism that are alive. 
currentlyAliveList = []

# DEBUGGING OUTPUT
for ageCohort in lifeTable:
    print("age : ", ageCohort[0], ", survival probability : ", ageCohort[1], ", mean fertility : ", ageCohort[2])


# step 1: create generation 1.
initialize(organismRecordList, currentlyAliveList, pop_size, initialDemographics)

for i in currentlyAliveList:
    print(i)
