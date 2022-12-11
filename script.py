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
f = open('result.txt', 'w')
f.close()


def main_script(ip, self_signed, expiration_date, longterm, bad_encryption, unreliable_organization, key_length, validity, days):
    cheks_amount = self_signed + expiration_date + longterm + bad_encryption + unreliable_organization + key_length + validity

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

    if (expiration_date == 1):
        if (x509.has_expired() == True):
            fails.append("Истёк срок действия сертификата;")
            count += 1

    if (longterm == 1):
        Before = str(x509.get_notBefore())
        After = str(x509.get_notAfter())

        aa = datetime.date(int(Before[2:6]), int(Before[7:8]), int(Before[9:10]))
        bb = datetime.date(int(After[2:6]), int(After[7:8]), int(After[9:10]))

        interval = bb-aa
        if(int(interval.days) > 397):
            fails.append("Слишком большой срок действия сертификата;")
            count += 1


    if(count == 0):
        f.write("IP: " + ip + ';' + " Все проверки пройдены успешно.")
    else:
        text = "IP: " + ip + ';' + " Провалено проверок: " + str(count) + ":"
        f.write(text)
        len_ip = len("IP: " + ip + '; ') + 10
        for i in range(len(fails)):
            f.write('\n' + ' ' * len_ip + fails[i])
    f.write("\n")
    f.close()
"""
    if(longterm == 1):
        #

    if(bad_encryption == 1):
        #

    if(unreliable_organization == 1):
        #

    if(key_length == 1):
        #

    if(validity != 0):
        #




    if (x509.has_expired() == False):
        verify = 1
    else:
        verify = 0
    subject = x509.get_subject().get_components()

    if (issuer.find("Let's Encrypt") != -1):
"""

main_script("151.101.193.69", 1, 1, 1, 0, 0, 0, 0, 0) #stack
main_script("93.186.225.194", 1, 1, 1, 0, 0, 0, 0, 0)  # vk
