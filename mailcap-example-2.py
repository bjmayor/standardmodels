import mailcap
caps = mailcap.getcaps()
command, info = mailcap.findmatch(
    caps, "image/jpeg", "view", "samples/sample.png"
    )
print command