import datetime
import ssl
import OpenSSL

"""
self_signed #Самоподписанный сертификат
expiration_date #Время действия сертификата
longterm #Слишком большой срок действия сертификата (Более 397 дней)
bad_encryption #Плохое шифрование
unreliable_organization #Недостоверная организация
key_length #Недостаточная длина ключа
validity #Период действия
"""


def checker(ip, self_signed, expiration_date, longterm, bad_encryption, unreliable_organization, key_length, validity):
    cheks_amount = self_signed + expiration_date + longterm + \
        bad_encryption + unreliable_organization + key_length + validity

    f = open('result.txt', 'a')

    cert = ssl.get_server_certificate((ip, 443))
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)

    issuer = str(x509.get_issuer())
    subject = x509.get_subject()
    After = x509.get_notAfter()
    Before = x509.get_notBefore()
    version = x509.get_version()
    serial_number = x509.get_serial_number()
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

    if(bad_encryption == 1):
        if(algoritm [2:-1] != 'sha256WithRSAEncryption'):
            fails.append("Не стандартный алгоритм подписи сертификата" + (algoritm [2:-1]))

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
    f.write("\n\n")
    f.close()


"""
    if(unreliable_organization == 1):
        #

    if(key_length == 1):
        #
"""


def main_script(file_addr, flags):
    f = open('result.txt', 'w')
    f.close()

    checker("151.101.193.69", 1, 1, 1, 0, 0, 0, 18)  # stack
    checker("93.186.225.194", 1, 1, 1, 0, 0, 0, 99999)  # vk
    checker("213.59.254.7", 1, 1, 1, 0, 0, 0, 31)  # gosuslugi
    print("ok")

main_script(0, 0)