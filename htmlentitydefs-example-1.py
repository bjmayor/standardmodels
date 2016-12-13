import htmlentitydefs
entities = htmlentitydefs.entitydefs
print entities
for entity in "amp", "quot", "copy", "yen":
    print entity, "=", entities[entity]
