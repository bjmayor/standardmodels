import mailbox
mb = mailbox.UnixMailbox(open("/var/spool/mail/effbot"))
while 1:
    msg = mb.next()
    if not msg:
        break
    for k, v in msg.items():
        print k, "=", v
    body = msg.fp.read()
    print len(body), "bytes in body"