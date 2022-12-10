import ssl, socket
import OpenSSL

cert=ssl.get_server_certificate(('translate.yandex.ru', 443))
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
issuer = str(x509.get_issuer())
subject = x509.get_subject()
After = x509.get_notAfter()
Before = x509.get_notBefore()
version = x509.get_version()
serial_number = x509.get_serial_number()
algoritm = x509.get_signature_algorithm()
if (x509.has_expired() == False):
    verify = 1
else:
    verify = 0
subject = x509.get_subject().get_components()

if (issuer.find("Let's Encrypt") != -1):
    result = 0

