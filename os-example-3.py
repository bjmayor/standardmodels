# coding=UTF-8
import os
import string

def replace(file, search_for, replace_with):
    back = os.path.splitext(file)[0] + ".bak"
    temp = os.path.splitext(file)[0] + ".tmp"

    try:
        os.remove(temp) #上次生成的临时文件,第一个执行肯定会报文件不存在,所以加了个try except
    except os.error:
        pass

    fi = open(file)
    fo = open(temp, "w")

    for s in fi.readlines():
        fo.write(string.replace(s, search_for,replace_with))

    fi.close()
    fo.close()


    try: # remove old backup file, if any os.remove(back)
        os.rename(file, back) # ...and temporary to original
        os.rename(temp, file)
    except  os.error:
        pass # rename  original to backup...
## try it out!
file ="samples/sample.txt"
replace(file, "hello", "tjena")
replace(file, "tjena",  "hello")
