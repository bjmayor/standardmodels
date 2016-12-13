import dbm
db = dbm.open("dbm", "c")
db["first"] = "bruce"
db["second"] = "bruce"
db["third"] = "bruce"
db["fourth"] = "bruce"
db["fifth"] = "michael"
db["fifth"] = "bruce" # overwrite
db.close()
db = dbm.open("dbm", "r")
for key in db.keys():
    print repr(key), repr(db[key])