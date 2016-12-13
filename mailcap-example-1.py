import mailcap
caps = mailcap.getcaps()
for k, v in caps.items():
    print k, "=", v