import grep
import glob
grep.grep("\<rather\>", glob.glob("samples/*.txt"))