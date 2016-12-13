import ConfigParser
import sys
config = ConfigParser.ConfigParser()
# set a number of parameters
config.add_section("book")
config.set("book", "title", "the python standard library")
config.set("book", "author", "fredrik lundh")
config.add_section("ematter")
config.set("ematter", "pages", 250)
# write to screen
config.write(sys.stdout)