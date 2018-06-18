import dataTypes
import random

# populates the livingOrganisms list with pop_size livingOrganismRecords.
def initialize(organismRecordList, livingOrganisms, pop_size, initial_demographics):

    #this block should proportionally add intergers 0 to initial_cohort_size
    # # to a 100-element lookup table
    demographics_lookup_table = []
    for i in range(0, len(initial_demographics)):
        initial_cohort_size = int(initial_demographics[i] * 100)
        for j in range(0, initial_cohort_size):
            demographics_lookup_table.append(i)
  
    for i in range(pop_size):
        d100 = random.randint(0, 99)
        
        organism = dataTypes.OrganismRecord(0, 0)
        liveOrganism = dataTypes.LivingOrganismRecord(organism, 
            demographics_lookup_table[d100])

        livingOrganisms.append(liveOrganism)
   

""" 
   organism1 = dataTypes.OrganismRecord(1, 0, 0)
    livingorganism1 = dataTypes.LivingOrganismRecord(organism1, 55)
    livingOrganisms.append(livingorganism1) 
 """
    
print("initializing!")

