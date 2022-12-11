import datetime,ssl,OpenSSL,csv

f = open('result.txt', 'w')
f.close()

def checker(ip, self_signed, expiration_date, longterm, bad_encryption, validity):
    try:
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
            if(buff.find("SHA256") != -1):
                flag2 = 1
                

        if(bad_encryption[1] == 1 and flag2 == 0):
            buff = str(algoritm)
            if(buff.find("sha1") != -1):
                flag2 = 1
            if(buff.find("SHA1") != -1):
                flag2 = 1

        if(bad_encryption[2] == 1 and flag2 == 0):
            buff = str(algoritm)
            if(buff.find("md5") != -1):
                flag2 = 1
            if(buff.find("MD5") != -1):
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
        print(f"Хороший - {ip}")
    except Exception:
        print(f"Плохой - {ip}")
        pass
def main_script(file,self_signed, expiration_date, longterm, bad_encryption, validity):
    with open(file) as f:
        one = 0
        reader = csv.reader(f)
        for row in reader:

            for i in range(20):
                if row[0][i] == '-':
                    one = i
                    start = row[0][:one - 1]
                    end = row[0][one+2:]
                    print(start, end)
                    a = ["","","",""]
                    count = 0
                    for i in start:
                        if i == '.':
                            count += 1
                        else:
                            a[count] += i
                    print(a)

                    b = ["", "", "", ""]
                    count = 0
                    for i in end:
                        if i == '.':
                            count += 1
                        else:
                            b[count] += i
                    print(b)


                    """
                    for i in range(int(a[0]), int(b[0]) + 1):
                        for j in range(int(a[1]), 256):
                            for w in range(int(a[2]), 256):
                                for z in range(int(a[3]), 256):
                                    checker(f"{i}.{j}.{w}.{z}", self_signed, expiration_date, longterm, bad_encryption, validity)
                    """


                    if (a[0] == b[0]):
                        i = a[0]
                        for j in range(int(a[1]), int(b[1])):
                            for w in range(int(a[2]), int(b[2])):
                                for z in range(int(a[3]), int(b[3])):
                                    checker(f"{i}.{j}.{w}.{z}", self_signed, expiration_date, longterm, bad_encryption, validity)
                    else:
                        for i in range(int(a[0]), int(b[0])):
                            for j in range(int(a[1]), int(b[1])):
                                for w in range(int(a[2]), int(b[1])):
                                    for z in range(int(a[3]), int(b[1])):
                                        checker(f"{i}.{j}.{w}.{z}", self_signed, expiration_date, longterm, bad_encryption, validity)
                    break
            if one == 0:
                a = row[0].split(";")
                for i in range(len(a)):
                    checker(a[i], self_signed, expiration_date, longterm, bad_encryption, validity)
    return 1