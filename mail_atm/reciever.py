#-*- coding:UTF-8 -*-

import imaplib, email, smtplib, time

server = "mail.test.com"
fadd =  "dynamist.sb@gmail.com"
mbody = ["""This is an example!"""]

while True:
    i = imaplib.IMAP4(server, 143)
    i.login("ec21b1042@iiitdm.ac.in", "neebtmlkkrqwsrwy")
    i.select("INBOX")
    types, datas = i.search(None, "NEW")
    ids = datas[0]
    
    if ids == "":
        i.logout()
        pass
    else:
        for n in ids.split():
            typs, dats = i.fetch(n, '(RFC822)')
            for dat in dats:
                if isinstance(dat, tuple):
                    rmsg = email.message_from_string(dat[1])
                    msub = rmsg['subject']
                    mfro = rmsg['from'].replace("<", '').replace(">",'').split()[-1]
                    if (mfro == "test1@test.com") or (mfro == "test2@test.com"):
                        pass
                    else:
                        mhead = ['From:%s' % fadd, 'To:%s' % mfro ,'Subject:%s' % msub]		
                        smsg = "\r\n\r\n".join(['\r\n'.join(mhead), '\r\n'.join(mbody)])
                        s = smtplib.SMTP()
                        s.connect(server)
                        s.starttls()
                        s.login("admin", "neebtmlkkrqwsrwy")
                        s.sendmail(fadd, mfro, smsg)
                        print("Send to %s success!" % mfro)
                        s.quit()
    time.sleep(120)