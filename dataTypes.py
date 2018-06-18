import collections

# basic individual organism record. Like a birth certificate.
OrganismRecord = collections.namedtuple('OrganismRecord', 'year_born, parent_id')

# ... and we need to keep track of extra info while they're alive. A wrapper for OrganismRecord
LivingOrganismRecord = collections.namedtuple('LivingOrganismRecord', 'organismRecord, current_age')