# Third party package
import peeweedbevolve

# User modules
import models as m


print("Running migration")

m.db.evolve(ignore_tables={'base_model'})

print("Finish Migration")