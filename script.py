import datetime
import ssl
import OpenSSL

f = open('result.txt', 'w')
f.close()

def checker(ip, self_signed, expiration_date, longterm, bad_encryption, validity):
    f = open('result.txt', 'a')

    cert = ssl.get_server_certificate((ip, 443))
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)

    issuer = str(x509.get_issuer())
    After = x509.get_notAfter()
    Before = x509.get_notBefore()
    algoritm = x509.get_signature_algorithm()
    
    fails = []

    count = 0
    if (self_signed == 1):
        if (issuer.find("Let's Encrypt") != -1):
            fails.append("Самоподписанный сертификат;")
            count += 1
    flag1 = 0
    if (expiration_date == 1):
        if (x509.has_expired() == True):
            fails.append("Истёк срок действия сертификата;")
            count += 1
            flag1 = 1

    if (longterm == 1):
        Before = str(x509.get_notBefore())
        After = str(x509.get_notAfter())

        aa = datetime.date(int(Before[2:6]), int(
            Before[7:8]), int(Before[9:10]))
        bb = datetime.date(int(After[2:6]), int(After[7:8]), int(After[9:10]))

        interval = bb-aa
        if (int(interval.days) > 397):
            fails.append("Слишком большой срок действия сертификата (" + str(interval.days) + "д.);")
            count += 1
    
    flag2 = 0
    if(bad_encryption[0] == 1):
        buff = str(algoritm)
        if(buff.find("sha256") != -1):
            flag2 = 1
            

    if(bad_encryption[1] == 1 and flag2 == 0):
        buff = str(algoritm)
        if(buff.find("sha1") != -1):
            flag2 = 1

    if(bad_encryption[2] == 1 and flag2 == 0):
        buff = str(algoritm)
        if(buff.find("md5") != -1):
            flag2 = 1

    if(flag2 == 0):
        fails.append("Алгоритм подписи сертификата: " + str(algoritm))

    if (validity != 0 and flag1 == 0):
        today_date = datetime.datetime.now()
        After = str(x509.get_notAfter())
        print(today_date)

        aa = datetime.date(today_date.year, today_date.month, today_date.day)
        bb = datetime.date(int(After[2:6]), int(After[7:8]), int(After[9:10]))

        interval = bb-aa
        if (int(interval.days) < validity):
            fails.append("Сертификат истечёт через " + str(interval.days) + "д.;")
            count += 1


    if (count == 0):
        f.write("IP: " + ip + ';' + " Все проверки пройдены успешно.")
    else:
        text = "IP: " + ip + ';' + " Провалено проверок: " + str(count) + ":"
        f.write(text)
        len_ip = len("IP: " + ip + '; ')
        for i in range(len(fails)):
            f.write('\n' + ' ' * len_ip + fails[i])

    sha1_fingerprint = x509.digest("sha1")
    f.write("\n" + "    Слепок сертификата: " + str(sha1_fingerprint))
            
    f.write("\n\n")
    f.close()